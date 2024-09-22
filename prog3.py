num=int(input("Enter any positive number"))
try:
    if num<=0:
        raise ValueError("Positive number-Input is correct")
    else:
       raise ValueError("Negative number-Input is incorrect")
except ValueError as e:
 print(e)

    
