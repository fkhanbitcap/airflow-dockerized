FROM python:3.8.6-buster

# Attach work directory
WORKDIR /app

# Install requirements
RUN pip install -U python-boilerplate==0.4.10 pylint tox==3.20.1 Sphinx==3.3.1 invoke==1.4.1

# Copy code files
COPY . .

# Code styling
RUN pylint devchallenge

# perform virtual test
RUN python3 -m tox

# Clean build
RUN invoke clean build

CMD ["/bin/sh"]