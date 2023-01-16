import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----' }

def encode_morse(text):
    morse_code = ""
    for letter in text:
        if letter in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[letter] + " "
        elif letter == " ":
            morse_code += "/ "
        else:
            print("ERROR")
            exit()
    return morse_code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sos.py <string>")
    else:
        input_text = " ".join(sys.argv[1:])
        print(encode_morse(input_text.upper()))
