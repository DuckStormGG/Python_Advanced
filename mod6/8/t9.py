import re

numbers_to_char = {2:['a','b','c'],
                   3:['d','e','f'],
                   4:['g','h','i'],
                   5:['j','k','l'],
                   6:['m','n','o'],
                   7:['p','q','r','s'],
                   8:['t','u','v'],
                   9:['w','x','y','z']}



with open("words.txt", "r") as file:
    words = file.read()


def my_t9(numbers_string:str):
    numbers_list = list(map(int,numbers_string))
    pattern = ""
    for number in numbers_list:
        pattern += f"[{numbers_to_char[number][0]}-{numbers_to_char[number][-1]}]"
    print(set(re.findall(pattern, words)))


my_t9("22736368")