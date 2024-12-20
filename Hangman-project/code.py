import random
import acsci_art

logo = acsci_art.symbol
words = acsci_art.words
hang = acsci_art.stages

print(logo)

word = random.choice(words).lower()
blank = "_" * len(word)
display = ""
print(word)

lives = 6

gameOver = False

corrected_words = []

while not gameOver:
    print(f"Word to guess: {blank}")
    guess = input(f"guess a letter: ").lower()
    display = ""

    present = False

    for i in word:
        if guess == i:
            display += i
            corrected_words.append(guess)
            present = True
        elif i in corrected_words:
            display += i
        else:
            display += "_"
            # print("Letter you have guessed is not in the word\n you loose a life")

    print(display)
    blank = display
    if not present:
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        print(f"****************************{lives}/6 LIVES LEFT****************************")

    print(hang[lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    if lives == 0:
        print(f"***********************IT WAS {word}! YOU LOSE**********************")
        break

    if "_" not in display:
        gameOver = True
        print(acsci_art.win)
