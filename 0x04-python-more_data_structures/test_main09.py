#!/usr/bin/python3

multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary
best_score = __import__('10-best_score').best_score

a_dictionary = {'Andy': 24, 'Jenny': 45, 'Jude': 34, 'Mich': 22, 'Martin': 32}

new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
print("--")
print("--")

best_key = best_score(a_dictionary)
print("Best score is: {}".format(best_key))