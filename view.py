# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    To view the distribution of data over geographic plane
"""
import folium
from folium import Icon, Popup

import dataset

__author__ = "freemso"

USER_MAP_FILENAME = "map_view/users.html"
NEW_TASKS_MAP_FILENAME = "map_view/new_tasks.html"
OLD_TASKS_MAP_FILENAME = "map_view/old_tasks.html"


if __name__ == '__main__':
    users, new_tasks, old_tasks = dataset.load_data()
    max_lon = max([t.longitude for t in old_tasks])
    min_lon = min([t.longitude for t in old_tasks])
    max_lat = max([t.latitude for t in old_tasks])
    min_lat = min([t.latitude for t in old_tasks])

    geo_map = folium.Map(
        location=[23, 113.5],
        zoom_start=9
    )
    for t in old_tasks:
        icon = Icon(
            color="green" if t.is_finished else "red",
            prefix="fa",
            icon="circle"
        )
        popup = Popup(
            html="P: ({},{})<br>"
                 "$: {}".format(
                t.latitude,
                t.longitude,
                t.price
            ))
        folium.Marker(
            location=[t.latitude, t.longitude],
            icon=icon,
            popup=popup
        ).add_to(geo_map)
    # for t in new_tasks:
    #     icon = Icon(
    #         icon_color="gray",
    #         prefix="fa",
    #         icon="circle"
    #     )
    #     folium.Marker(
    #         location=[t.latitude, t.longitude],
    #         icon=icon
    #     ).add_to(geo_map)
    for u in users:
        if min_lat < u.latitude < max_lat and min_lon < u.longitude < max_lon:
            icon = Icon(
                color="blue",
                prefix="fa",
                icon="user"
            )
            popup = Popup(
                html="P: ({},{})<br>"
                     "C: {}<br>"
                     "T: {}<br>"
                     "Q: {}".format(
                        u.latitude,
                        u.longitude,
                        u.credit,
                        u.book_start_time,
                        u.book_quantity_limit
                    ))
            folium.Marker(
                location=[u.latitude, u.longitude],
                icon=icon,
                popup=popup
            ).add_to(geo_map)

    geo_map.save(OLD_TASKS_MAP_FILENAME)

