from input_validation import require_not_null, require_symbols_in_string, incorrect_user_input


def encrypt(message):
    """
    Алгоритм шифрования.

    Каждая буква шифруется другим алфавитом, включая пробел.
    Первая буква шифруется первым алфавитом, вторая - вторым, третья - третьим, четвёртая - первым и т.д.
    """

    encryption_message = ""
    # Создаётся список из слов без пробела
    text = message.split()
    last = text[-1]

    # Счётчик текущего слова.
    current_number_counter = 0

    # Проход по каждому слова в строке
    for word in text:
        # Добавляем пробел к слову, если оно не последнее
        if word != last:
            word += " "

        current_number_counter += 1

        # Проход по каждому символу слова
        for char in word:
            index = ALPHABET.index(char)

            # Замена символа на символ в соответствующем алфавите
            if current_number_counter % 3 == 1:
                encryption_message += ALPHABET_1[index]

            elif current_number_counter % 3 == 2:
                encryption_message += ALPHABET_2[index]
            elif current_number_counter % 3 == 0:
                encryption_message += ALPHABET_3[index]

            current_number_counter += 1

    return encryption_message


def decrypt(message):
    """
    Алгоритм дешифрования.

    Каждая буква расшифровывается отдельным алфавитом, включая пробел.
    Для условного разделения на слова программа идёт до пробела из алфавита, который используется для
    расшифровки текущего слова.
    """

    decoded_text = ""

    # Счётчик текущего слова
    current_number_counter = 1

    # Проход по всему закодированному сообщению
    for char in message:
        if current_number_counter % 3 == 1:
            index = ALPHABET_1.index(char)
            current_symbol = ALPHABET[index]
            decoded_text += current_symbol

            if current_symbol == " ":
                current_number_counter += 1

        elif current_number_counter % 3 == 2:
            index = ALPHABET_2.index(char)
            current_symbol = ALPHABET[index]
            decoded_text += current_symbol

            if current_symbol == " ":
                current_number_counter += 1

        elif current_number_counter % 3 == 0:
            index = ALPHABET_3.index(char)
            current_symbol = ALPHABET[index]
            decoded_text += current_symbol

            if current_symbol == " ":
                current_number_counter += 1

        current_number_counter += 1
    return decoded_text


def output(phrase="", text=""):
    """
    Форматированный вывод.

    Если в функцию не передаются параметры, то программа выводит все алфавиты.
    Если в функцию передаются параметры, то программа выводит алфавиты, фразу, которая зависит от
    функции, и полученное сообщение.
    """

    if phrase != "" and text != "":
        print("Алфавиты: \n" + "\n" + ALPHABET + "\n" + ALPHABET_1 + "\n" + ALPHABET_2 + "\n" + ALPHABET_3 + "\n" + "\n"
              + "\n" + phrase + text)
    else:
        print("Алфавиты: \n" + "\n" + ALPHABET + "\n" + ALPHABET_1 + "\n" + ALPHABET_2 + "\n" + ALPHABET_3)


ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя .,!0123456789"

ALPHABET_1 = "ЖЗИЙКЛстуфхцчшщМНОПРСабвгмно23456пръыьэюяАБВГДЕЁТУФХЦдеёжзийклЧШЩЪЫЬЭЮЯ .,!01789"
ALPHABET_2 = "9876! ЯЮЭЬЫДГВБАяшевыХФУ543210ТСРПОНМЛКЙИЗЖъщшчцхфутсрпоЪЩШЧЦЁЕнмлкйиз,.жёедгвба"
ALPHABET_3 = "ЙФЯЧЫЦУВС789м,акепитрнГОЁЬБЛШЩДХазэ 0146хъйфячыцу.всМАКЕПИТРНгоьёблшщдюЖЗЭХЪ235!"

ENCRYPTION = "Зашифрованное сообщение: "
DECRYPTION = "Расшифрованное сообщение: "

choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите расшифровать сообщение, введите 2\n"
               "Если Вы хотите вывести алфавиты, введите 3\n>> ")

if choice == "1":
    user_input = input("Введите сообщение, которое хотите зашифровать\nПосле ввода нажмите на Enter\n>> ")

    # Проверка на нулевой ввод и проверка на то, что все введённые символы принадлежат алфавиту
    require_not_null(user_input), require_symbols_in_string(user_input, ALPHABET)
    output(phrase=ENCRYPTION, text=encrypt(user_input))


elif choice == "2":
    user_input = input("Введите сообщение, которое хотите расшифровать\nПосле ввода нажмите на Enter\n>> ")
    # Проверка на нулевой ввод и проверка на то, что все введённые символы принадлежат алфавиту
    require_not_null(user_input), require_symbols_in_string(user_input, ALPHABET)
    output(phrase=DECRYPTION, text=decrypt(user_input))

elif choice == "3":
    output()

else:
    incorrect_user_input()
