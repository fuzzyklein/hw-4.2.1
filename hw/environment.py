from os import environ

class Environment(dict):
    def __init__(self, d={k:v for k,v in environ.items() if k[0].islower()}):
        super().__init__(d)
