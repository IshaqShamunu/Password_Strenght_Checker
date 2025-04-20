password = "Danrimi@2025"

has_upper =  any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?" for char in password)
long_enough = len(password) >= 8

print("\n Password Strength Checker")
if not password:
	print("password cannot be empty")
elif not long_enough:
	print("Password must be atleast 8 character")
else:
	if not has_upper:
		print("Password Must have atleast one upper case")
	if not has_lower:
		print("Password must have atleast one lower  case letter")
		if not has_special:
			print("Password must have atleast one Special Character")
		if not has_digit:
			print("Password must have atleast one Number")
if all([long_enough, has_upper, has_lower, has_special, has_digit]):
        print("Your password is strong!")
else:
        print("Improve your password by addressing the points above.")
