# Kafka Queue with Kafka

For this Example we will generate 2 docker services "Producer" and "Consumer" and build a kafka broker from image.
+ Producer will send items to kafka topic using multithreading
+ Consumer will retrieve them and show it to screen in async tasks

To try this you will need docker and docker-composer installed:
```
    sudo apt-get install docker docker-compose
    sudo usermod -a -G docker $USER
```
    

To stat it just:
    ./start.sh