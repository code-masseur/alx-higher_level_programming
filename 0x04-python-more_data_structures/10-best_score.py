#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        score = 0
        best_key = None
        for key in a_dictionary.keys():
            if score == 0 or a_dictionary[key] > score:
                score = a_dictionary[key]
                best_key = key
        return best_key
