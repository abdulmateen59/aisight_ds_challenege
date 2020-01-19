FROM python:latest
RUN pip3 install -U scikit-learn pandas
COPY . /home/WORKSPACE
WORKDIR /home/WORKSPACE


# $ docker build -t aisight . && docker run -it --rm aisight /bin/bash 
# $ python3 main.py
