# Install python version
FROM tensorflow/tensorflow:2.16.1

# Install requirements
COPY requirements_prod.txt /requirements.txt
RUN apt-get update && apt-get install -y libgl1
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#Copy pawparazzi code
COPY pawparazzi /pawparazzi

#Copy the model
ARG model
COPY models/${model} /models/model.keras

#Execute the Uvicorn app
CMD uvicorn pawparazzi.api.fast:app --host 0.0.0.0 --port $PORT
