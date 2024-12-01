import function_paramaters_and_caesar.caesar_art as caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesar_art.logo)

def caesar(direction, original_text, shift_amount):
    if direction == "encode":
        encoded_text = ""  
    #Hvis man finner matchende bokstav i alphabet så legger man til bokstav.index + shift_amount. 
        for letter in original_text:
            #Hvis symbolet ikke er med i listen så legger vi den til i encoded som den er, for å få med symboler
            if letter not in alphabet:               
                encoded_text += letter
            else:
                #shiften_position finner indexen til bokstav i alphabet og så legger til shift_amount
                shifted_position = alphabet.index(letter) + shift_amount
                #Denne her sikrer at man ikke går utenfor lengden til alfabetet. Da begynner man på nytt
                shifted_position %= len(alphabet)
                #Legger til den nye bokstaven til encoded_text
                encoded_text += alphabet[shifted_position]
    
        print(f"Here is the encrypted text: {encoded_text}")
    elif direction == "decode":
        decrypted_text = ""

        for decode_letter in original_text:
            #shiften_position finner indexen til bokstav i alphabet og så trekker fra shift_amount for å gå bakover
            shifted_position = alphabet.index(decode_letter) - shift_amount
            #Denne her sikrer at man ikke går utenfor lengden til alfabetet. Da begynner man på nytt
            shifted_position %= len(alphabet)
            #Legger til den nye bokstaven til encoded_text
            decrypted_text += alphabet[shifted_position]
        
        print(f"Here is the decrypted text: {decrypted_text}")
    else:
        print("Please write decode or encode.")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    
    continue_or_not = input("Type yes if you want to go again. Otherwise, type no: ").lower()
    if continue_or_not == "no":
        print("Thank you for playing. PEACE.")
        break 
    elif continue_or_not == "yes":
        continue
    else:
        print("Not valid input. Ending the program. ")


