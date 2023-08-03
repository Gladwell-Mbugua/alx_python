def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Test
my_dict = {'name': 'John', 'age': 25}
update_dictionary(my_dict, 'name', 'Alice')
update_dictionary(my_dict, 'city', 'New York')

print(my_dict)
