username = "Batman"
password = "I am Batman"
input_username = input("username:")
input_password = input("password:")

for i in range(500000000000000):
	if input_password == password and input_username == username:
		print("Welcome")
		break
	else:
		input_username = input("username:")
		input_password = input("password:") 