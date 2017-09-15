# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    To view the distribution of data over geographic plane
"""
import folium

import dataset

__author__ = "freemso"

USER_MAP_FILENAME = "map_view/users.html"
NEW_TASKS_MAP_FILENAME = "map_view/new_tasks.html"
OLD_TASKS_MAP_FILENAME = "map_view/old_tasks.html"


def map_it(objects, filename):
    assert all("latitude" in dir(o) and "longitude" in dir(o) for o in objects)
    lat_lon = [
        (o.latitude, o.longitude) for o in objects
    ]
    geo_map = folium.Map()
    for coord in lat_lon:
        folium.Marker(location=[coord[0], coord[1]]).add_to(geo_map)
    geo_map.save(filename)


if __name__ == '__main__':
    users, new_tasks, old_tasks = dataset.load_data()
    map_it(users, USER_MAP_FILENAME)
    map_it(new_tasks, NEW_TASKS_MAP_FILENAME)
    map_it(old_tasks, OLD_TASKS_MAP_FILENAME)

