docker build -t flapp .
docker run -d -p 5000:5000 flapp
docker container list