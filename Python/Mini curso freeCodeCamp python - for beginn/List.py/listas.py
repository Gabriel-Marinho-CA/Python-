friends = ["olivia",5.3, True,"Arrow"]  #famoso array / vetor
print(friends)
friends[1] = "Mike" # modifying items thro list, of him index [0,1,2,3,n]

print(friends[1:4])
print("=================")

lucky_numbers = [4,8,15,16,18,9]
friend = ["kevin","mario","luigi","lucca","lucca","edgar"]

friend.extend(lucky_numbers)  # function extender list

friend.append("Marcos") #function increase +1 item

friend.insert(1,"KAKA") # function incresa +1 item according to the posicion of the index, like : [ 1 , 2 ,3 ] insert(1,4), be like : [ 1, 4,2,3]

friend.remove("kevin") # You can remove any item by name or var 

#friend.clear() # basically clean all the list

friend.pop() # exclude the last element of the list
 
print(friend.index("mario")) # sourche if there's any element in the list and retur a 0 or 1 ( True or false)

print(friend.count("lucca")) # count how much elemente equal have

# ***** friend.sort() #Organizate as a alfabetic order or increase sequence

lucky_numbers.reverse() # just reverse the list
print(friend)
print(lucky_numbers)

friend2 = friend.copy() # copia uma variavel
print(friend2)