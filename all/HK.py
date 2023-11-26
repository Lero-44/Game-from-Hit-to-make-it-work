import re
from datetime import datetime
from collections import defaultdict

# Берем строку из журнала и будем исползовать выражение re.match для извлечения информации
def parse_message(line):
    # pattern используется для сопостовления строк такие как (Время (\d{2}.\d{2}.\d{4} \d{2}:\d{2}); Имя(\w+); Содержание сообщения(.+))
    pattern = r'(\d{2}.\d{2}.\d{4} \d{2}:\d{2}) (\w+): (.+)'
    match = re.match(pattern, line)

    if match:
        timestamp_str, author, content = match.groups()
        timestamp = datetime.strptime(timestamp_str, '%d.%m.%Y %H:%M')
        return timestamp, author, content
    else:
        return None

# проверяем попадает ли время сообщение в диапозон от 20:00 до 7:00
def is_time_between(start_time, end_time, current_time):
    if start_time <= end_time:
        return start_time <= current_time <= end_time
    else:
        return start_time <= current_time or current_time <= end_time

#Считывает содержимое файла
def analyze_messages(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    messages_per_day = defaultdict(int)

    #используем parse_message чтобы извлечь информацию
    for line in lines:
        parsed_data = parse_message(line)
        if parsed_data:
            timestamp, author, _ = parsed_data
            #Увеличиваем количество сообщений в день для кажого человека который есть в чате
            day_key = timestamp.date()
            messages_per_day[(author, day_key)] += 1

            #Проверка сообщения когда оно было отпралвено
            if is_time_between(datetime.strptime('20:00', '%H:%M').time(),
                               datetime.strptime('07:00', '%H:%M').time(),
                               timestamp.time()):
                print(f"{author} написал(а) сообщение в {timestamp}.")

    #Проверка написали ли люди больше 2 сообщений
    for author, count in messages_per_day.items():
        if count > 2:
            print(f"{author[0]} написал(а) {count} сообщение(ий) в {author[1]}.")

filename = 'hah.txt'
analyze_messages(filename)
