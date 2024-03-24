# start by pulling the python image
FROM python:3.11.3

EXPOSE 5000

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# switch working directory
WORKDIR /flask-app

# copy the requirements file to the working directory
COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip

# install the requirements
RUN pip install --upgrade -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# configure the container to run in an executed manner
ENTRYPOINT [ "python" , "app.py" ]