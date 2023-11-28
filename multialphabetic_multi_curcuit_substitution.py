from input_validation import require_not_null, require_symbols_in_string, incorrect_user_input


def encrypt(message):
    encryption_message = ""
    text = message.split()
    current_number_counter = 1

    for word in text:
        word += " "
        current_symbol_counter = 0

        if current_number_counter % 3 == 1:
            current_symbol_counter += 1

            for char in word:
                index = ALPHABET.index(char)
                if current_symbol_counter % 3 == 1:
                    encryption_message += ALPHABET_1[index]
                elif current_symbol_counter % 3 == 2:
                    encryption_message += ALPHABET_2[index]
                elif current_symbol_counter % 3 == 0:
                    encryption_message += ALPHABET_3[index]
                current_symbol_counter += 1

            current_number_counter += 1

        elif current_number_counter % 3 == 2:
            current_symbol_counter += 1

            for char in word:
                index = ALPHABET.index(char)
                if current_symbol_counter % 3 == 1:
                    encryption_message += ALPHABET_4[index]
                elif current_symbol_counter % 3 == 2:
                    encryption_message += ALPHABET_5[index]
                elif current_symbol_counter % 3 == 0:
                    encryption_message += ALPHABET_6[index]
                current_symbol_counter += 1

            current_number_counter += 1

        elif current_number_counter % 3 == 0:
            current_symbol_counter += 1

            for char in word:
                index = ALPHABET.index(char)
                if current_symbol_counter % 3 == 1:
                    encryption_message += ALPHABET_7[index]
                elif current_symbol_counter % 3 == 2:
                    encryption_message += ALPHABET_8[index]
                elif current_symbol_counter % 3 == 0:
                    encryption_message += ALPHABET_9[index]
                current_symbol_counter += 1

            current_number_counter += 1

    encryption_message = encryption_message[:-1]
    return encryption_message


def decrypt(message):
    decryption_message = ""
    current_number_counter = 1
    current_symbol_counter = 1

    for char in message:
        if current_number_counter % 3 == 1:
            if current_symbol_counter % 3 == 1:
                index = ALPHABET_1.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            elif current_symbol_counter % 3 == 2:
                index = ALPHABET_2.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            elif current_symbol_counter % 3 == 0:
                index = ALPHABET_3.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            current_symbol_counter += 1

            if decryption_message[-1] == " ":
                current_number_counter += 1
                current_symbol_counter = 1

        elif current_number_counter % 3 == 2:
            if current_symbol_counter % 3 == 1:
                index = ALPHABET_4.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            elif current_symbol_counter % 3 == 2:
                index = ALPHABET_5.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            elif current_symbol_counter % 3 == 0:
                index = ALPHABET_6.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            current_symbol_counter += 1

            if decryption_message[-1] == " ":
                current_number_counter += 1
                current_symbol_counter = 1

        elif current_number_counter % 3 == 0:
            if current_symbol_counter % 3 == 1:
                index = ALPHABET_7.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            elif current_symbol_counter % 3 == 2:
                index = ALPHABET_8.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            elif current_symbol_counter % 3 == 0:
                index = ALPHABET_9.index(char)
                current_symbol = ALPHABET[index]
                decryption_message += current_symbol

            current_symbol_counter += 1

            if decryption_message[-1] == " ":
                current_number_counter += 1
                current_symbol_counter = 1

    return decryption_message


def check_user_input():
    user_input = input("Введите сообщение, которое хотите зашифровать\nПосле ввода нажмите на Enter\n>> ")
    require_not_null(user_input), require_symbols_in_string(user_input, ALPHABET)
    return user_input


