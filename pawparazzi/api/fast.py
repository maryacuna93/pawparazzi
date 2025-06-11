from pawparazzi.breed_predict.predict import predict_breed, load_model
from pawparazzi.breed_predict.names import DOG_BREEDS

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import numpy as np
import cv2
import matplotlib.pyplot as plt

app = FastAPI()
app.state.model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def root():
    return {'greeting': 'Hello'}

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    contents = await img.read()

    nparr = np.frombuffer(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    id = predict_breed(cv2_img, app.state.model)
    breed = DOG_BREEDS[id]

    return {'prediction':breed}
