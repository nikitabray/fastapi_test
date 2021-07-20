FROM tiangolo/uvicorn-gunicorn:python3.8
RUN pip install fastapi[all]
COPY ./app /app
