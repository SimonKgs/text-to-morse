morse_list = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'CH': '----',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'Ñ': '--.--',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '"': '.-..-.',
    '/': '-..-.'
}


def convert_to_morse(text_to_convert: str) -> list:
    clean_text = text_to_convert.replace(" ", "")
    final_morse_code = []
    for letter in clean_text:
        try:
            final_morse_code.append(morse_list[letter.upper()])
        except KeyError:
            final_morse_code.append('***')
            print(f'There is no key {letter}')
        except IndexError:
            final_morse_code.append('***')
            print(f'There is no key {letter}')

    return final_morse_code


def convert_morse_to_text(morse_to_convert) -> list:
    message_decoded = []
    for code in morse_to_convert:
        letter = ''
        try:
            letter = [letter for letter, value in morse_list.items() if value == code]
        except IndexError:
            letter = '***'
            print(f'Code {code} not found')
        finally:
            message_decoded.append(letter)

    return message_decoded


working = True

while working:
    user_action = input('What do you want to do?\n'
                        '1. convert message to morse code\n'
                        '2. convert from morse to message\n'
                        '3. exit\n'
                        '(type the number of the option)\n')

    if user_action == '1':
        user_message = input('Write your message:\n')
        message_converted = convert_to_morse(user_message)
        # print(' '.join(message_converted))
        print(message_converted)
    elif user_action == '2':
        user_code_message = input('Write your morse code here\n'
                                  'each letter must be separated by a coma\n'
                                  'eg: ...., ---, .-.., .-\n')
        code_string = user_code_message.replace(" ", "")
        split_string = code_string.split(',')

        final_message = convert_morse_to_text(split_string)
        print(final_message)

    elif user_action == '3':
        print('Bye')
        working = False
    else:
        pass
