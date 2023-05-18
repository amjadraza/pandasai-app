FROM python:3.10-slim-bullseye

ENV HOST=0.0.0.0

ENV LISTEN_PORT 8501

EXPOSE 8501

RUN apt-get update && apt-get install -y git

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

WORKDIR app/

COPY ./pandasai_app /app/pandasai_app
COPY ./.streamlit /app/.streamlit

CMD ["streamlit", "run", "pandasai_app/main.py"]
