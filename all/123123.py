import re
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

#принимаем строку long в качестве входных данных и используем для извечения данных
def parse_message(line):
    pattern = r'(\d{2}.\d{2}.\d{4} \d{2}:\d{2}) (\w+): (.+)'
    match = re.match(pattern, line)

    if match:
        timestamp_str, author, content = match.groups()
        timestamp = datetime.strptime(timestamp_str, '%d.%m.%Y %H:%M')
        return timestamp, author, content
    else:
        return None
#Проверяем, находится ли заданное время current_time между началом и окончанием
def is_time_between(start_time, end_time, current_time):
    if start_time <= end_time:
        return start_time <= current_time <= end_time
    else:
        return start_time <= current_time or current_time <= end_time

#Используеv функцию parse_message для извлечения информации из каждой строки и в случае успеха увеличивает количество сообщений за этот день и автора
def analyze_messages(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    messages_per_day = defaultdict(int)

    for line in lines:
        parsed_data = parse_message(line)
        if parsed_data:
            timestamp, author, _ = parsed_data
            day_key = timestamp.date()
            messages_per_day[(author, day_key)] += 1
    # Заполняем списки x и y
    x = []
    y = []
    for (author, day_key), count in messages_per_day.items():
        x.append(day_key)
        y.append(count)
    #Устанавливаем метки оси, заголовок и настраивает макет
    fig, ax = plt.subplots()
    ax.bar(x, y, align='center')
    ax.xaxis_date()
    date_format = DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(date_format)
    plt.xlabel('Date')
    plt.ylabel('Number of Messages')
    plt.title('Number of Messages per Day')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

filename = 'hah.txt'
analyze_messages(filename)
