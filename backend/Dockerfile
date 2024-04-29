FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10 AS base

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY source /app/source
COPY asset /app/asset
COPY run.py /app/run.py

FROM base AS prod
EXPOSE 80

CMD [ "python", "run.py" ,"-p","80"]


FROM base AS dev
CMD [ "python", "run.py" ]
