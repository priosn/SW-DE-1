# syntax=docker/dockerfile:1

# Use an official Python Image (version=3.10.4)
FROM python:3.10.4

# Copy the directory app into the image
COPY . /app

# Set the working directory
WORKDIR /app

## Update pip package and installs all packages specified in requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Run flask Application
CMD ["python", "app.py"]