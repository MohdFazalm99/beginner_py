secret_word = "Phuppa hain"
# this will be our secret word
guess = ""
# this is a variable used for storing the words which the user will guess
guess_count = 0
# this will track how many time a user guess
guess_limit = 2
# this will tell the program how many time  a user guess
out_of_guesses = False
# this variable will tells if there is any other guesses are left or not

while guess != secret_word and not(out_of_guesses):
    if guess_count <= guess_limit:
        guess = input("Enter your guess : ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses! YOU LOSE :-(")
else:
    print("YOU WIN :-)")