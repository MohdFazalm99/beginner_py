# 1- simple if statement example

is_male = True

if is_male:
    print("you are a male")

# 2- simple if-else statement example

is_male1 = False

if is_male1:
    print("you are a male")
else:
    print("You are a female")

# 3- using if-else with or

is_male2 = True
is_tall = True

if is_male2 or is_tall:
    print("You are male or tall or both")
else:
    print(" You are neither male nor tall")

# 4- using if-else with and

is_male3 = True
is_short = False

if is_male3 and is_short:
    print("you are a tall male")
else:
    print("you are either not male or not tall")

# 5- using if-else and else-if statement with not operator

if is_male3 and is_short:
    print("you are a  male but not tall")
elif is_male3 and not(is_short):
    print(" you are a tall man")
else:
    print("you are a tiny man :-)")
