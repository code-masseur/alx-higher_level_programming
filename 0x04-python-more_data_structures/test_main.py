#!/usr/bin/python3

update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary
simple_delete = __import__('8-simple_delete').simple_delete
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)

print("--")

print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
print("--")
print("--")
new_dict = update_dictionary(a_dictionary, 'name', "Jude")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
new_dict = update_dictionary(a_dictionary, 'name', "Onyiagu")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")

new_dict = simple_delete(a_dictionary, 'number')
print_sorted_dictionary(new_dict)
print("--")

print_sorted_dictionary(a_dictionary)





