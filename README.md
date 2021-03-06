# Semester Project - Virtualization 1 WS2019 / 2020
## Bergische Universität Wuppertal

### Project 
In Docker you should run a MQTT message broker and a database as well as some glue code (3 containers)

### Tasks
1. a container with a standard MQTT server of your choice and
2. a database of your choice. Configure both accordingly.
3. Write a code that calculates prime numbers and sends them to your server, which uses the
MQTT protocol. The glue code picks the numbers from MQTT and writes them into a
database of your choice inside containers.
4. Develop a way to show your results.

## Directories
- **GlueCode :** glueCode.py
- **MongoDB :** build,sh, run.sh, Dockerfile
- **Mosquitto :** build,sh, run.sh, Dockerfile, src/mosquitto.conf
- **PrimeLauncher :** primeLauncher.py, build,sh, run.sh, Dockerfile

## Build & Run Containers
Every folders have three files in common.

- Dockerfile
- build.sh
- run.sh

### To Build
```bash
sudo chmod a+x build.sh # If the file is not yet executable
sudo ./build.sh
```

### To Run
```bash
sudo chmod a+x run.sh # If the file is not yet executable
sudo ./run.sh
```