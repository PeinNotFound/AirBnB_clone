#!/usr/bin/python3
'''Module for the City class.'''
from AirBnB_clone.models.base_model import BaseModel

class City(BaseModel):
    '''
    Represent a city.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    '''
    state_id = ""
    name = ""
