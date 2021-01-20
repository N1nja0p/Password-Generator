#Password Generator Is Created By Abhimanyu Sharma A.K.A N1nja0p
import random
import string
import time
if __name__=="__main__":
	s1=string.ascii_lowercase
	s2=string.ascii_uppercase
	s3=string.digits
	s4=string.punctuation
	while True:
		try:
			plen=int(input("Enter Password Length : "))
			break
		except ValueError:
			print("Please Enter Password Length In Number")
			plen=int(input("Enter Password Length : "))
	s=[]
	s.extend(list(s1))
	s.extend(list(s2))
	s.extend(list(s3))
	s.extend(list(s4))
	random.shuffle(s)
	time.sleep(1)
	print("Generating Password.........")
	time.sleep(1)
	print("The Password For You Is : ")
	password="".join(s[0:plen])
	print(password)
	print("It Will Be Saved On Your Computer As \"save.txt\"")
	with open("save.txt","a")as f:
    		f.write(password)

