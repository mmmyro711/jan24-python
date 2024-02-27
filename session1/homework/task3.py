##Write a program that accepts user input of two variables, chars, and word. The program should then perform the following tasks:
    #Let’s assume that the length of the variable chars is exactly 4.
    #Use string concatenation to create a new variable called result. The first half of chars should be included in the result up to the middle index, followed by the word variable, and then the second half of chars from the middle index onwards.
    #Print out the resulting string stored in the result variable.

str1 = "<<>>"
str2 = "hello"
result = str1 [2:] + str2 + str1 [:2]
print (result)


str3 = "aabb"
str4 = "hello"
result = str3 [:2] + str4 + str3 [2:]
print (result)
