#!/usr/bin/env python3


from base_model import BaseModel


class City(BaseModel):
    def __init__(self):
        self.state_id = ""
        self.name = ""
