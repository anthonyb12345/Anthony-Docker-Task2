## Docker Compose Configuration Explanation

### Volumes

The `volumes` keyword in Docker Compose (`docker-compose.yml`) allows you to define named volumes or bind mounts. These volumes provide persistent storage for your containers, ensuring data persists even if the container is stopped or removed. 


### Networks

The `networks` keyword in Docker Compose allows you to define custom networks and specify network-specific options for your services. Networks isolate containers and control how they communicate.


### Depends-On

The `depends_on` keyword in Docker Compose specifies the startup order dependency between services. It ensures one service starts only after another has started.



