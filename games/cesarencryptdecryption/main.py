alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(message, shift_number):
    new_empty_list = []
    for word in message.split():
        new_word = ''
        for char in word:
            if char not in alphabet:
               new_word += char
               continue
            else: 
               char = alphabet[(alphabet.index(char) + shift_number) % len(alphabet)]
               new_word +=char
        new_empty_list.append(new_word)

    return "The encoded text is " + ' '.join(new_empty_list)

def decrypt(cipher_message, shift_number):
    new_empty_list = []
    for word in cipher_message.split():
        new_word = ''
        for char in word:
            if char not in alphabet:
               new_word += char
               continue
            else: 
               char = alphabet[(alphabet.index(char) - shift_number) % len(alphabet)]
               new_word +=char
        new_empty_list.append(new_word)

    return "The decoded text is " + ' '.join(new_empty_list)

from logo import logo
print(logo)

end_of_program = False
while not end_of_program:
  action = input("type 'E' to encrypt, type 'D' to decrypt\n")
  message = input("Enter your message:\n").upper()
  shift_number = int(input("Enter the shift number:\n"))
  if action == "E":
    print(encrypt(message,shift_number))
  else:
    print(decrypt(message,shift_number))
  restart = input("Type 'Y' if you want to go again. Otherwise type 'N'.\n")
  if restart == "N":
    end_program = True
    print("See you next time!")
    break
