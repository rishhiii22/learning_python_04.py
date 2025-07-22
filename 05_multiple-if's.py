a = int(input("Enter your age:"))

# if statement no 1

if(a%2 == 0):

  print("a is even")
  # If statement no.1 ends here
  
# If statement no.2
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

    # If statement no.2 ends here.


print("Thank you for using this program")