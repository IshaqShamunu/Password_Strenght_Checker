Password Strength Checker

A simple Python script to check the strength of a user’s password based on common security criteria.

Features

Verifies that the password:

Is at least 8 characters long

Contains at least one uppercase letter

Contains at least one lowercase letter

Includes at least one digit (0–9)

Has at least one special character (e.g. @, #, $, etc.)


Provides feedback on any missing elements

Prints a final verdict on overall strength


How It Works

The script evaluates a hardcoded password variable using:

.isupper(), .islower(), and .isdigit()

A set of allowed special characters

A length check (len(password) >= 8)


It then prints messages for any unmet requirements and—if all checks pass—declares the password strong.

Sample Output

Password Strength Checker
Your password is strong!

or

Password Strength Checker
Password must have at least one uppercase letter
Password must have at least one special character
Improve your password by addressing the points above.

How to Use

1. Clone the repository:

git clone https://github.com/IshaqShamunu/Password_Strenght_Checker.git


2. Navigate into the project directory:

cd Password_Strenght_Checker


3. (Optional) Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate


4. Run the script:

python work.py



License

This project is free to use for learning and educational purposes.
