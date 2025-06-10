# Pawparazzi
## Package Setup
Install the Package by running from within
```bash
pip install .
```
## Testing the API locally
Open a shell and run
```bash
make run_api
```
In a second shell test whether the API works using
```bash
make load_image
```
This will send `test/labrador_test_image.jpg` to the running Uvicorn server.
Alternatively you can use
```bash
curl -X POST -F "img=@t<path/to/image>.jpg" http://localhost:8000/upload_image
```
