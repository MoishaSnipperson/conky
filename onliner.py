#!/usr/bin/python
# -*- coding: utf-8 -*-


import my_libs
from bs4 import BeautifulSoup
import os.path
import datetime

if __name__ == "__main__":
    #Имя сохраняемого файла
    FILE_NAME = "onliner.html"

    # Если файла есть
    if os.path.exists(FILE_NAME):

        # Если время создание больше чем 
        if my_libs.change_file(FILE_NAME, 120):
            page = my_libs.download_page("https://kurs.onliner.by")
            soup = BeautifulSoup(page.text, 'lxml')
            my_libs.write_file(FILE_NAME, page.text) 
        else:
            page = my_libs.read_file(FILE_NAME)
            soup = BeautifulSoup(page, 'lxml')   
        
    #Если файла нет
    else:
        page = my_libs.download_page("https://kurs.onliner.by")
        soup = BeautifulSoup(page.text, 'lxml')
        my_libs.write_file(FILE_NAME, page.text)
        
     

coins = []
bank_poks = []
bank_prods = []
table = soup.find_all("table", class_ = "b-currency-table__best")
#================================================================
for x in table:
    coin = x.find("p", class_="abbr rate")
    if coin:
        coins.append(coin)

    bank_pok = x.find('p', class_="value")
    if bank_pok:
        bank_poks.append(bank_pok)

        bank_pro = x.find('p', class_="value").find_next('p', class_="value")
        if bank_pro:
            bank_prods.append(bank_pro)
#================================================================

#Выводим все в цвете
for x in range(0, 3):
    print("${color yellow}" + coins[x].text, "${color green}" + bank_poks[x].text, "${color blue}" + bank_prods[x].text, "${color silver}" + my_libs.get_file_time("onliner.html"))
