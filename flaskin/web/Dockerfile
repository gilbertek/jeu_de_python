FROM alpine

# Install required packages
RUN apk update
RUN apk upgrade
RUN apk add --update python \
  python-pip \
  python-dev \
  py-pip \
  build-essential \


# Initialize
RUN mkdir -p /app
COPY . /app
WORKDIR /app

# Setup
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Prepare
ENTRYPOINT ["python"]
CMD ["app.py"]
