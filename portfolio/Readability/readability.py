l = 0.0
w = 0.0
s = 0.0
g = 0.0
i = 0
index = 0

# Prompt user to input text
str = input("Input text: ")

# Add one to the number of words if the text is not empty
if str[0] != None:
    w += 1

for i in str:
    # count the number of letters
    if ((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9')):
        l += 1

    # count the number of words
    if i == ' ':
        w += 1

    # count the number of sentences
    if (i == '.' or i == '!' or i == '?'):
        s += 1

# Determining the readability grade of the text using the given index (index = 0.0588 * L - 0.296 * S - 15.8)
g = (0.0588 * (l / (w / 100))) - (0.296 * (s / (w / 100))) - 15.8

index = int(g + 0.5)

# printing the Grade of the text that the program receives from the user
if index >= 2 and index <= 16:
    print(f"Grade {index}")

elif index < 1:
    print("Before Grade 1")

else:
    print("Grade 16+")