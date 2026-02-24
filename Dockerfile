FROM python:3.10-slim

WORKDIR /app

# Install required system libraries
RUN apt-get update && apt-get install -y \
        build-essential \
        libgl1 \
        libglib2.0-0 && \
        rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]