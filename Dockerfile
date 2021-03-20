FROM python:3.8.8-alpine3.13
RUN pip install uvicorn fastapi motor && \
    mkdir /app
EXPOSE 8000
COPY rest_api /app/
WORKDIR /app
ENTRYPOINT ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
