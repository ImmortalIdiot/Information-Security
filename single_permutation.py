from math import ceil
from input_validation import require_not_null, incorrect_user_input


def laboratory_work():
    print("Лабораторная работа №5 'Простая перестановка'")


def encrypt(key_index_to_real_index: dict, number_of_columns: int, number_of_rows: int, encrypted_str: str) -> str:
    encryption_message = ""

    # Кодирование всей строки по таблицам (запуск цикла на необходимое количество таблиц)
    for tab_index in range(ceil(len(encrypted_str) / (number_of_columns * number_of_rows))):
        code_table = [["" for _ in range(number_of_columns)] for _ in range(number_of_rows)]
        column_counter = 0
        row_counter = 0

        # Проход по кодируемой строке (блок размером с таблицу или меньше) и заполнение таблицы
        for encrypted_symbol in encrypted_str[
                tab_index * (number_of_columns * number_of_rows):(
                tab_index + 1) * (number_of_columns * number_of_rows)]:

            code_table[row_counter][column_counter] = encrypted_symbol
            column_counter += 1
            if column_counter == number_of_columns:
                row_counter += 1
                column_counter = 0

        # # Вывод таблицы и ключа
        # print(" ", "    ".join(str(key_index + 1) for key_index in key_index_to_real_index.keys()))
        # print(*code_table, sep="\n")
        # print()

        # Исходя из таблицы, происходит заполнение строки шифром по столбцам
        for column_index in sorted(key_index_to_real_index.keys()):
            encryption_message += "".join([row_list[key_index_to_real_index[column_index]] for row_list in code_table])

    return encryption_message


def decrypt(key_index_to_real_index: dict, number_of_columns: int, number_of_rows: int, encrypted_str: str) -> str:
    decryption_message = ""

    # Декодируем всю строку по таблицам (запуск цикла на необходимое кол-во таблиц)
    for tab_index in range(ceil(len(encrypted_str) / (number_of_columns * number_of_rows))):
        code_table = [["" for _ in range(number_of_columns)] for _ in range(number_of_rows)]
        column_counter = 0

        # Определение шифра на текущую таблицу путём обрезки
        block_encrypted_str = encrypted_str[tab_index * (number_of_columns * number_of_rows):(
                                            tab_index + 1) * (number_of_columns * number_of_rows)]

        # Нахождение количества полностью заполненных строк и столбцов
        filed_rows = ceil(len(block_encrypted_str) / number_of_columns)
        filed_cols = len(block_encrypted_str) % number_of_columns
        all_column_list = []
        if len(block_encrypted_str) < number_of_columns * number_of_rows:

            # Если текущей части шифра не хватает на заполнение всей таблицы - заполняется то, что можно заполнить
            for column_index in range(number_of_columns):

                # Заполнение новый столбец
                column_str = ""
                counter = 0
                while True:

                    # Если последняя строка была только что заполнена, то программа переходит к следующему столбцу
                    if counter == filed_rows:
                        break

                    # Если только что была заполнена предпоследняя строка, но в текущем столбце
                    # последняя строка не полная, то программа также переходит к следующему столбцу

                    if counter == filed_rows - 1 and key_index_to_real_index[column_index] + 1 > filed_cols:
                        break

                    # в противном случае происходит добавление символа в текущий столбец
                    # с последующим удалением его из текущей части шифра
                    column_str += block_encrypted_str[0]
                    block_encrypted_str = block_encrypted_str[1:]
                    counter += 1

                all_column_list.append(column_str)
        else:

            # Если текущей части шифра хватает на заполнение всей таблицы, то происходит заполнение списка столбцов
            for current_row in range(0, len(block_encrypted_str), number_of_rows):
                column_str = ""
                for row_index in range(number_of_rows):
                    column_str += block_encrypted_str[current_row + row_index]

                all_column_list.append(column_str)

        # Заполнение таблицы из списка столбцов
        for column_list in all_column_list:
            for row_counter in range(number_of_rows):
                if row_counter < len(column_list):
                    code_table[row_counter][key_index_to_real_index[column_counter]] = column_list[row_counter]
            column_counter += 1

        # # Вывод таблицы и ключа сверху
        # print(" ", "    ".join(str(key_index + 1) for key_index in key_index_to_real_index.keys()))
        # print(*code_table, sep="\n")
        # print()

        # Исходя из таблицы, происходит заполнение строки дешифровки
        for row_list in code_table:
            for column in row_list:
                decryption_message += column

    return decryption_message


