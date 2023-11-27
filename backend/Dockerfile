FROM python:3.8-slim

RUN pip install -U pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir markupsafe==2.0.1 flask~=1.1.2 langchain openai
RUN pip3 install tiktoken

COPY app /app

# Expose the port
EXPOSE 80

# Set the working directory
WORKDIR /app

# RUN pip install -r requirements.txt

# Run the flask server for the endpoints
CMD python -u app.py