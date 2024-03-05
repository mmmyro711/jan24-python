# Create a list that contains numbers from 1 to 50 using list comprehension

# Using that list do the following:

# 1)Compute the sum of all even numbers in the list
# 2)Compute the product of all odd numbers in the list
# 3)Find the largest number in the list
# 4)Print out the result of all computations

#1)
# list_my = for even in [i for i in range(50) if i % 2 == 0]:      ##when i%2 ==0
    
# print(list_my)
# evennum = [num for num in range(50)if num % 2 == 0]
# sum_num = sum(evennum)
# print(evennum)
# print(sum_num) 
    
#2)

# odd_num =[ num for num in range (50) if num % 2 != 0]     #when i%2 !=0
# mult_odd = 2
# for num in odd_num:
#     mult_odd *= num
# print(mult_odd)



#3)
num = [num for num in range(50)]
max_number = (max(num))
print(max_number) 

# number = [54,67,12,33,69,32] 
# #printing max element 
# print (max(number))
      