# favorite_sports = {}
# print(type(favorite_sports))

# favorite_sports = {
#     'sepehr': 'football',
#     'pendar': 'basketball',
#     'nika': 'tennis',
#     'iliya': 'football',
#     'atay': 'pingpong',

# }
# print(favorite_sports['iliya'])
# print(favorite_sports['sepehr'])
# print(favorite_sports['atay'])


# print(favorite_sports.items())
# print(favorite_sports.keys())
# print(favorite_sports.values())

# favorite_sports = {
#     'sepehr': 'football',
#     'pendar': 'basketball',
#     'nika': 'tennis',
#     'iliya': 'football',
#     'atay': 'pingpong',
#     'some one': "some thing"

# }

# favorite_sports['nima'] = "football"

# print("after adding ...", favorite_sports)


# del favorite_sports['some one']

# print("after removing", favorite_sports)

#   برنامه ای بنویسید که نام و ورزش مورد علاقه 4 نفرا را از ورودی بگیرد و در یک دیکشنری ذخیره نماید
# نفر سوم را از دیکشنری حذف نمایید
# یک نفر جدید به دیکشنری اضافه کنید


# برنامه ای بنویسید که نام و سن 4 دانش آموز  را از وزودی دریافت نماید و در یک دیکشنری ذخیره نماید
# مجموع سن دانش آموزان را از داخل دیکشنری حساب نماید.


students = {}
name1 = input("enter first studen's name: ")
age1 = float(input("enter first studen's age: "))
name2 = input("enter second studen's name: ")
age2 = float(input("enter second studen's age: "))

students[name1] = age1
students[name2] = age2

print("our student dictionary: ", students)
ages_sum = students[name1] + students[name2]
print(f"sum of two student's age is {ages_sum}")
