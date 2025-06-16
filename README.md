# Pawparazzi

Pawparazzi is a project backend to predict dog breeds from images.
Building on the Stanford Dogs and the Tsinghua Dogs datasets, we built a vision
model to classify the breeds of dogs in images submitted by users.
This Repository is the backend of the
[Pawparazzi](https://pawparazzi.streamlit.app/) web application.

## Table of contents

- [Installation](#installation)
- [Model Section](#model-section)
- [Local use](#local-use)
- [Docker Image](#docker-image)
- [Deploying](#deploying)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)


## Installation

To install the pawparazzi package, clone the repository, navigate into it and install the package using pip:
```bash
pip install .
```
### Environment variables
The package will need a few environment variables to run and easily deploy automatically. You can set them in a `.env` file in the root directory of the repository. The required variables are:
```bash
#Model variables
MODELS_LOCATION=<path to the model directory>
MODEL_NAME=<name of the model>

#Docker variables
DOCKER_IMAGE_NAME=pawparazzi
DOCKER_REPO_NAME=<your docker repository name>
DOCKER_LOCAL_PORT=8080

#Google Cloud variables
GOOGLE_CLOUD_PROJECT_ID=<google cloud project id>
GOOGLE_CLOUD_REGION=<google cloud region>
GAR_MEMORY=<memory for the container, e.g. 4Gi>
```
For running the API on Cloud Run, there needs to be an `env.yaml`. See in [Deploying](#deploying) for more information.

## Model Section

The chosen Model archtecture is based on *Resnet(?)* and was trained on a class
balanced version of the Stanford Dogs and Tsinghua Dogs datasets. The notebook
used to train the final model was `notebooks/<thenotebook.ipynb>`. The accuracy
of the model on our test set was about 80%, with 97% accuracy within the top 5. The two datasets miss some prominent dog breeds.
## Local use
### Running the API
Open a shell and run
```bash
make run_api
```
which will start a Uvicorn server on port 8000. The API is built with FastAPI and provides an endpoint to upload images for breed prediction.
To test the api you can run the following command in a second shell:
```bash
make load_image
```
This will send `test/labrador_test_image.jpg` to the running Uvicorn instance.
Alternatively you can use
```bash
curl -X POST -F "img=@t<path/to/image>.jpg" http://localhost:8000/upload_image
```
or interact with the FastAPI genereated documentation at `http//localhost:8000/docs`
## Docker Image
To build the Docker image, run the following command in the root directory of the repository:
```bash
make build_image
```
This will create a Docker image named `pawparazzi` with the latest version of the code and all dependencies installed.
## Deployment on Google Cloud Run

### Building the container

### Deploying
Environment yaml:
```yaml
LOCAL_REGISTRY_PATH: "<models directory path>"
MODEL_NAME: "<model file name>"

GCP_PROJECT: "<google cloud project id>"
GCP_REGION: "<google cloud project region>"

DOCKER_IMAGE_NAME: "pawparazzi"
DOCKER_REPO_NAME: "<docker repository name>"
MEMORY: "<memory allocation, e.g. 4Gi>"
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
