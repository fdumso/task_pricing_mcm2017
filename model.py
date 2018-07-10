# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Binary classification model
"""
from math import acos, sin, cos
from sklearn.metrics import pairwise_distances

import dataset

__author__ = "freemso"


def sphere_dist(a, b):
    return acos(sin(a[0]) * sin(b[0]) + cos(a[0]) * cos(b[0]) * cos(a[1] - b[1]))


def dist_matrix(X, Y=None, metric="euclidean"):
    if metric == "sphere":
        metric = sphere_dist
    return pairwise_distances(X, Y, metric=metric, n_jobs=4)


def get_near_points(matrix, top_k=10):
    return [
        [idx for idx, _ in sorted(enumerate(row), key=lambda r: r[1])[:top_k]]
        for row in matrix
    ]


def get_x(dist_metric="sphere", user_top_k=10, task_top_k=10):
    users, new_tasks, old_tasks = dataset.load_data()
    max_lon_old = max([t.longitude for t in old_tasks])
    min_lon_old = min([t.longitude for t in old_tasks])
    max_lat_old = max([t.latitude for t in old_tasks])
    min_lat_old = min([t.latitude for t in old_tasks])

    max_lon_new = max([t.longitude for t in new_tasks])
    min_lon_new = min([t.longitude for t in new_tasks])
    max_lat_new = max([t.latitude for t in new_tasks])
    min_lat_new = min([t.latitude for t in new_tasks])

    max_lon, min_lon = max(max_lon_old, max_lon_new) + 0.5, min(min_lon_old, min_lon_new) - 0.5
    max_lat, min_lat = max(max_lat_old, max_lat_new) + 0.5, min(min_lat_old, min_lat_new) - 0.5

    # Since almost all tasks are in Guangdong Province,
    # users in other area are not considered
    users = [user for user in users if min_lat < user.latitude < max_lat and min_lon < user.longitude < max_lon]

    lon_range = max_lon - min_lon
    lat_range = max_lat - min_lat

    # Distance Matrix
    old_task_user_dist_matrix = dist_matrix(
        X=[(t.latitude, t.longitude) for t in old_tasks],
        Y=[(u.latitude, u.longitude) for u in users],
        metric=dist_metric
    )
    old_tasks_dist_matrix = dist_matrix(
        X=[(t.latitude, t.longitude) for t in old_tasks],
        metric=dist_metric
    )

    # Absolute position feature
    old_tasks_ap_norm = [
        ((t.latitude - min_lat) / lat_range, (t.longitude - min_lon) / lon_range)
        for t in old_tasks
    ]
    new_tasks_ap_norm = [
        ((t.latitude - min_lat) / lat_range, (t.longitude - min_lon) / lon_range)
        for t in new_tasks
    ]
    users_ap_norm = [
        ((u.latitude - min_lat) / lat_range, (u.longitude - min_lon) / lon_range)
        for u in users
    ]

    # Relative position
    top_k_users = get_near_points(old_task_user_dist_matrix, top_k=user_top_k)
    top_k_tasks = get_near_points(old_tasks_dist_matrix, top_k=task_top_k)








    # Relative position feature
    pass


if __name__ == '__main__':
    pass
