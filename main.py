list_alphabet_num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', ' ', '?',
                     "'", ]
list_morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----",
                   ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", ".-.-.-", "--..--",
                   "/", '..--..', '.----.']
def morse_func():
    code_decode = input('Type Code or Decode').lower()
    if code_decode == 'code':
        user_input = input('Enter your text').lower()
        morse_code = ""
        for char in user_input:
            for char_ in list_alphabet_num:
                if char == char_:
                    morse_code += f" {list_morse_code[list_alphabet_num.index(char_)]}"
                elif char not in list_alphabet_num:
                    return print("Invalid input. please, try again")
        print(f"Morse code: {morse_code}")
    elif code_decode == 'decode':
        user_input = input('Enter your code')
        text = ''
        x = user_input.split()
        # xx = ''
        # if '/' in user_input:
        #     xx = user_input.replace('/', '')
        # x = xx.split()
        # print(x, xx)
        for item in x:
            for char_ in list_morse_code:
                if item == char_:
                    text += list_alphabet_num[list_morse_code.index(char_)]
                elif item not in list_morse_code:
                    return print("Invalid input. Please, try again")
        print(f"Your text: {text.upper()}")
    else:
        return print("Invalid input")



while True:
    morse_func()
