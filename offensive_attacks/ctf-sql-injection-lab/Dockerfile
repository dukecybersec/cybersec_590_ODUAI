FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy compiled application files (NO SOURCE CODE)
COPY app.pyc .
COPY main.py .
COPY templates/ ./templates/

# Create a non-root user
RUN useradd -m -u 1000 ctfuser && chown -R ctfuser:ctfuser /app
USER ctfuser

# Expose port
EXPOSE 5000

# Run the application using the wrapper script
CMD ["python", "main.py"]
