# 1. Image Python (lightweight)
FROM python:3.9-slim

# 2. set the working directory in the container
WORKDIR /app
# 3. set environment variables for the API URL and input filename
ENV IS_GD_API_URL="https://is.gd/create.php"
ENV INPUT_FILENAME="urls.txt"
# 4. copy the requirements file to the container
COPY requirements.txt .

# 5. Install the 'requests' library inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the Python script and the urls.txt file to the container
COPY main.py urls.txt .

# 7. Set the command to run the Python script when the container starts
CMD ["python", "main.py"]