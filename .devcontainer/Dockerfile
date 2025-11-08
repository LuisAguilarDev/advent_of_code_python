FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

WORKDIR /workspace

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


