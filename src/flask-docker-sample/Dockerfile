# build: docker build -t flask-sample:latest .
# run:   docker run -it -p 5000:5000 flask-sample

FROM ubuntu:latest
MAINTAINER Richard Irving "irvingr@us.ibm.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]


