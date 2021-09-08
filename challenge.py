# 2021.09.07

# nodejs = var():
# python = def():


# a = 3
# b = 3
# c = a+b
# print(c)

# a_string = "like"
# a_number = 3
# a_float = 3.12
# a_boolean = False
# a_none = None

# print(a_number+a_float)



# days = ["M","T","W","T","F"]
# # days.append("S")
# # days.reverse()
# if "M" in days:
#     print(True)
# print(days)
# print(days[0])


# days = ("M","T","W","T","F")
# print(type(days))




# dictionary
# kimo = {
#     "age" : 26,
#     "korean" : True,
#     "lol" : "gold"
# }
# print(kimo["age"])



# def say_hello():
#     print("hello")
#     print("bye")

# say_hello


# a = input(int())
# b = input(int())
# def plus(a,b):
#     print("a+b=",int(a)+int(b))

# plus(a,b)


# def say_hello():
#     print("king")

# say_hello()

# days = ["m","t","w","t","f"]
# if "a" not in days:
#     print("누워~~~~ ●▅▇█▇▆▅▄▇")


# def p_plus(a,b):
#     print(a+b)


# def r_plus(a,b):
#     return a+b
    
# p_result = p_plus(6,3)
# r_result = r_plus(6,3)

# print(p_result,r_result)




# def plus(a,b):
#     return a+b

# result = plus(6,4)
# print(result)



# def plus(a,b):
#     return a+b

# result = plus(a= 50,b=25)
# print(result)


# 입력받은 값을 계산하기
# a = input("a = ")
# b = input("b = ")
# def plus():
#     return int(a)+int(b)
# print(plus())   




# # # 2021-09-07 챌린지 1
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# def is_on_list():
#   print("Is Wed on 'days' list?", "Wed" in days )
# is_on_list()

# def get_x():
#   print("The fourth item in 'days' is:", days[3])
# get_x()

# def add_x():
#   days.append("Sat")
#   print(days)
# add_x()

# def remove_x():
#   days.remove("Mon")
#   print(days)
# remove_x()


# # 정답
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# def is_on_list(a_list=[], word=""):
#     return word in a_list

# def get_x(a_list=[], index=0):
#     return a_list[index]

# def add_x(a_list=[], word=""):
#     a_list.append(word)

# def remove_x(a_list=[], word=""):
#     a_list.remove(word)


# print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

# print("The fourth item in 'days' is:", get_x(days, 3))

# add_x(days, "Sat")
# print(days)

# remove_x(days, "Sat")
# print(days)




# 2021-09-08 챌린지 2

# # 조건문
# def plus(a,b):
#     if type(b) is int or type(b) is float:
#         return a + b
#     else: 
#         return None
# print(plus(12, 1))




# # 나이 계산하기 if, elif, else
# age = int(input())

# def age_check(age):
#     print(f"you are {age}")
#     if age < 18:
#         print("you can't drink")
#     elif age == 18 or age == 19:
#         print("you are highschool student nope")    # 위와 아래를 바꾸면 위에서 아래부터 인식한다.
#     elif age == 18:    
#         print("also you can't")
#     elif age > 20 and age < 25:
#         print("you are still young")
#     else:
#         print("you can!!")

# age_check(age)



# 2021-09-08 챌린지 2 문제

def add_to_dict(a,b="",c=None):
    if type(a) == dict:
        if type(b) != str or type(c) != str:
            print("You need to send a word and a definition.")
        elif b in a:
            print("kimchi is already on the dictionary. Won't add.")
        elif type(b) == str and type(c) == str:
            my_english_dict[b]=c
            print("kimchi has been added")
    else: print("You need to send a dictionary. You sent:",type(a))

def get_from_dict(dictionary={}, word=""):
    if type(dictionary) != dict:
        print(f"You need to send a dictionary. You sent: {type(dictionary)}")
    elif not word:
        print("You need to send a word to search for.")	 
    elif not word in dictionary:
        print(f"{word} was not found in this dict.")
    else:
        print(f"{word}: {dictionary[word]}")

def update_word(dictionary = {}, word ="", key=""):
    if type(dictionary) != dict:
        print(f"you need to send a dictionary. You sent: {type(dictionary)}")
    elif word in dictionary:
        dictionary[word]=key
        print(f"{word} has been updated to: {key}")
    elif not word or not key:
        print("You need to send a word word and a definition to update")

def delete_from_dict(dictionary = {}, word = ""):
    if type(dictionary) != dict:
        print(f"You need to send a dictionary. You sent: {type(dictionary)}")
    elif not word:
        print("You need to specify a word to delete")
    elif not word in dictionary:
        print(f"{word} is not in this dict. Wont't delete")
    else:
        del dictionary[word]
        print(f"{word} has been deleted.")
# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

# import os

# os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello","kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")