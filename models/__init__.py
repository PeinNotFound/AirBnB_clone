#!/usr/bin/python3

'''it creates a unique file storage inst for the app'''

from AirBnB_clone.models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