def output(phrase="", text=""):
    """
    Форматированный вывод.

    Если в функцию не передаются параметры, то программа выводит все алфавиты.
    Если в функцию передаются параметры, то программа выводит алфавиты, фразу, которая зависит от
    функции, и полученное сообщение.
    """

    if phrase != "" and text != "":
        print("Алфавиты: \n" + ALPHABET + "\n\n" +
              "Контур 1:\n" +
              ALPHABET_1 + "\n" +
              ALPHABET_2 + "\n" +
              ALPHABET_3 + "\n\n" +

              "Контур 2:\n" +
              ALPHABET_4 + "\n" +
              ALPHABET_5 + "\n" +
              ALPHABET_6 + "\n\n" +

              "Контур 3:\n" +
              ALPHABET_7 + "\n" +
              ALPHABET_8 + "\n" +
              ALPHABET_9 + "\n\n" + phrase + text)

    else:
        print("Алфавиты: \n" + ALPHABET + "\n\n" +
              "Контур 1:\n" +
              ALPHABET_1 + "\n" +
              ALPHABET_2 + "\n" +
              ALPHABET_3 + "\n\n" +

              "Контур 2:\n" +
              ALPHABET_4 + "\n" +
              ALPHABET_5 + "\n" +
              ALPHABET_6 + "\n\n" +

              "Контур 3:\n" +
              ALPHABET_7 + "\n" +
              ALPHABET_8 + "\n" +
              ALPHABET_9 + "\n\n")


ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя .,!0123456789"

ALPHABET_1 = "яНсМуэКЗЛЬЯДРьыВШЭлё76б.1мТпГ3ещБ4шЮизУъФдхЪтнЫ8к,ЙХ0СЧ9ж5юф оаОЕйчЩ!ЁАЦ2рЖПИцвг"
ALPHABET_2 = "потГРЛЩ8МАУ5ПЦ47Ыъм29ЁЭа.3ьдфэыс6ё0КжчЯ,ЧцеНхТЙЕяЮЪ ЖОнг1ФДВрювСшиШХлбБ!ЬзкщИуйЗ"
ALPHABET_3 = "АРШ5м!щчНЗЪЯЙкЕЩ,ис0жуло2фзСДЬаЛЁ.цВэП3дйрИёъФ ютбх17Ц6нОЫКеЧХУя9Мь8гГЖЭвТышпЮ4Б"

ALPHABET_4 = "э5няъ3Гг0п4.ща2ХАёсйШМЖЬРОкбКТЩ!ЙтЁСч7иИЧЮрНБ1ьжевЫшЗюЭЦхм,дДц8ф ВЯ6ЪуЛЕФлУ9ыоПз"
ALPHABET_5 = "НРшВуШ4нсъоькУКгЯ0яажЫ!Щ9623рЕГе17БЗиыОлАЁПЬЧщТЛ,85дЖёцХб звфИмЮпйЭ.ЪДтэчФЙюМСЦх"
ALPHABET_6 = "1ЕЭЬИА0ньчЧфтЛ2б6,рюэГЙЩУв!сау.35ВЁОз8л Д7СЖикжпъШКЪРы4НХцПёЗгЫоТФйдЦяБЯщеш9хмМЮ"

ALPHABET_7 = "ПЫдцрБ5,1ЖЪЧ.ГюъЭМЗ4маЮвиЁЙшуНКсхо0кфзпщгЕ ьС2ЯР9ОУ6тэян8йжФеч3ТлХёВ!ыЬЩШ7ИбДАЦЛ"
ALPHABET_8 = "НАтцИЫЖщЕВкЬ2Фф5юеШжомУБДМРнаТб 1Ч8Зв.Ярдчзь,иы3!ОГЮЛЪэ0КягЦъСйЁлХпЙшуПхЭ6Щс7ё94"
ALPHABET_9 = "уиХЛЕёжШЯошЖ07ЭС.ЁЮг9хр6мУЪбАБяМеы1Щ8эЦй!дцщкГКОазВпЬТН3тлФЫчсИ,2 РвфП4ЗД5юЧЙъьн"


ENCRYPTION = "Зашифрованное сообщение: "
DECRYPTION = "Расшифрованное сообщение: "

choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите расшифровать сообщение, введите 2\n"
               "Если Вы хотите вывести алфавиты, введите 3\n>> ")

if choice == "1":
    output(phrase=ENCRYPTION, text=encrypt(check_user_input()))

elif choice == "2":
    output(phrase=DECRYPTION, text=decrypt(check_user_input()))

elif choice == "3":
    output()

else:
    incorrect_user_input()
