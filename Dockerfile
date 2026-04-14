# 1. Image Python (lightweight)
FROM python:3.9-slim

# 2. set the working directory in the container
WORKDIR /app

# 3. copy the requirements file to the container
COPY requirements.txt .

# 4. Install the 'requests' library inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the Python script and the urls.txt file to the container
COPY main.py urls.txt .

# 6. Set the command to run the Python script when the container starts
CMD ["python", "main.py"]