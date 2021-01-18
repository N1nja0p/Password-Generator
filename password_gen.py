#Password Generator Is Created By Abhimanyu Sharma
import string #string module to generate random characters
import random #random module to shuffle
if __name__=='__main__':
    s1=string.ascii_lowercase #generate lower case
    s2=string.ascii_uppercase #generate upper case
    s3=string.digits #generate integers
    s4=string.punctuation #generate characters
    while True:
        try:
            password_length=int(input("Enter Password Length : ")) #password len input
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
    password="".join(s[0:password_length]) #simple concatination
    print(password)
    print("It Will Be Saved On Your Computer As \"save.txt\"")
    with open("save.txt","a")as f:
        f.write("Your Password Is : "+password+"\n")