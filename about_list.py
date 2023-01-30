# shopping_list = ['apple', 'banana', 'milk', 'potato']
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])
# print(shopping_list[4]) # error


# list1 = [1, 'a', [1, 2], 'ali']
# print(list1)
# print(list1[2])
# print(list1[2][0])
# print(list1[2][1])
shopping_list = ['apple', 'banana', 'milk', 'potato']
# اضافه کردن به لیست
shopping_list.append('tomato')
shopping_list.append('onion')
print(shopping_list)

# remove from list
del shopping_list[0]
print(shopping_list)

shopping_list.remove('milk')
print(shopping_list)
