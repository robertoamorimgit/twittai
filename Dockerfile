FROM python:3.9-slim

WORKDIR /app

COPY requisitos.txt .
RUN pip install --no-cache-dir -r requisitos.txt

COPY . .

CMD ["python", "main.py"]
