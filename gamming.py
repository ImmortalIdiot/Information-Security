from input_validation import incorrect_user_input, require_not_null, require_symbols_in_string


def laboratory_work():
    print("Лабораторная работа №7 'Гаммирование'")


def encrypt(user_message: str, alphabet: str, key: str):
    encrypted_message = ""
    counter = 0

    for char in user_message:
        key_char = key[counter]
        counter += 1
        msg_index = alphabet.index(char)
        key_index = alphabet.index(key_char)

        if msg_index >= 0 and key_index >= 0:
            result_index = msg_index ^ key_index
            result_char = alphabet[result_index]
            encrypted_message += alphabet[(msg_index ^ key_index)]

            msg_binary, key_binary = format(msg_index, "08b"), format(key_index, "08b")
            # print(f"Символ сообщения: {char}\n"
            #       f"Индекс символа в десятичном СС: {msg_index}\n"
            #       f"Индекс символа в двоичной СС:  {msg_binary}\n"
            #       f"Символ ключа: {key_char}\n"
            #       f"Индекс ключа в десятичной СС: {key_index}\n"
            #       f"Индекс ключа в двоичной СС: {key_binary}\n"
            #       f"Операция 'исключающее ИЛИ': {format(result_index, '08b')}\n"
            #       f"Результирующий символ: '{result_char}'\n")

    return encrypted_message


def decrypt(user_message: str, alphabet: str, key: str):
    decrypted_message = ""
    key_length = len(key)
    counter = 0

    for char in user_message:

        key_char = key[counter % key_length]
        counter += 1
        msg_index = alphabet.index(char)
        key_index = alphabet.index(key_char)

        decrypted_message += alphabet[(msg_index ^ key_index)]

    return decrypted_message


def check_user_input(action: str, alphabet: str):
    if action == "1":
        user_input = input("Введите сообщение, которое хотите зашифровать.\nПосле ввода нажмите на Enter.\n>>")
        require_not_null(user_input), require_symbols_in_string(user_input, alphabet)
    else:
        user_input = input("Введите сообщение, которое хотите расшифровать.\nПосле ввода нажмите на Enter.\n>>")
        require_not_null(user_input), require_symbols_in_string(user_input, alphabet)
    return user_input


def get_is_correct_key(user_message: str):
    key = input("Введите гамму:\n>>")
    require_not_null(key)
    msg_length = len(user_message)
    while msg_length > len(key):
        key += key

    while len(key) > len(user_message):
        key = key[:len(user_message)]
    return key


ALPHABET = ("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmn"
            "opqrstuvwxyz .,!0123456")  # 128 символ
print(len(ALPHABET))
ENCRYPTION = "Зашифрованное сообщение: "
DECRYPTION = "Расшифрованное сообщение: "

laboratory_work()

choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите вывести алфавиты, введите 2\n>>")

if choice == "1":
    message = check_user_input(choice, ALPHABET)
    print(f"Использованный алфавит:\n{ALPHABET}\n\n" + ENCRYPTION +
          encrypt(message, ALPHABET, get_is_correct_key(message)))

elif choice == "2":
    message = check_user_input(choice, ALPHABET)
    print(f"Использованный алфавит:\n{ALPHABET}\n\n" + DECRYPTION +
          decrypt(message, ALPHABET, get_is_correct_key(message)))

elif choice == "3":
    print(f"Использованный алфавит:\n{ALPHABET}")

else:
    incorrect_user_input()
