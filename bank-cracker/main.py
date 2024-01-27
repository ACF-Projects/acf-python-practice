from bankcracker import log_error, print_cyan, print_green

# BANK CRACKER

"""
Welcome, hacker.

Your goal is to infiltrate the Bank of ACF to
test their security is as a white-hat hacker.
White-hat hackers ensure security of pre-existing
applications by attempting to access them
without malicious intent.

You know that, to access their vault, you must
find the vault's secret security code, which is
compiled from typing THREE accurate passwords
into the Python script below.

Your job is to read through the code and figure
out what to type in as input to the three
prompts. This means reading through the script
and learning what the conditionals check for,
instead of running the code and guessing.

The answer to your homework is the final
key that is obtained from this procedure.

Good luck!
"""

print("-------------------------------------")
print_cyan("<< WELCOME TO THE BOA SECURITY FORM >>")
print_green("""By typing in three correct answers to
three different prompts, the password
to access the secret vault will be 
provided. Incorrect responses will
immediately terminate the script.""")
print("-------------------------------------")

# PROMPT ONE

input_one = input("Enter passkey #1: ")

if input_one + "3" == "1313":
    print_green("KEY ONE: " + input_one)
else:
    log_error("KEY ONE INCORRECT, STOPPING SCRIPT")

# PROMPT TWO

input_two = input("Enter passkey #2: ")

if int(input_two) == int(input_one) + 9:
    print_green("KEY TWO: " + input_two)
else:
    log_error("KEY TWO INCORRECT, STOPPING SCRIPT")

# PROMPT THREE

input_three = float(input("Enter passkey #3: "))

if int(input_three) != 155:
    log_error("A: KEY THREE INCORRECT, STOPPING SCRIPT")
elif input_three - 0.5 == int(input_three):
    print_green("KEY THREE: " + str(input_three))
else: 
    log_error("B: KEY THREE INCORRECT, STOPPING SCRIPT")

# FINISHED

print("-------------------------------------")
print_green("Completed all bank security checks.")
print_green("The passcode is: " + input_one + input_two + str(input_three))
print("-------------------------------------")