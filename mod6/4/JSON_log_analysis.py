import json
import itertools
import operator
import datetime
from collections import Counter

with open("log.txt", 'r', encoding="UTF-8") as file:
    logs = [json.loads(log) for log in file.readlines()]



def print_levels_occurrences():
    level_logs = logs
    level_logs.sort(key=lambda x: x['level'])
    for level , occurrences in itertools.groupby(level_logs, key=lambda x: x['level']):
        print(f'{level}:{len(list(occurrences))}')


def print_max_logs_hour():
    hour_dict = {}
    hour_logs = logs
    hour_logs.sort(key=lambda x: x['time'])
    for hour, occurrences in itertools.groupby(hour_logs, key=lambda x: x['time']):
        hour_dict[hour] = len(list(occurrences))
    print(f"MAX logs was in {max(hour_dict.items(), key=operator.itemgetter(1))[0]}")

def print_occur_in_time(level:str, time_start:str, time_stop:str):
    hour_dict = {}
    hour_logs = logs
    hour_logs.sort(key=lambda x: x['time'])
    for hour, occurrences in itertools.groupby(hour_logs, key=lambda x: x['time']):
        hour_dict[hour] = len(list(occurrences))
    result = 0
    for time in hour_dict.keys():
        if (datetime.datetime.strptime(time_stop, "%H:%M:%S") >= datetime.datetime.strptime(time, "%H:%M:%S")
                >= datetime.datetime.strptime(time_start, "%H:%M:%S")):
            result += hour_dict[time]
    print(f"Logs {level} from {time_start} to {time_stop} was {result}")


def print_word_occur(word:str):
    occur = 0
    word_logs = logs
    word_logs.sort(key=lambda x: x['message'])
    for message, occurrences in itertools.groupby(word_logs, key=lambda x: x['message']):
        if word in message:
            occur = len(list(occurrences))
    print(f'Word "{word}" was in {occur} messages')

def print_most_frequent_word_in_level(level:str):
    log_level = [log for log in logs if log["level"] == level]
    words = [log['message'].split() for log in log_level]
    counter = Counter([i for sublist in words for i in sublist]).most_common()[0]
    print(f"Most common word for level '{level}' is '{counter[0]}'")


if __name__ == "__main__":
    print_levels_occurrences()
    print("______________________________________________________")
    print_max_logs_hour()
    print("______________________________________________________")
    print_occur_in_time("INFO","20:25:02", "20:25:05")
    print("______________________________________________________")
    print_word_occur("Пользователь")
    print("______________________________________________________")
    print_most_frequent_word_in_level("INFO")
