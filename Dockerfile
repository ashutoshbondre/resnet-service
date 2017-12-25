# our base image
FROM python:3.6

WORKDIR /resnet_service
ADD . /resnet_service

# install Python modules needed by the Python app
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "src/application.py"]
