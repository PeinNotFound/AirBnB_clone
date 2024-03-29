#!/usr/bin/python3
'''Module for the Review class.'''

from AirBnB_clone.models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
