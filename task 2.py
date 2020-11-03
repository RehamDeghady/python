print("1.check palindrome")
print("2.check if prime")
print("3.Exit")
operation = int (input ("choose an operation:"))
if operation == 1 :
      word = str(input("enter the word"))
      revword = word[::-1]
      print("reversed word is" ,revword)
      if word == revword :
          print("yes it is palindrome")
      else:
          print("No it is not palindrome")
elif operation == 2:
    num = int(input("enter a positive number"))
    if num<=0:
        print(num,"is not a prime number")
    else:
        for i in range(2,num):
            if num%i == 0 :
                print(num , "is not a prime number")
                break
        else:
            print(num, "is a prime number")
else:
    print("EXIT")


