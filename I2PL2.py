#print("'Do not go gentle into that good night.'")

#print("""'Do not go gentle into that good night,
#Old age should burn and rave at close of day;
#Rage, rage, against the dying of the light.'""")

#x = "October"

#print (x.upper())
#print (x.lower())

#input("\n\nPress the enter key to exit.")

#vValue = 35
#print(type(vValue))
#print(vValue)

#x = int(34)
#y = int(24.9)
#print x, y, x-y

#vValue = 35.34
#print(type(vValue))
#print(vValue)

#vMonth = "October Yo!"

# TO CHOOSE A SPECIFIC CHRACTER IN "OCTOBER YO!"
#vLetter = vMonth[1]
#print(vLetter)

# TO PRINT IN A LOOP TO MAKE "OCTOBER YO!" VERTICAL
#i=0
#for letter in vMonth:
#    print(vMonth[i])
#    i=i+1

#vMonth = "September"
#print(vMonth[5])

# SLICING UP STRINGS
#vMonth = "December"
#print(vMonth[3:6])
#print(vMonth[:6])
#print(vMonth[6:])

# USING THE FIND() METHOD, RETURNS AN INTEGER THAT REPRESENTS STARTING POSITION OF WHERE SUB-STRING LOCATED IN A STRING
#vMessage = "Life is a beach and then you die."
#print(vMessage)
#print(vMessage.find("beach"))

#vMessage = "Life is a beach and then you die."
#print(vMessage)

# USING THE LEN() METHOD TO FIND THE LENGTH OF A STRING
#print("The length of the string is")
#print(len(vMessage))

# CONCATENATION USING ADDITION
#vString1 = "Douglas"
#vString2 = "Lau"
#print(vString1 + vString2)
#print vString1, + 3

# USING FLOAT() TO CONVERT A GIVEN VALUE INTO A FLOAT
#vInteger = 10
#print(vInteger)
#vFloat = float(vInteger)
#print(vFloat)

# USING STR() TO CONVERT A GIVEN VALUE INTO A STRING
#vInteger = 32
#print(vInteger)
#vString = str(vInteger)
#print(vString)

#vYears = input("Enter your age.")
#vMonths = vYears*12
#print "You are", vMonths, "months old."

# USING "IF" STATEMENTS
#vNumber1 = input("Enter a number: ")
#vNumber2 = input("Enter another number: ")
#if vNumber1 > vNumber2:
#    print vNumber1, "is bigger."
#if vNumber1 < vNumber2:
#    print vNumber1, "is smaller."

#vNumber = 0
#while vNumber < 10:
#    print(vNumber)
#    vNumber = vNumber + 1

#vQuote = "What."
#print(vQuote)

#vName = "Douglas Lau"
#print(vName)

x = input("Enter a number: ")
y = input("Enter a second number: ")
z = input("Enter a third number: ")
print "The sum of these three numbers is", x+y+z
