# lst = []
# for i in range (1, 11):
#         lst.append(i)
# print(lst)

# ORR

# lst = [num for num in range(1, 11)]
# print(lst)


# lst = []
# for i in range(1, 11):
#     if i % 2 == 0 :
#         lst.append(i)
# print(lst)


# lst = [num for num in range(1, 11) if num % 2 == 0]
# print(lst)

#-----------------------------------------------------------------

# def checkEven(num):
#     if num % 2 == 0:
#         return"This is even" ---> data type (string data type)
#     else:
#         return("This is odd")
    
# even = 3
# print(checkEven(even))
# print(checkEven(89))

#------------------------------------------------------------------

# def checkEven(num):
#     if num % 2 == 0:
#         return num
#     else:
#         return num
    
# even = 4
# print(checkEven(even))

#------------------------------------------------------------------

# def converter(cels):
#     f = (cels * 1.8) + 32
#     return (f)
# inp = int(input("Please provide your degree : "))
# print (converter(inp) + 2 )

#exampl hw1.tas1 with #def

# def check_odd(num):
#     list = [1,2,3,4,5,6,7,8,9,10]
#     if i % 2 != 0:
#################TASK

# def oddList(par):
#     odd_lst = []
#     for i in par:
#         if i % 2 != 0:
#             odd_lst.append(i)
#     return odd_lst

# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# print(oddList(lst))

########################

# def checker(lst, char):
#     word_lst = []
#     for word in lst:
#         if char in word:
#             word_lst.append(word)
#     return word_lst

# print(checker(["banana","apple","cherry"], "a"))

##########################TASK1
#   -Create a function for addtition:
#   -Create a function for subtraction
#   -Create a function for multiplication
#   -Create a function for devision
#1
# def add(num1, num2):
#     return num1 + num2
# num1 = 10
# num2 = 10
# print(add(num1, num2))

###############################TASK2

# def ckeck(word, char):
#     return word, char
# val = "Hello"
# character = "e"
# print(ckeck(val, character))


#################################TASK3

# def check (word, char):
#     if char in word:
#         return "Inside"
#     else:
#         return "Outside"
    
# print(check("Hello", "e"))
# print(check("Table", "a"))
# print(check("Water", "r"))
#

#very powerfull topic, need repeat evrithing more times and NEED PRACTIS.
#READ TOPIC #8
#WHAT DIFFERENT BETWEEN ARGUMENT AND FUNCTIONS? and more ...
