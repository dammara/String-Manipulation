# Markhus Dammar
# 2/6/2020
# This is the first proj of Adv. Prog. Techniques. This is string Manipulation.

print("""Hello, USER, or should I say, LOSER.
Help me out with something;
type out 3 words, separated by commas.""")

string = input(">>> ")
print(string)

input("Press ENTER to continue...")
print("The length of the string is...")
print(len(string))
input("Press ENTER to continue...")

print("\nHere's the first letter of the string.")
print(string[0])
print("Now here's the last letter")
print(string[-1])
input("Press ENTER to continue...")

print("I'm going to replace the third character.")
print(string.replace(string[2], " ", 1))
input("Press ENTER to continue...")
print("\nLet's do upper case and title case now.")
print(string.upper())
print(string.title())
input("Press ENTER to continue...")
alphaa = string.isalpha()
print('Is this string alpha?')
print(alphaa)
numm = string.isnumeric()
print("Is this string numeric?")
print(numm)
print("Before I split these, I'm going to display 'lower case'")
print(string.lower())
print("Now, I'm gonna split these up")
input("Press ENTER to continue...")
split = string.split(",")
print(split)
print("Thanks for playing")
input("Press ENTER to exit")
exit()







# del string[2}
