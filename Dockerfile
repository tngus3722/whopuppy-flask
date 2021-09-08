FROM python:3.7.0

WORKDIR /test
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install pillow
RUN pip install tensorflow
EXPOSE 5000

CMD python ./app.py
