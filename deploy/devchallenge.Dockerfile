FROM python:3.8.6-buster

# Attach work directory
WORKDIR /app

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy code files
COPY . .

RUN pip install python-boilerplate==0.4.10

# Clean build
RUN invoke clean build

RUN python3 -m tox