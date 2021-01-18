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
			password_length=int(input("Enter Password Length : "))
			break
		except ValueError:
			print("Please Enter Password Length In Number")
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
	print("".join(s[0:password_length]))
