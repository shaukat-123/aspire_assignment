FROM python:3.12
# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
# Update and install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean
# Set the working directory
WORKDIR /target
# Copy the requirements file into the container
COPY requirements.txt .
# Create a virtual environment and install dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
#    pip install wheel && \
    pip install -r requirements.txt
# Copy the rest of the application code
COPY . .
# Ensure the virtual environment is activated
ENV VIRTUAL_ENV=/target/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#EXPOSE 8080
# Specify the command to run the application
#CMD python3 manage.py runserver 0.0.0.0:8080
ENTRYPOINT ["/target/docker-entrypoint.sh"]






