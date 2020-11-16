FROM python:3.8.6-buster

# Attach work directory
WORKDIR /app

# Copy code files
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# Copy code files
COPY . .

# Code styling
RUN pylint src

# perform virtual test
RUN python3 -m tox

# Clean build
RUN invoke clean build

# Serve documenation
ENTRYPOINT ["python", "-m", "src"]

