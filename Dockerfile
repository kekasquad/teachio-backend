FROM python:3.10-slim

WORKDIR /app

COPY requirements.prod.txt .
RUN pip install -r requirements.prod.txt

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python -m compileall .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "teachio_backend.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]