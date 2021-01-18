import string
import random
if __name__=='__main__':
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    while True:
        try:
            password_length=int(input("Enter Password Length : "))
            break
        except ValueError:
            print("Please Enter Length In Numbers")
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    print("Your Password Is : ")
    print("".join(s[0:password_length]))