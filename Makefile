.DEFAULT_GOAL := default
################### PACKAGE ACTIONS ####################
run_api:
	uvicorn pawparazzi.api.fast:app --reload

load_image:
	curl -X POST -F "img=@test/labrador_test_image.jpg" http://localhost:8000/upload_image
