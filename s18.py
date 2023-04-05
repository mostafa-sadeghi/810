# for i in range(5):
#     print("I want to learn pygame.")
#     print("I want to program great games with python")
#     print("I want to create a website with python")

# print("ok")

# for i in range(10):
#     print(i)

# for i in range(1,11):
#     print(i)

# for i in range(1,11):
#     print(i, end=' ')

# for i in range(10):
#     print(i+1, end=' ')

# print("even numbers are: ", end=' ')
# for i in range(2,11,2):
#     print(i, end=' ')

# print()

# for i in range(5):
#     print((i + 1) * 2, end=' ')

# print()
# print("odd numbers are: ", end=' ')
# for i in range(1,11,2):
#     print(i, end=' ')

# numbers from 10 to 1
# for i in range(10, 0, -1):
#     print(i, end=' ')

# for i in [2, 6, 4, 2, 4, 6, 7, 4]:
#     print(i, end=' ')
# print()
# for i in (2, 6, 4, 2, 4, 6, 7, 4):
#     print(i, end=' ')
# print()
# for i in '2357890':
#     print(i, end=' ')
# exercise:
# یک برنامه بنویسید که یک عدد پنج رقمی را از ورودی دریافت نماید و مجموع ارقام آن را محاسبه و نمایش دهد.
# یک برنامه بنویسید که یک عدد پنج رقمی را از ورودی دریافت نماید و مجموع ارقام زوج آن را محاسبه و نمایش دهد.
# یک برنامه بنویسید که یک عدد پنج رقمی را از ورودی دریافت نماید و مجموع ارقام فرد آن را محاسبه و نمایش دهد.

# result = 0
# number = input('enter a number:> ')
# for n in number:
#     result += int(n) # result = result + int(n)

# print(result)
sum_of_even_digits = 0
sum_of_odd_digits = 0
number = input('enter a number:> ')
for n in number:
    if int(n) % 2 == 0:
        # sum_of_even_digits = sum_of_even_digits + int(n)
#         sum_of_even_digits += int(n)
#     else:
#         sum_of_odd_digits += int(n)

# print("sum of even numbers :", sum_of_even_digits)
# print("sum of odd numbers :", sum_of_odd_digits)


# exercise 1:
# draw flowchart and write the python code of this alorithm:
# 1. take n from input
# 2. m = n % 10
# 3. print m
# 4. n = n // 10
# 5 . if   n!= 0 goto step 2, else: goto step 6
# 6. end
