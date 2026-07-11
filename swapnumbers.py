a= int(input("enter the first number: "))
b= int(input("enter the second number: "))
#using swap with 3rd variable

temp = a
a = b
b = temp

print("after swapping: ")
print("a=",a)
print("b=",b)

#without using third variable

x= int(input("enter the first number: "))
y= int(input("enter the second number:"))

x,y=y,x

print("after swap: ")
print("x=",x)
print("y=",y)