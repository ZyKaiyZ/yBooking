#!/bin/bash

IMAGE_NAME="ybooking-frontend"
IMAGE_TAG="latest"

docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .

docker run -d -p 8888:8888 --name "${IMAGE_NAME}" "${IMAGE_NAME}:${IMAGE_TAG}" 
