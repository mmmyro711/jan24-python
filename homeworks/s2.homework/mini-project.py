# Import the 're' module for regular expressions
#import re

# Prompt the user to input a password and store it in the variable 'p'
#p = input("Enter your password: ")

# Set 'x' to True to enter the while loop
#x = True

# Start a while loop that continues until 'x' is True
#while x:  
    # Check conditions for a valid password:
    # Password length should be long 8 characters
 #   if (len(p) < 8 ):
 #       break
    
    # Password should contain at least one uppercase letter
  #  elif not re.search("[A-Z]", p):
  #      break
   
    # Password should contain at least one lowercase  letter
  #  elif not re.search("[a-z]", p):
  #      break
     # Password should contain at least one digit
   # elif not re.search("[0-9]", p):
    #    break
    # Password should contain at least one special character among '$', '#', '@'
    #elif not re.search("[@#$]", p):
    #    break
    # Password should not contain any whitespace character
    #elif re.search("\s", p):
        #break
   # else:
        # If all conditions are met, print "Valid Password" and set 'x' to False to exit the loop
    #    print("Password accepted")
     #   x = False
      #  break

# If 'x' remains True, print "Not a Valid Password"
#if x:
    #print("Not a Valid Password")

##################### it is now correct 

import re
while True:
    passwd = input("Enter your password: ")
    if len(passwd) > 23 or len(passwd) < 8:
        print ("Password length should be between 8 to 23 characters")
    elif not re.search('[a-z]', passwd):
        print ("Password should contain at least one lowercase letter")
    elif not re.search('[A-Z]', passwd):
        print ("Password should contain at least one capital letter")
    elif not re.search('[0-9]', passwd):
        print ("Password should contain at least one digit")
    elif not re.search ('[!@#$%^&*()]', passwd):
        print ("Password should contain at least one special character")
    else:
        print("Password accepted.")
        break
    



