# 使用官方Python运行时作为父镜像
FROM python:3.8-slim-buster

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到容器的/app目录
COPY . /app

# 安装requirements.txt中指定的任何所需包
RUN pip install --no-cache-dir -r requirements.txt

# 使端口80可用于此容器外的世界
EXPOSE 80

# 定义环境变量
ENV NAME LLM-RAG-Online-Course

# 在容器启动时运行app.py
CMD ["python", "src/api/app.py"]