#for i in range(5):
#    print(i)
#else:
#    print("The lopps is finished") 
######for else and while else is gonna run when the loop is finished.

#----------------------------------------------------------------------    
#for i in range (10):
#    if i % 2 ==1:
#        continue
#    print(i)
#else:
#    print("The loops is stopped")

#-----------------------------------------------------------------------
#for i in range (10):
#    if i % 2 ==1:
#        pass
#    print(i)
#else:
#    print("The loops is stopped")

#################TASK
#for i in range(1, 4):
   #for j in range(1, 4):
      #for k in range (1, 4):
            #print(i,j,k)

#####################
#jan24_names = ["Aiperi", "Khusraf", "Fatima", "Yrys", "Myroslav", "Abbos","Dastan","Guliza","Meerim"]
#for name in jan24_names:
#    print(name[::-1])

##############TASK2
#numbers= [10, 10.4, 90, 110, 10, 23.3]
#num=0.0
#for num in numbers:

#    pass

#jan24_names = [
  #           "Aiperi",
  #           "Khusraf",
  #           "Fatima", 
  #           "Yrys", 
 #            "Myroslav", 
 #            "Abbos",
 #            "Dastan",
 #            "Guliza",
 #            "Meerim",
 #            "Jamolbi",
 #            "Tatina"
#]

#del jan24_names[-1]
#print(jan24_names)
#deleate 


#jan24_names = [
#             "Aiperi",
#             "Khusraf",
#             "Fatima", 
#            "Yrys", 
#             "Myroslav", 
#             "Dastan",
#             "Guliza",
#             "Meerim",
#             "Jamolbi",
#             "Tatina"
#]#

#jan24_names.append (3)
#print(jan24_names)


#jan24_names = [
 #            "Aiperi",
 #            "Khusraf",
 #            "Fatima", 
 #           "Yrys", 
 #            "Myroslav", 
 #            "Dastan",
 #            "Guliza",
 #            "Meerim",
#            "Jamolbi",
#             "Tatina"
#]
#jan24_names.sort(reverse=True)
#print(jan24_names)

#sort a-z and reverse


jan24_names = [
             "Aiperi",
             "Khusraf",
             "Fatima", 
            "Yrys", 
             "Myroslav", 
             "Dastan",
             "Guliza",
             "Meerim",
             "Jamolbi",
             "Tatina"
]
may24_names = jan24_names.copy
may24_names.append("Esen")
print (id(may24_names))
print (id(jan24_names))