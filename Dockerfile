FROM python:3.7

WORKDIR /app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
ENV PORT=80
CMD ["sh", "-c", "python initialize.py && gunicorn -b :80 -w 3 gavel:app"]

COPY . .