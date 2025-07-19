# 使用多階段構建來減少最終映像大小
FROM python:3.11-slim as builder

# 設置工作目錄
WORKDIR /app

# 安裝構建依賴
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 複製並安裝 Python 依賴
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# 生產階段
FROM python:3.11-slim

# 創建非 root 用戶
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 設置工作目錄
WORKDIR /app

# 從構建階段複製已安裝的包
COPY --from=builder /root/.local /home/appuser/.local

# 複製應用程式碼
COPY run.py .
COPY app/ ./app/

# 更改文件所有權
RUN chown -R appuser:appuser /app

# 切換到非 root 用戶
USER appuser

# 設置 PATH 以包含用戶安裝的包
ENV PATH=/home/appuser/.local/bin:$PATH

# 暴露端口
EXPOSE 8000

# 健康檢查 - 使用更輕量的方法
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# 啟動應用 - 使用 run.py 作為入口點
CMD ["python", "run.py"]