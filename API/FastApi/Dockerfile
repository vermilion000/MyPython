FROM python:3.10-slim

WORKDIR /fastapi
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ..
ENTRYPOINT ["python", "fastapi.py"]
CMD ["--port", "8080"]
