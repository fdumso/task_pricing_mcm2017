# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Data structures
"""
import datetime

import pandas

__author__ = "freemso"

USERS_FILENAME = "data/users.xlsx"
OLD_TASKS_FILENAME = "data/old_tasks.xls"
NEW_TASKS_FILENAME = "data/new_tasks.xls"

TIME_FORMAT = "%H:%M:%S"


class Task(object):
    def __init__(self, id_, longitude, latitude, price, is_finished):
        self.id_ = id_
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.price = float(price) if price else None
        self.is_finished = bool(is_finished) if is_finished else None


class User(object):
    def __init__(self, id_, position, book_quantity_limit, book_start_time, credit):
        self.id_ = id_
        self.latitude = float(position.split()[0])
        self.longitude = float(position.split()[1])
        self.book_quantity_limit = int(book_quantity_limit)
        self.book_start_time = book_start_time
        self.credit = float(credit)


def load_data():
    # Load user data
    user_df = pandas.read_excel(USERS_FILENAME)
    users = [
        User(id_, position, book_quantity_limit, book_start_time, credit)
        for id_, position, book_quantity_limit, book_start_time, credit in zip(
            user_df["会员编号"], user_df["会员位置(GPS)"], user_df["预订任务限额"],
            user_df["预订任务开始时间"], user_df["信誉值"])
    ]
    # Load new tasks
    new_tasks_df = pandas.read_excel(NEW_TASKS_FILENAME)
    new_tasks = [
        Task(id_, longitude, latitude, None, None)
        for id_, latitude, longitude in zip(
            new_tasks_df["任务号码"], new_tasks_df["任务GPS纬度"], new_tasks_df["任务GPS经度"]
        )
    ]
    # Load old tasks
    old_tasks_df = pandas.read_excel(OLD_TASKS_FILENAME)
    old_tasks = [
        Task(id_, longitude, latitude, price, is_finished)
        for id_, latitude, longitude, price, is_finished in zip(
            old_tasks_df["任务号码"], old_tasks_df["任务gps 纬度"], old_tasks_df["任务gps经度"],
            old_tasks_df["任务标价"], old_tasks_df["任务执行情况"]
        )
    ]
    return users, new_tasks, old_tasks


if __name__ == '__main__':
    pass
