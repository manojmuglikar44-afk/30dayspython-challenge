num = [-4, "-3", "-2", "-1", 0, 2, 4, 6]
negative_or_zero = [int(num) for num in numbers if isinstance(num, (int, str)) and int(num) <= 0]
print(negative_or_zero)
---> [-4, -3, -2, -1, 0]

lst_of_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in lst_of_lst for item in sublist]
print(flattened)
---> [1, 2, 3, 4, 5, 6, 7, 8, 9]


