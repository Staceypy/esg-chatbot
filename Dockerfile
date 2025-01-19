# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables for Pinecone and OpenAI API keys (from .env or through Docker)
# Copy .env file into the container (optional)
COPY .env /app/.env

# Expose the port the app runs on (if necessary for interaction)
EXPOSE 8000

# Command to run the application
CMD ["python", "chatbot.py"]
