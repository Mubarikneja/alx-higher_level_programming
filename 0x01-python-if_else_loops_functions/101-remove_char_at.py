#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for chara in range(0, len(str)):
        if chara != n:
            result = result + str[chara]
    return result
