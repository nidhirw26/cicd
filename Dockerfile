FROM python:3.9-slim

# Set the shell to /bin/sh for compatibility
SHELL ["/bin/sh", "-c"]

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application
COPY . /app

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
