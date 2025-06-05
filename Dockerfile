FROM python:3.10-slim

# Set working directory
WORKDIR /code

# Install system dependencies for image handling (used by PIL, CLIP, etc.)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Make run.sh executable
RUN chmod +x run.sh

# Expose the port FastAPI will run on
EXPOSE 7860

# Start the app
CMD ["bash", "run.sh"]
