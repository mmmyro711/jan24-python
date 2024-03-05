
# animal_list = [
#     'lion', 'tiger', 'elephant', 'giraffe', 
#     'zebra', 'hippopotamus', 'monkey', 'crocodile', 
#     'bear', 'panda', 'penguin', 'kangaroo', 'lion', 
#     'gazelle', 'parrot', 'toucan', 'giraffe', 'elephant', 
#     'kangaroo', 'monkey'
#     ]

# print(animal_list)

def animals(my_list):
 
    # Creating an empty dictionary
    count = {}
    for i in [
    'lion', 'tiger', 'elephant', 'giraffe', 
    'zebra', 'hippopotamus', 'monkey', 'crocodile', 
    'bear', 'panda', 'penguin', 'kangaroo', 'lion', 
    'gazelle', 'parrot', 'toucan', 'giraffe', 'elephant', 
    'kangaroo', 'monkey'
   ]:
        count[i] = count.get(i, 0) + 1
    return count
 
 
# Driver function
if __name__ == "__main__":
    my_list = ['lion', 'tiger', 'elephant', 'giraffe', 
    'zebra', 'hippopotamus', 'monkey', 'crocodile', 
    'bear', 'panda', 'penguin', 'kangaroo', 'lion', 
    'gazelle', 'parrot', 'toucan', 'giraffe', 'elephant', 
    'kangaroo', 'monkey']
    print(animals(my_list))