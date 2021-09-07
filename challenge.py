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





days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
def is_on_list():
  print("Is Wed on 'days' list?", "Wed" in days )
is_on_list()

def get_x():
  print("The fourth item in 'days' is:", days[3])
get_x()

def add_x():
  days.append("Sat")
  print(days)
add_x()

def remove_x():
  days.remove("Mon")
  print(days)
remove_x()


