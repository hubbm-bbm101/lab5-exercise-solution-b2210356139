def check_email(email):
    if (email.find("@")) != -1 and (email.find(".")) != -1:
        return 1
    else:
        return 0

email = input("Enter your email adress:")

if check_email(email):
    print("{} is a valid email adress.".format(email))
    
else:
    print("{} is not a valid email adress.".format(email))