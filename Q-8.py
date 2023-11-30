a = input("enter a letter:")

def vowel(letter):
    vowel = "aeiou AEIOY"
    return letter in vowel

if vowel(a):
    print("a is a vowel.")
else:
    print("a is not a vowel.")
    