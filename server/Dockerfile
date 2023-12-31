# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        binutils \
        libproj-dev \
        gdal-bin \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /code

COPY ./requirements.txt /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the local code into the container
COPY . /code/

# Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python manage.py migrate && uvicorn --workers=4 --timeout-keep-alive=10 config.asgi:application --host=0.0.0.0 --port=8080
