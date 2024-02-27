
##Write a program that takes a temperature in Celsius and converts it to Fahrenheit.

#Fahrenheit = (Celsius * 1.8) + 32

c = (( 25 * 1.8 ) + 32) #77.0
c1 = (( 12 * 1.8 ) + 32) #53.6
#print(c1) 

##Write a program that takes a string input from the user and reverses it.

txt = "hello world" [: :-1] #dlrow olleh
#print (txt)


##Write a program that accepts user input of two variables, chars, and word. The program should then perform the following tasks:
    #Let’s assume that the length of the variable chars is exactly 4.
    #Use string concatenation to create a new variable called result. The first half of chars should be included in the result up to the middle index, followed by the word variable, and then the second half of chars from the middle index onwards.
    #Print out the resulting string stored in the result variable.

chars = "<<>>"
insert = "hello"
result = chars [2:] + insert + chars [:2]
#print (result)

chars = "aabb"
insert = "hello"
result = chars [:2] + insert + chars [2:]
#print (result)


##In AWS there is something that is called ARN Format that follows this format:

