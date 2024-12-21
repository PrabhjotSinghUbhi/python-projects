def encode(word , key):
    secret = ""
    for i in range(len(word)):
        if word[i].isupper():
            secret += chr(((ord(word[i]) - ord('A') + key) % 26) + ord('A'))
        elif word[i].islower():
            secret += chr(((ord(word[i]) - ord('a') + key) % 26) + ord('a'))
        elif word[i] == ' ':
            secret += " "
    print(f"Here's the encoded result: {secret}")

def decode(word , key):
    expose = ""
    for i in range(len(word)):
        if word[i].isupper():
            expose += chr(((ord(word[i]) - ord('A') - key) % 26) + ord('A'))
        elif word[i].islower():
            expose += chr(((ord(word[i]) - ord('a') - key) % 26) + ord('a'))
        elif word[i] == ' ':
            expose += " "
    print(f"Here's the decoded result: {expose}")

