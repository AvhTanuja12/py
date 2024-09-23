dict={'MON':3,'TUE':5,'WED':6}
print("The given dictionary:",dict)
check_key=input("Enter key to check:")
check_key=input("Enter value:")
if check_key in dict:
    print(check_key,"is present")
    dict.pop(check_key)
    dict[check_key]
else:
    print(check_key,"is not present")
    dict[check_key]
    print("Updated dictionary:",dict)
