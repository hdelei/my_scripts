from os import path
from time import sleep
import json


class Input():

    def __init__(self):
        self.new_input = False
        self.file = 'input.json'
        self.creation_time = path.getmtime(self.file)
        self.event = 0
        self.BEEP_MUTE = 4

    def watch_file(self):
        mod_time = path.getmtime(self.file)
        if mod_time != self.creation_time:
            sleep(1)
            self.read_input()
            self.creation_time = mod_time
            return self.event
        else:
            self.event = 0
            return self.event

    def read_input(self):
        with open('input.json') as jsonfile:
            data = json.load(jsonfile)
            self.event = data['event']
