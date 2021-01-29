# Carla environment setupper

The aim of this project is to provide scripts that setup the environment for working with Carla AV simulator. It gives the developer an easy way to start and customize the environment to make its basic internals ready for e.g. developing your game or running ML operations.

## Requirements

All of the requirements are provided in `requirements.txt` file.

## Running the script

Firstly, make sure the scripts are added to the main folder of Carla (the one with `CarlaUE4.exe`). Then run the first script:

```python
python .\start_carla.py
```

You will be asked to provide the quality of the Carla environment. Choose the correct one based on your hardware and needs.

Next, run the second script:

```python
python .\setup_env.py
```

This script provides a variety of options for the user.

## Script API definition

## --host

IP of the host server. Defaults to `'127.0.0.1'`.

## --port

TCP port to listen to. Defaults to `2000`.

## --res

Window resolution. Defaults to `1280x720`.

## --town

Number of the map provided to the environment. Defaults to `1`.

## --model

Model of the simulation cars should aquire. '0' for Chevy Impala, '1' for Mercedes ccc, '2' for Audi A2, '3' for Nissan Micra. Defaults to `3`.
       
## --actors

Number of actors to be spawned. Defaults to `3`.