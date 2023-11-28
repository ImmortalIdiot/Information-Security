"""
Данная программа шифрует сообщение по методу Виженера.

Ключ вводит пользователь с клавиатуры.
"""

from input_validation import require_not_null, require_symbols_in_string, incorrect_user_input


def encrypt(alphabet, text, unique):  # Данная функция шифрует сообщение по принципу Виженера,
    # используя базовый алфавит и ключ, который вводит пользователь с клавиатуры

    alphabet_length = len(alphabet)
    unique_length = len(unique)
    encryption_message = []
    unique_index = 0

    for c in text:
        unique_letter = unique[unique_index % unique_length]  # Получаем текущий символ ключа
        shift = alphabet.find(unique_letter)  # Определяем вертикальное смещение
        encryption_message.append(
            alphabet[(alphabet.find(c) + shift) % alphabet_length])  # кодируем символ тем символом, который получился
        # при пересечении текущей буквы сообщения и текущего символа ключа

        unique_index += 1  # Переход к следующему символу слова

    return encryption_message


def decrypt(alphabet, text, unique):  # Данная функция расшифровывает сообщение по принципу Виженера,
    # используя базовый алфавит и ключ, который пользователь вводит с клавиатуры

    alphabet_length = len(alphabet)
    unique_length = len(unique)
    decryption_message = []
    unique_index = 0

    for c in text:
        unique_letter = unique[unique_index % unique_length]  # Получаем текущий символ ключа
        shift = alphabet.find(unique_letter)  # Определяем вертикальное смещение
        decryption_message.append(
            alphabet[(alphabet.find(c) - shift) % alphabet_length])  # раскодируем символ тем символом, который стоит
        # в вертикальном смещении (то есть у нас есть текущий символ сообщения и символ, полученный в результате
        # пересечения текущего символа сообщения и смещения, исходя из этих данных находим символ смещения)

        unique_index += 1  # Переход к следующему символу слова

    return decryption_message


"""
Функция для вывода всех используемых алфавитов.
Выводятся те алфавиты, в которых символ ключа стоит на первом месте.
Например, алфавит "012345" и ключ "502". Здесь будет выведено 3 алфавита:
    1: "501234";
    2: "012345";
    3: "234501".
"""


def print_alphabets(alphabet, word):
    print("Исходный алфавит:\n" + alphabet + "\n")
    unique = ""
    for i in word:
        if not (i in unique):
            unique += i

    unique_length = len(unique)
    for i in range(unique_length):
        print(alphabet[alphabet.index(unique[i]):] + alphabet[:alphabet.index(unique[i])])
    print()


ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя .,0123456789!"
ENCRYPTION = "Зашифрованное сообщение: "
DECRYPTION = "Расшифрованное сообщение: "

choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите расшифровать сообщение, введите 2\n"
               "Если Вы хотите вывести алфавиты, введите 3\n>> ")

if choice == "1":
    user_input = input("Введите сообщение >> ")
    require_not_null(user_input), require_symbols_in_string(user_input, ALPHABET)
    key = input("Введите ключ >> ")
    require_not_null(key)

    print_alphabets(ALPHABET, key)
    print(ENCRYPTION + "".join(encrypt(ALPHABET, user_input, key)) + "\n")

elif choice == "2":
    user_input = input("Введите сообщение >> ")
    require_not_null(user_input), require_symbols_in_string(user_input, ALPHABET)
    key = input("Введите ключ >> ")
    require_not_null(key)

    print_alphabets(ALPHABET, key)
    print(DECRYPTION + "".join(decrypt(ALPHABET, user_input, key)))

elif choice == "3":
    print(f"Исходный алфавит:\n{ALPHABET}")

else:
    incorrect_user_input()
