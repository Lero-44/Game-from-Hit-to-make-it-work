import re
from datetime import datetime
from collections import defaultdict
import plotly.express as px

#принимаем строку журнала в качестве входных данных и использует регулярное выражение re.match для извлечения временной метки
def parse_message(line):
    pattern = r'(\d{2}.\d{2}.\d{4} \d{2}:\d{2}) (\w+): (.+)'
    match = re.match(pattern, line)

    if match:
        timestamp_str, _, _ = match.groups()
        timestamp = datetime.strptime(timestamp_str, '%d.%m.%Y %H:%M')
        return timestamp.date()
    else:
        return None

#принимаеv словарь messages_per_day содержащий даты в качестве ключей и количество сообщений в качестве значений.
def plot_message_graph(messages_per_day):
    dates = list(messages_per_day.keys())
    message_counts = list(messages_per_day.values())

    fig = px.bar(x=dates, y=message_counts, labels={'x': 'Date', 'y': 'Number of Messages'}, title='Messages per Day')
    fig.update_xaxes(type='category')
    fig.show()

#Используем функцию parse_message для извлечения дат и подсчета количества сообщений в день
def analyze_messages(filename, author_name):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    messages_per_day = defaultdict(int)

    for line in lines:
        parsed_date = parse_message(line)
        if parsed_date:
            messages_per_day[parsed_date] += 1

    # Plot the graph for the specified author
    plot_message_graph(messages_per_day)

# Example usage
filename = 'hah.txt'  # Replace with your actual file name
author_name = 'John'   # Replace with the author's name you want to analyze
analyze_messages(filename, author_name)
