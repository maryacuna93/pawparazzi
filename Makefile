.DEFAULT_GOAL := default
################### PACKAGE ACTIONS ####################
run_api:
	uvicorn pawparazzi.api.fast:app --reload
