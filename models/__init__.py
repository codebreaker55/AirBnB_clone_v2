#!/usr/bin/python3
"""This module instantiates an object of class FileStorage,
for the application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
