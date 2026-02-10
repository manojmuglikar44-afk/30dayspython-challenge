numbers = [-4, "-3", "-2", "-1", 0, 2, 4, 6]
negative_or_zero = [int(num) for num in numbers if isinstance(num, (int, str)) and int(num) <= 0]
print(negative_or_zero)
---> [-4, -3, -2, -1, 0]
