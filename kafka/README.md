# Kafka Queue with Kafka

For this Example we will generate 2 docker services "Producer" and "Consumer" and build kafka from source.
+ Producer will send items to kafka topic in async tasks
+ Consumer will retrieve them and show it to screen using multithreading

To try this you will need docker and docker-composer installed:
    sudo apt-get install docker docker-compose
    sudo usermod -a -G docker $USER
    

To stat it just:
    ./deploy.sh