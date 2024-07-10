# Use an official Python runtime as a parent image
FROM python:3.8-slim AS builder

# Set the working directory in the container
WORKDIR /app

ENV MINIO_ROOT_USER=Anthony
ENV MINIO_ROOT_PASSWORD=AnthonyBassil
# Copy the current directory contents into the container at /app
COPY api/requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY api/ /app

# Final stage
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /app /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]

