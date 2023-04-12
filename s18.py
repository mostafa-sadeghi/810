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
# sum_of_even_digits = 0
# sum_of_odd_digits = 0
# number = input('enter a number:> ')
# for n in number:
#     if int(n) % 2 == 0:
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


#   مجموع رقم های زوج و فرد یک عدد به صورت جداگانه

# n = int(input('enter a "number": '))
# sum_of_even_digits = 0
# sum_of_odd_digits = 0
# while n:
#     m = n % 10
#     if m % 2 == 0:
#         sum_of_even_digits += m  # sum_of_even_digits = sum_of_even_digits + m
#     else:
#         sum_of_odd_digits += m
#     n //= 10  # n = n // 10
# print("sum of even digits :", sum_of_even_digits)
# print("sum of odd digits :", sum_of_odd_digits)


#

'''
برنامه ای برای ثبت نام دانش آموزان مدرسه خود بنویسید
در این برنامه اطلاعات دانش آموز از ورودی دریافت می شود
و در قالب دیکشنری یک لیست اضافه می شود

برنامه امکان اضافه کردن
حذف کردن و ویرایش اطلاعات دانش آموزان را دارد
همینطور امکان نمایش لیست تمام اطلاعات دانش آموزان مدرسه را دارد
'''

all_students = []
while True:
    print('''Students registration software
    to add  student -> 1,
    to show all students -> 2,
    to delete a student -> 3
    to exit -> 0
    ''')
    user_selection = input('> ')
    if user_selection == '0':
        print("Thank you for joining us...")
        exit()
    elif user_selection == '1':
        student = {}
        name = input('enter student`s name: ')
        age = int(input('enter student`s age: '))
        student['name'] = name
        student['age']= age
        all_students.append(student)
        print(f'{name} added...')
        input('press enter to continue... ')

    elif user_selection == '2':
        print("all students", all_students)
        input('press enter to continue... ')
    elif user_selection == '3':
        print('delete ...')
        name = input('enter student`s name: ')
        for i in range(len(all_students)):
            if name == all_students[i]['name']:
                confirm = input(f'you are deleting {name}.Are you sure? (yes or no)')
                if confirm.lower().startswith('y'):
                    del all_students[i]
                    print(f'{name} was deleted...')
                    input('press enter to continue... ')
                    break
                else:
                    break






