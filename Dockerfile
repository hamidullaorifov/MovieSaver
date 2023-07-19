FROM python:3.10.1

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Django project
COPY . .

# Expose port (if necessary)
# EXPOSE 8000

# Start the Django application
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]