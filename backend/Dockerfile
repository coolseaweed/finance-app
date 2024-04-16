FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10 AS base

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY source /app/source
COPY run.py /app/run.py

FROM base AS prod
EXPOSE 80

CMD [ "python", "run.py" ]


# FROM RPOD AS DEV