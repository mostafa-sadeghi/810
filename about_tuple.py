my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[:4])
print(my_tuple[::2])
print(my_tuple[1::2])


# تاپل قابل تغییر نیست

# my_tuple[0] = 12  # error

# my_tuple.append(12)  # error

# نوع داده رشته هم غیرقابل تغییر است
# string = 'abc'

# string[0] = 'd'


numers1 = (1, 2, 3, 4)
numers2 = (5, 6, 7, 8, 9)

numbers = numers1 + numers2
print(numbers)
numbers = numers1 * 10
print(numbers)
