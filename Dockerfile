FROM python:3.7

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 80

# Set the environment variables
ENV PORT=80

# Run any pre-startup commands (if needed)
# CMD ["sh", "-c", "python initialize.py && gunicorn -b :80 -w 3 gavel:app"]

# Run Celery worker and Gunicorn server concurrently
CMD ["sh", "-c", "python initialize.py && celery -A gavel:celery worker --loglevel=info & gunicorn -b :80 -w 3 gavel:app"]

# Copy the application code into the container
COPY . .
