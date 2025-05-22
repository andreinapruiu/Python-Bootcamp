my_list = ['cat', 'catatatatctsa', 'abcdefghijklmnop', '124259239185125', '', 'foo', 'unique']

most_unique = max(my_list, key=lambda s: len(set(s)))
print("String with most unique characters:", most_unique)
