### Docker Concepts Q&A

1. **If Docker containers are like shipping containers, what would the Docker image be?**

   Answer: A Docker image is like the blueprint or design of what goes inside the shipping container.

2. **You want to ensure your container is running fine and healthy. Which Docker feature will you use to monitor its health?**

   Answer: You can use Docker's health checks to monitor the health of a container.

3. **If a Docker network is like a company's internal LAN, what would docker-compose.yml be?**

   Answer: Docker-compose.yml would be like the company's networking configuration document.

4. **You have two services, frontend and backend, and you want to ensure that backend starts before frontend. Which Docker Compose key value will you use?**

   Answer: depends_on

5. **If Docker volumes are like USB drives, what does the volumes key in Docker Compose do?**

   Answer: The `volumes` key in Docker Compose specifies data volumes to be mounted inside containers, similar to plugging in USB drives.

6. **You need to create multiple instances of the same service. What feature of Docker Compose will you use?**

   Answer: scale

7. **If Docker networks are like chat rooms, what would the bridge network mode be?**

   Answer: The bridge network mode in Docker is like a private chat room where containers can communicate internally.

8. **You want to limit the CPU usage of a specific container. Which Docker Compose key value will you use?**

   Answer: cpus

9. **If the Docker Hub is like a public library, what would docker pull be?**

   Answer: `docker pull` is like borrowing a book from the public library, where you download Docker images from Docker Hub.

10. **You need to pass environment variables to a container to configure its settings. Which Docker Compose key value will you use?**

    Answer: environment

11. **If a Docker container is like a running application on your computer, what would the Dockerfile be?**

    Answer: The Dockerfile is like the set of installation instructions or setup script for the application.

12. **You want to make sure a container only starts if another service is successfully running. Which Docker Compose feature helps with this dependency management?**

    Answer: depends_on

13. **If the Docker Compose file (docker-compose.yml) is like a party invitation list, what would the services section be?**

    Answer: The services section in Docker Compose is like the list of guests invited to the party, specifying the containers to be run.

14. **You want to share data between multiple running containers. What Docker feature will you use?**

    Answer: Docker volumes or shared volumes allow you to share data between multiple running containers.

15. **If Docker CLI commands are like the controls on a remote control, what would docker-compose up -d do?**

    Answer: `docker-compose up -d` is like pressing the power button on the remote control, starting Docker containers in detached mode.

16. **You need to add a host device (like a GPU) to your container. Which Docker Compose key value will you use?**

    Answer: devices

17. **If Docker containers are like individual apartments, what would docker-compose be?**

    Answer: Docker-compose is like the apartment building manager, orchestrating and managing multiple Docker containers.

18. **You want to ensure that your service only uses a specific amount of memory. Which Docker Compose key value will you use?**

    Answer: mem_limit

19. **If Docker Compose networks are like different floors in a building, what would the networks key in the Docker Compose file be?**

    Answer: The `networks` key in Docker Compose defines different virtual networks (or floors) where containers communicate.

20. **You need to run a specific command every time your container starts. Which Docker Compose key value will you use?**

    Answer: command