def get_is_correct_key(number_of_columns: int) -> dict:
    """
    Валидация ключа:
    1) Количество цифр ключа должно совпадать с количеством столбцов;
    2) Ключ должен содержать только цифры и знаки тире, причём знаков тире должно быть ровно на 1 меньше, чем цифр;
    3) Ключ не должен содержать число 0 и числа, превышающие количество столбцов.

    Гарантируется, что функция вернёт абсолютно верный ключ.
    """
    def check_key(verifiable_key: str):  # Проверка ключа на 1 условие
        column_list = []
        help_key = verifiable_key.split("-")
        for char in help_key:
            if not (char in column_list):
                column_list.append(char)
        if len(help_key) == len(column_list):
            return True
        else:
            return False

    def num_of_digits_in_string(s: str):  # Подсчёт цифр в строке
        counter = 0
        for c in s:
            if c.isdigit():
                counter += 1
        return counter

    while True:
        hint = ""
        for i in range(1, number_of_columns + 1):
            hint += f"{i}-"
        hint = hint[:-1]

        key_text = input("Введите ключ шифрования.\n"
                         f"Формат ввода ключа для {number_of_columns} столбцов: {hint}\n"
                         f"Вы можете использовать любые комбинации из этих чисел\n>> ")
        key_without_dash = key_text.split("-")

        if ((len(key_without_dash) != number_of_columns or
                not all(key_char.isdigit() for key_char in key_without_dash) or
                not all(0 < int(key_char) <= number_of_columns for key_char in key_without_dash)) or
                not check_key(key_text)) or not (num_of_digits_in_string(key_text) - key_text.count("-") == 1):

            print("Неверный ключ.\n"
                  "Введите ключ шифрования.\n"
                  "Ключ должен содержать только числа и знаки '-'\n"
                  "Между числами, содержащимися в ключе, должны стоять символы '-'. Например, 2-1-3\n"
                  f"Каждое число ключа не должно превышать количество столбцов\n"
                  "Количество чисел в ключе, записанных через знак '-', "
                  "должно быть строго равно количеству столбцов.\n>> "
                  f"(Подсказка: формат ввода ключа для {number_of_columns} столбцов: {hint})\n>> ")
            continue

        key_list = [int(key_char) for key_char in key_without_dash]
        key_index_to_real_index = {}
        real_index = 0
        for index in key_list:
            key_index_to_real_index[index - 1] = real_index
            real_index += 1
        return key_index_to_real_index


def get_is_correct_column():
    """
    Валидация столбцов:
    1) Количество столбцов должно быть натуральным числом;
    2) Количество столбцов должно быть больше 1.

    Гарантируется, что функция возвращает абсолютно верное количество столбцов.
    """
    n = input("Введите количество столбцов для размера блока шифрования (ввод должен быть натуральным числом) >> ")
    while not (n.isnumeric() and int(n) > 0):
        n = input("Некорректный ввод количества столбцов\n"
                  "Введите количество столбцов для размера блока шифрования "
                  "Подсказка: введите натуральное число (0 не входит)\n>> ")

    return int(n)


def get_is_correct_row():
    """
    Валидация строк:
    1) Количество строк должно быть натуральным числом;
    2) Количество строк должно быть больше 1.

    Гарантируется, что функция возвращает абсолютно верное количество столбцов.
    """
    m = input("Введите количество строк для размера блока шифрования (ввод должен быть натуральным числом) >> ")
    while not (m.isnumeric() and int(m) > 0):
        m = input("Некорректный ввод количества строк\n"
                  "Введите количество строк для размера блока шифрования "
                  "Подсказка: введите натуральное число (0 не входит)\n>> ")

    return int(m)


ENCRYPTION = "Зашифрованное сообщение: "
DECRYPTION = "Расшифрованное сообщение: "

laboratory_work()
choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите расшифровать сообщение, введите 2\n>> ")

if choice == '1':
    user_input = input("Введите сообщение >> ")
    require_not_null(user_input)

    columns, rows = get_is_correct_column(), get_is_correct_row()
    key = get_is_correct_key(columns)

    print(ENCRYPTION + encrypt(key, columns, rows, user_input))
elif choice == '2':
    user_input = input("Введите сообщение >> ")
    require_not_null(user_input)

    columns, rows = get_is_correct_column(), get_is_correct_row()
    key = get_is_correct_key(columns)

    print(DECRYPTION + decrypt(key, columns, rows, user_input))

else:
    incorrect_user_input()
