#print(0o507)
#print(hex(12345630))


# for word in range(10):
#     print("Hello", word)

# jan24_names = [
#              "Aiperi",
#              "Khusraf",
#              "Fatima", 
#             "Yrys", 
#              "Myroslav", 
#              "Dastan",
#              "Guliza",
#              "Meerim",
#              "Jamolbi",
#              "Tatina"
# ]
# print(jan24_names.)

# person = ("John", "Jones", "01-01-1909", "123-3212", ["224-833-12332", "553--312-1321", "836-635-3234"])
# person[-1][0] = "762-098-7876"
# print(person)

# person = {
# "name": "Jone",
# "last name": "Jones",
# "date of birth": "10-10-1999",
# "ssn": "123-2243",
# "phone": ["224-988-9098", "123-4214-124214", "123-4124-124"]

# }

# print(person["ssn"])


#___________________________________________________________
# person = {
# "name": "Jone",
# "last name": "Jones",
# "date of birth": "10-10-1999",
# "ssn": "123-2243",
# "phone": ["224-988-9098", "123-4214-124214", "123-4124-124"]

# }

# person["name"] = "Jones"
# print(person)
#_____________________________________________________________

############################TASK

# movies = [
#     {
# "name": "The Dark Knight",
# "year of release": "2008",
# "director": "Christopher Nolan",
# "main actors/actresses": ["Christian Bale", "Gary Oldman", "Morgan Freeman", "Michael Caine"],


#     },



# {
# "name": "Top Gun",
# "year of release": "1986",
# "director": "Tony Scott",
# "main actors/actresses":["Tom Cruis", "Anthony Edwards", "Kelly McGillis"]
# }
# ]

#for movie in movies:   #iterating inside of a list ---> dictinary
    #print("----------------------------")
    # for info in  movie.items():
    #for info in  movie.items():
     #   print(info)


# str = {1,1,1,2,2,2,3,3,3, 4, "Hello", "Hello"}
# print(str)

# lst = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, "Hello", "Hello", "Word", "Word"}
# st = set(lst)
# lst = list(st)
# print(lst[-1])

# st = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, "Hello", "Hello", "Word", "Word"}
# st.add("Myro")
# print(st)
# st.remove("Myro")
# print(st)

# st = {3,2,4,6,1,3,51,52,66}
# print(st)


# st = {3,2,4,6,1,3,51,52,66}
# for num in st :
#     print(num)

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# union_set = set_a | set_b    #put sets thogether
# print(union_set)
    #if this 
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# union_set = set_a & set_b   #put just same value
# print(union_set)


#--------------------------------------------------------------------NXT TOPIC

#Comprehension
# lst = []

# for i in range(10):
#     lst.append(i)

# print(lst)


# lst = [num for num in range(20)]   ###[value | for loop]

# print(lst)



# lst = [char for char in "Hello"]   
# print(lst)

#lst = [char for char in "Hello" if char == 'l']
#print(lst)
                        # lst = []
                        # for char in "Hello":
                        #     if char == 'l':
                        #   lst.append(char)



#---------------------------------------------------------------------

#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#lst = [fruit for fruit in fruits if 'a' in fruit]
#print(lst)
##print all fruits with letter "a"

# 1 : 1
# 2 : 4
# 3 : 9
# 4 : 16


d = {i : i ** 2 for i in range(1, 5)}
print(d)