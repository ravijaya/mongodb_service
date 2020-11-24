FROM python:3.8

# set the working directory in the container
WORKDIR /app

# ENV DATABASE=mongodb:///
#ENV PASSWORD=rootpassword
#ENV USERNAME=root

# copy the dependencies file to the working directory
COPY requirements.txt .
# COPY default-data.py .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local directory to the working directory
COPY . .


CMD ["python3", "default-data.py"]
