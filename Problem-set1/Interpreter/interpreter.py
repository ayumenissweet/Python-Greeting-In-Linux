expression = input("Please Type an expression: ").strip()

x,y,z = expression.split(" ")

x = float(x) 
z = float(z)

if(y == "+"):
    result = x+z
elif(y == "-"):
    result = x-z
elif(y == "*"):
    result = x*z
elif(y == "/"):
    if(z == 0):
        print("ERROR : z = 0")
        result = 0
    else: result = x/z
else:
    print("Cant understand the expression")

print(result)