FROM python:3.10.6-buster
COPY pawparazzi /pawparazzi
COPY requirements_prod.txt /requirements.txt
COPY models/model.keras /models/model.keras
RUN apt-get update && apt-get install -y libgl1
RUN pip install --no-cache-dir -r requirements.txt
CMD uvicorn pawparazzi.api.fast:app --host 0.0.0.0 --port $PORT
