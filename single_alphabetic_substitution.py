from input_validation import require_not_null, require_symbols_in_string, incorrect_user_input


def encrypt(u_key, message, alphabet): # Шифрование
    encryption_output = []
    alphabet_length = len(alphabet)
    for c in message:
        encryption_output.append(alphabet[(alphabet.find(c) + u_key) % alphabet_length])
    return encryption_output


def decrypt(u_key, message, alphabet): # Дешифрование
    decryption_output = []
    alphabet_length = len(alphabet)
    for c in message:
        decryption_output.append(alphabet[(alphabet.find(c) - u_key) % alphabet_length])
    return decryption_output


def key_input_validation(): # Ввод ключа и проверка его на исключение
    while True:
        u_key = input("Введите ключ\n>>")
        if u_key.isnumeric():
            return int(u_key)


ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя .,0123456789"
ALPHABET_LENGTH = len(ALPHABET)

ENCRYPTION = "Зашифрованное сообщение: "
DECRYPTION = "Расшифрованное сообщение: "

choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите расшифровать сообщение, введите 2\n"
               "Если Вы хотите вывести алфавит, введите 3\n>>")

if choice == "1":
    user_input = input("Введите сообщение, которое хотите зашифровать\nПосле ввода нажмите на Enter\n>>")
    # Проверка на исключения: ввод не может быть пустым, вводные символы должны принадлежать алфавиту
    require_not_null(user_input), require_symbols_in_string(user_input, ALPHABET)

    key = key_input_validation()

    print(f"\nАлфавит: {ALPHABET}")
    print("\n" + ENCRYPTION + "\n" + "".join(encrypt(key, user_input, ALPHABET)))

elif choice == "2":
    user_input = input("Введите сообщение, которое хотите расшифровать\nПосле ввода нажмите на Enter\n>>")
    # Проверка на исключения: ввод не может быть пустым, вводные символы должны принадлежать алфавиту
    require_not_null(user_input), require_symbols_in_string(user_input, ALPHABET)

    key = key_input_validation()

    print(f"\nАлфавит: {ALPHABET}")
    print("\n" + DECRYPTION + "\n" + "".join(decrypt(key, user_input, ALPHABET)))

else:
    print("Неизвестный запрос")
