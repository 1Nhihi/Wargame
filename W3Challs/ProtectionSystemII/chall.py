def check0(s):
	if len(s) <= 4 and len(s) >= 9:
		return 0
	for i in s:
		if i < 97 and i > 122:
			return 0
	return 1


def cal0(s):
	v4 = s[0]
	for i in range(1, len(s)):
		if i%2 ==1 :
			v4 += s[i]
		else:
			v4 -= s[i]
	return v4

def cal1(s):
	v4 = s[0]
	for i in range(1, len(s)):
		if i%2 ==1 :
			v4 -= s[i]
		else:
			v4 += s[i]
	return v4

def check1(a1, a2):
	if sum(a1) != sum(a2):
		return  0

	for i in a1:
		if i in a2:
			return 0

	for i in range(len(a1)):
		if a1[i] in a1[i+1:]:
			return 0
	for i in range(len(a2)):
		if a2[i] in a2[i+1:]:
			return 0
	return(1)

def checkpass(a):
	for i in range(1, len(a) -2):
		if i % 2 :
			if a[i] < a[i+2]:
				# print("hihi")
				return  0
		else:
			if a[i] > a[i+2]:
				# print("hihi")
				return 0
	if a[0] < a[-1]:
		return 0
	return 1

login = input('Please enter your login :')
password = input('Please enter your password :')
login = [ord(i) for i in login]
password = [ord(i) for i in password]

if (check0(login) == 0 or check0(password) == 0):
	print("Wrong password or login !", 0)
elif cal0(login) != cal1(password):
	print("Wrong password or login !", 1)
elif check1(login,password) == 0 or checkpass(password) == 1:
	print("Wrong password or login !", 2)
else:
	print("Good password and login !!")



