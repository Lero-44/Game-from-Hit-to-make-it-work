import re
from datetime import datetime
import datetime
from collections import defaultdict
import calendar
import matplotlib.pyplot as plt
from collections import Counter

def graph(filename, year, month):
    n_list = [] # тут должен быть массив с количеством сообщений некотороко сотрудника за каждый день месяца
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        messages_per_day = defaultdict(int)

    #алгоритм, который подсчитывает, сколько сообщений написал каждый пользователь
    name_list = list()
    for line in lines:
        all_elem = line.split()
        for n_elem in range(0, len(all_elem)-1):
            if n_elem == 2:
                name_list.append(all_elem[n_elem])


    name_cnt = Counter(name_list)
    employee = []        
    for value in name_cnt:
        n_list.append(name_cnt[value])
        employee.append(value)
   
   
    fig1, ax1 = plt.subplots()   
    ax1.pie(n_list, labels = employee, autopct='%1.1f%%',   
        shadow=True, startangle=90)   
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.   
   
    plt.show() 


graph('hah.txt', 2023, 1)

