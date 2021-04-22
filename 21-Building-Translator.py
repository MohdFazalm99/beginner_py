# Now in this we will translate and convert all the vowels to g or any letter

def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter the phrase : ")))