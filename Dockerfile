# set base image
FROM python:3

# set working directory in the container
WORKDIR /myapp

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the content of the src directory (where the app.py is located) to the working directory
COPY src/. .

CMD ["python", "./app.py"]
