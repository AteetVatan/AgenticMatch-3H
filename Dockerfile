FROM python:3.10-slim

# Install image/model system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# permission error by setting writable cache path
ENV TRANSFORMERS_CACHE=/tmp/hf_cache
ENV HF_HOME=/tmp/hf_cache

# Ensure entrypoint is executable
RUN chmod +x run.sh

EXPOSE 7860
CMD ["bash", "run.sh"]
