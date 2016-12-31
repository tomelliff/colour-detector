#!/usr/bin/env python
'''
Command line script for retrieving all stored RGB values in the database.
'''
import data_storage

ds = data_storage.DataStorage()
print(ds.get_all_rgb_values())
