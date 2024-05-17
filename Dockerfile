FROM python:3.8.19-slim-bullseye

WORKDIR /flask

COPY app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /app .

CMD [ "flask", "run", "--host=0.0.0.0"]