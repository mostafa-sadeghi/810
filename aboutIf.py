# a = 4
# b = 5
# if a < b:
#     print("a is lower than b.")
# if a > b:
#     print("a is greater than b.")
# a = 4
# b = 4
# if a <= b:
#     print("a is lower than or equal to b.")
# if a > b:
#     print("a is greater than b.")
# a = 4
# b = 4
# if a == b:
#     print("a is is equal to b.")
# a = 4
# b = 5
# if a != b:
#     print("a is is not equal to b.")
# if not a == b:
#     print("a is is not equal to b.")

# exercise1:
# برنامه ای بنویسید که سه عدد را از ورودی دریافت نماید
# در صورتی که عدد اول از دو عدد دیگر بزرگتر باشد
# a is greater than b,c
# در صورتی که عدد اول از دو عدد دیگر کوچکتر باشد:
# a is lower than b,c
# در صورتی که عدد اول از عدد دوم بزرگتر ولی از عدد سوم کوچکتر باشد:
# a is greater tha nb but is lower than c
# را نمایش دهد.

# a = 5
# b = 8

# if a == 5 and b == 7:
#     print("ok")

# if a == 5 or b == 7:
#     print("ok")


# a = True
# if a:
#     print("to do some thing.")
# if not a:
#     print("not do some thing.")


# a = True
# b = False
# if a and b:
#     print("a and b are both true")


# a = 3
# b = 3
# c = a == b
# print(c)


# if 1:
#     print("ok")

# if 0:
#     print("zero")

# if -2:
#     print("-2")

# if "":
#     print("hello")

# if "a":
#     print("a")

# if " ":
#     print("hello")

# exit() if or
# تازمانیکه کاربر کلمه زیر را وارد نکرد ازش یه کلمه دیگه بپرسه
# exit   Exit   EXIT

# for s in "nima":
#     print(s)
# for i in range(len("nima")):
#     print("nima"[i])
# i = 0
# while i < len("nima"):
#     print("nima"[i])
#     i = i + 1
# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     print(n)
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

'''
    *
   * *
  * * *
 * * * *
* * * * *

'''
print(' ' * 4 + '* '*1)
print(' ' * 3 + '* '*2)
print(' ' * 2 + '* '*3)
print(' ' * 1 + '* '*4)
print(' ' * 0 + '* '*5)

for i in range(5):
    print(' ' * (4-i) + '* '*(i+1))
