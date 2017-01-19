# LISTS
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print(fruitList[0]) #Starts from left, first slot is labelled 0
#print(fruitList[-2]) #Starts from right, first slot is labelled -1

# CONCATENATION
#numberList1 = [1,2,3]
#numberList2 = [6,7,8]
#
#numberList3 = numberList1 + numberList2
#print(numberList3)

# MULTIPLICATION
#numberList = [1,2,3]
#print(numberList * 3)

# SLICING
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print(fruitList[2:5])
#print(fruitList[:4])
#print(fruitList[5:])

# EDITING A LIST
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#fruitList[1] = "KIWI" #Change value at position 1 (replaces "orange" with "kiwi")
#print(fruitList)

# LIST OF LISTS
#olympicList = [["London",2012],["Beijing",2008],["Athens",2004]]
#print(olympicList)
#print(olympicList[1]) #Print the first element in the list
#print(olympicList[1][0]) #Only print the first part in the list's second element

# LIST METHODS: APPEND()
#inventoryList = ["sword","armour","shield","healing potion"]
#print(inventoryList)
#inventoryList.append("cabbage") #Cabbage is added to end of list because we didn't define where to put it
#print(inventoryList)

# LIST METHODS: INSERT()
#inventoryList = ["sword","armour","shield","healing potion"]
#print(inventoryList)
#inventoryList.insert(2,"cabbage")
#print(inventoryList)

# LIST METHODS: SORT()
#inventoryList = ["sword","armour","shield","healing potion"]
#print(inventoryList)
#inventoryList.sort() #Sort in alphabetical order
#print(inventoryList)

# LIST METHODS: LIST.COUNT()
#inventoryList = ["sword","armour","shield","healing potion"]
#print(inventoryList)
#print(inventoryList.count("sword")) #Count how many times an element occurs in the list

# LIST METHODS: LIST.EXTEND()
#inventoryList = ["sword","armour","shield","healing potion"]
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print(inventoryList)
#print(fruitList)
#inventoryList.extend(fruitList) #Similar to concatenation
#print(inventoryList)
#print(fruitList)

# LIST METHODS: LIST.POP()
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print(fruitList)
#
#v_fruit = fruitList.pop() #Remove the last element
#print(fruitList)
#print(v_fruit)
#
#v_fruit = fruitList.pop(0) #Remove the first element
#print(fruitList)
#print(v_fruit)

# LIST METHODS: LIST.REMOVE()
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print(fruitList)
#fruitList.remove("banana") #Remove the first occurance of an element
#print(fruitList)

# LIST METHODS: LIST.REVERSE()
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print(fruitList)
#fruitList.reverse() #Reverse the order of a list
#print(fruitList)

# LIST METHODS: LIST.INDEX()
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print(fruitList)
#v_index = fruitList.index("banana") #Position of the banana in the list
#print(v_index)

# LENGTH OF LIST
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print(fruitList)
#print(len(fruitList))

# "IN" FUNCTION
#fruitList = ["apple","orange","banana","grape","tomato","mango"]
#print("apple" in fruitList) #Results in Boolean output

# "MIN" AND "MAX" OF A LIST
fruitList = ["apple","orange","banana","grape","tomato","mango"]
print(fruitList)
print(min(fruitList)) #Minimum/smallest of the list
print(max(fruitList)) #Maximum/largest value in the list
