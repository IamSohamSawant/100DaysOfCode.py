alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                        
''')
direction=(input("Type 'encode' to Encrypt, Type 'decode' to Decrypt:\n ")).lower()
text=input("Type you message:\n")
shift=int(input("Type shift number:\n"))

#hello 2
# def encrupt(original_text,shift_amount):
#     cipher_text=""

#     for letter in original_text:
#         shift_position=alphabet.index(letter)+shift_amount #h is at position 7 --->+2 =9-j 
#         shift_position%= len(alphabet)
#         cipher_text+=alphabet[shift_position] #j
    
# encrupt(original_text=text,shift_amount=shift)

# def decrupt(original_text,shift_amount):
#     cipher_text=""
#     for letter in original_text:
#         shift_position=alphabet.index(letter)-shift_amount
#         shift_position%=len(alphabet)
#         cipher_text+=alphabet[shift_position]
    
# decrupt(original_text=text,shift_amount=shift)

def caeser(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
        shift_amount*=-1

    for letter in original_text:

        if letter not in alphabet:
            output_text+=letter
        else:
            shift_position=alphabet.index(letter)+shift_amount #---> 3 + (5* -1)= 3-5
            shift_position%=len(alphabet)
            output_text+=alphabet[shift_position]
    print(f"Here is your {encode_or_decode}d result: {output_text}")
caeser(original_text=text,shift_amount=shift,encode_or_decode=direction)

want_to_continue=True
while want_to_continue:
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart=="no":
        want_to_continue=False
        print("GoodBye")
    else:
        direction=(input("Type 'encode' to Encrypt, Type 'decode' to Decrypt:\n ")).lower()
        text=input("Type you message:\n")
        shift=int(input("Type shift number:\n"))

    caeser(original_text=text,shift_amount=shift,encode_or_decode=direction)

