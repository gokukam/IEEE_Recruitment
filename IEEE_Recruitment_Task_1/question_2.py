# Accepting a paragraph
para = input("Enter your paragraph: ")
words = para.split()  # Space-separated list of para's words
palindromes = []  # Empty list to store palindromes

for word in words:
    # [::-1] indicates negative step from beginning to end of string,
    # so the string gets reversed
    if word == word[::-1]:
        palindromes.append(word)

# Checking if list is empty and printing 0 if yes
if palindromes:
    for p in palindromes:
        print(p)
else:
    print(0)
