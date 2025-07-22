# If-elif-else ladder example in Python

a = int(input("Enter your age:"))


if(a>=18):
    print("You are above the age of consent")
    print("You can vote")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 which is invalid")

else: 
    print("You are below the age of consent")

    print("You cannot vote")

print("Thank you for using this program")
# This code checks the age and provides appropriate messages based on the input.

