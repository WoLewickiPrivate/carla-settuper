import glob
import os
import sys
import time
import random

try:
    sys.path.append(glob.glob('./PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
import numpy as np
import subprocess
import psutil
import argparse

import manual_control

class Env():

    def __init__(self, args):
        self.build_carla(args.width, args.height, args.town, args.host, args.port)
        for _ in range(int(args.actors)):
            self.spawn_actor(args.model)
        while True:
            time.sleep(10)

    def build_carla(self, resX, resY, town_number, host, port):
        self.client = carla.Client(host, port)
        self.client.set_timeout(10.0)
        self.actor_list = []
        self.client.load_world('Town0' + town_number)
        self.world = self.client.get_world()
        self.blueprint_library = self.world.get_blueprint_library()
        self.resX = resX
        self.resY = resY

    def spawn_actor(self, car_model):
        while True:
            try:
                vehicle = self.world.try_spawn_actor(self.blueprint_library.filter('vehicle')[int(car_model)], random.choice(self.world.get_map().get_spawn_points()))
                self.actor_list.append(vehicle)
                vehicle.set_autopilot(True)
                print('created %s' % vehicle.type_id)
                break
            except:
                time.sleep(0.01)

    def destroy_actors(self):
        print('destroying actors')
        self.client.apply_batch([carla.command.DestroyActor(x) for x in self.actor_list])


def main():
    argparser = argparse.ArgumentParser(
        description='CARLA Basic Usage')
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    argparser.add_argument(
        '--res',
        metavar='WIDTHxHEIGHT',
        default='1280x720',
        help='window resolution (default: 1280x720)')
    argparser.add_argument(
        '--town',
        metavar='T',
        default='1',
        help="number of the map. Options are: '1', '2', '3'.")
    argparser.add_argument(
        '--manual',
        metavar='M',
        default=0,
        type=int,
        help="Should the player take control over the vehicle. `0` for `true`, `false` otherwise. If you choose this option, the next ones don't change anything. It uses the configuration provided by Carla's package.")
    argparser.add_argument(
        '--model',
        metavar='M',
        default='3',
        help="car model. '0' for Chevy Impala, '1' for Mercedes ccc, '2' for Audi A2, '3' for Nissan Micra.")
    argparser.add_argument(
        '--actors',
        metavar='A',
        default=5,
        type=int,
        help='number of actors to be spawned')
    args = argparser.parse_args()
        
    args.width, args.height = [int(x) for x in args.res.split('x')]


    if args.manual == 0:
        manual_control.main()
    else:
        game = None
        try:
            game = Env(args)
        except KeyboardInterrupt:
            print('\n Ending simulation')
        finally:
            if game is not None:
                game.destroy_actors()

if __name__ == '__main__':
   main()