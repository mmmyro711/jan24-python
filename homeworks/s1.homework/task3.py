##Write a program that accepts user input of two variables, chars, and word. The program should then perform the following tasks:
    #Let’s assume that the length of the variable chars is exactly 4.
    #Use string concatenation to create a new variable called result. The first half of chars should be included in the result up to the middle index, followed by the word variable, and then the second half of chars from the middle index onwards.
    #Print out the resulting string stored in the result variable.


###############Program
#str1=str(input("Please enter a four-character string for the variable chars: "))
#str2=str(input("Please enter a word to insert into the middle of chars: "))
#middle = int(len(str1)/2)
#gm =str1[:middle:]
#get =gm + str2
#middle = get + str1[middle:]
#print ("This is your word combination:", middle) 
#("str1","str2")

########REMADE HOMEWORK

inp1 = input("Enter your characters:")
inp2 = input("Enter your word:")

result = inp1[0:2] + inp2 + inp1[2:4]
print(result)










#str1 = "<<>>"
#str2 = "hello"
#result = str1 [2:] + str2 + str1 [:2]
#print (result)


#str3 = "aabb"
#str4 = "hello"
#result = str3 [:2] + str4 + str3 [2:]
#print (result)