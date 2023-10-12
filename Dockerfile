# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set the working directory to /app
WORKDIR /app

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Copy all the files in the current directory to the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit when the container launches
CMD ["streamlit", "run", "streamlit.py"]
