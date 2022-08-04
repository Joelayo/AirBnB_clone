#!/usr/bin/env python3


from base_model import BaseModel


class Place(BaseModel):
    def __init__(self):
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = ""
        self.number_bathrooms = ""
        self.max_guest = ""
        self.price_by_night = ""
        self.latitude = ""
        self.longitude = ""
        self.amenity_ids = ""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
