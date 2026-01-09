FROM python:3.11-slim

WORKDIR /app

COPY calculator.py .

ENTRYPOINT ["python", "calculator.py"]
