import asci_art
import cipher

print(asci_art.logo)

action =  input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
digits = input("Type your message: ")
shift_no = int(input("Type the shift number: \n"))

if action == "encode":
    cipher.encode(digits,shift_no)
elif action == "decode":
    cipher.decode(digits,shift_no)
else:
    print("Please type 'encode' to encrypt, type 'decode' to decrypt: \n")





