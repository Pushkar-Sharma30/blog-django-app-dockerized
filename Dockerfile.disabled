# Use official Python image
FROM python:3.11-slim


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# Install dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config && \
    pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*



# Copy project files
COPY . /app/

# Collect static files (optional, only if you're using them)
RUN python manage.py collectstatic --noinput

# Expose port 8000 (Django default)
EXPOSE 8000

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


