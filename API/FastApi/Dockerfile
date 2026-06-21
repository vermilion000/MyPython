FROM python:3.10-slim

WORKDIR /fastapi
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ..
CMD ["python","fastapi.py"]
