# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir fiftyone

# Make port 5151 available to the world outside this container
EXPOSE 5151

# Make the script executable
RUN chmod +x start.sh

# Run start.sh when the container launches
# CMD ["./start.sh"]
CMD ["python", "app.py", "--detections", "--segmentations", "--points"]
