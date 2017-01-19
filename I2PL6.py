# MULTI-LINE CODE
#print("""
#PPAP
#I have a apple
#I have a pen
#UHHHHHGHHGHGHHGHGHHGHGHGHGHHG
#Apple pen
#""")

# USING FUNCTIONS SO WE DON'T HAVE TO REPEAT MULTI-LINE CODE
#def ppap():
#    print("""
#    PPAP
#    I have a apple
#    I have a pen
#    UHHHHHGHHGHGHHGHGHHGHGHGHGHHG
#    Apple pen
#    """)
#print(ppap())

# USING FUNCTIONS TO RETURN VALUES
#def f_print_largest(int1,int2):
#    if int1 > int2:
#        print int1,"is the largest"
#    if int1 < int2:
#        print int2,"is the largest"

#print(f_print_largest(1002,24332))

# RETURNING THE HIGHEST INTEGER USING FUNCTIONS
def f_larger(int1,int2):
    if int1 >= int2:
        return int1
    else:
        return int2

x = 12
y = 7
z = 79

print(f_larger(f_larger(x,y),z))
