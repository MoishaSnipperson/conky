#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import time


#Функция скачивания страницы с фэйковыми заголовками
def download_page(URL):
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"none",
        "Sec-Fetch-User":"?1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent": agent,
        "X-Amzn-Trace-Id":"Root=1-6356ee8b-52c0c6bf23113a8b79fc81b1"
        }
    try:
        page = requests.get(URL, headers=headers)
    except requests.ConnectionError:
        return "None"
    else:    
        return page

#Функция проверки устаревания файла
def change_file(file_name, time_change):

    file_time = os.path.getmtime(file_name) + time_change
    if int(file_time) < int(time.time()):
        return True
    else:
        return False


#Функция записи файла
def write_file(file_path, data_file):
    with open(file_path, "w") as file:
        file.write(data_file)



#Функция чтения файла
def read_file(file_path):
    file = open(file_path,'r')
    try:
        return file.read()
    finally:
        file.close() 


#Функция получение даты и времени создания файла
def get_file_time(file_name):
    file_time = os.path.getmtime(file_name)
    m_ti = time.ctime(file_time)
    t_obj = time.strptime(m_ti)
    T_stamp = time.strftime("%H:%M:%S", t_obj)
    return T_stamp
