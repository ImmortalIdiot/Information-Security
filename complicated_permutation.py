from input_validation import require_not_null, incorrect_user_input


def laboratory_work():
    print("Лабораторная работа №6 'Перестановка, усложнённая по таблице'")


def encrypt(key_index_to_real_index: dict, number_of_columns: int, number_of_rows: int, encrypted_str: str,
            unavailable_cells: list) -> str:
    encryption_message = ""

    # Кодирование всей строки по таблицам (запуск цикла на необходимое количество таблиц)
    while True:
        code_table = [['' for _ in range(number_of_columns)] for _ in range(number_of_rows)]

        for unavailable_cell in unavailable_cells:
            code_table[unavailable_cell[1]][unavailable_cell[0]] = '~'

        column_counter, row_counter = 0, 0
        # Проход по кодируемой строке (блок размером с таблицу или меньше) и заполнение таблицы
        while True:
            if code_table[row_counter][column_counter] != '~':
                code_table[row_counter][column_counter] = encrypted_str[0]
                encrypted_str = encrypted_str[1:]
                if not encrypted_str:
                    break

            if column_counter == number_of_columns - 1 and row_counter == number_of_rows - 1:
                break

            column_counter += 1
            if column_counter == number_of_columns:
                row_counter += 1
                column_counter = 0

        # # Вывод таблиц
        # print(" ", "    ".join(str(key_index + 1) for key_index in key_index_to_real_index.keys()))
        # print(*code_table, sep='\n')
        # print()
        # for unavailable_cell in unavailable_cells:
        #     code_table[unavailable_cell[1]][unavailable_cell[0]] = ''

        # Исходя из таблицы, заполняется строка шифра по столбцам
        for col_index in sorted(key_index_to_real_index.keys()):
            encryption_message += ''.join([row_list[key_index_to_real_index[col_index]] for row_list in code_table])
        if not encrypted_str:
            break

    return encryption_message


def decrypt(key_index_to_real_index: dict, number_of_columns: int, number_of_rows: int, encrypted_str: str,
            unavailable_cells: list) -> str:
    decryption_message = ""
    # Декодируем всю строку по таблицам (запускаем цикл на необходимое кол-во таблиц
    while True:
        decode_table = [['' for _ in range(number_of_columns)] for _ in range(number_of_rows)]
        for unavailable_cell in unavailable_cells:
            decode_table[unavailable_cell[1]][unavailable_cell[0]] = '~'

        if len(encrypted_str) < number_of_columns * number_of_rows - len(unavailable_cells):
            column_counter, row_counter = 0, 0
            test_table = [['' for _ in range(number_of_columns)] for _ in range(number_of_rows)]

            for unavailable_cell in unavailable_cells:
                test_table[unavailable_cell[1]][unavailable_cell[0]] = '~'
            counter = len(encrypted_str)

            while True:
                if test_table[row_counter][column_counter] != '~':
                    test_table[row_counter][column_counter] = '_'
                    counter -= 1
                    if counter == 0:
                        break
                column_counter += 1
                if column_counter == number_of_columns:
                    row_counter += 1
                    column_counter = 0

            empty_place_in_columns = []
            print(*test_table, sep='\n')
            print(empty_place_in_columns, sep='\n')

            for column_index in range(number_of_columns):
                empty_place_in_columns.append(len(['' for column_list in test_table
                                                   if column_list[column_index] == '_']))

        else:
            empty_place_in_columns = [number_of_rows for _ in range(number_of_columns)]

        column_counter, row_counter = 0, 0
        # Проходимся по кодируемой строке (блок размером с таблицу или меньше) и заполняем табличку
        while True:
            # Иначе добавляем символ в нашу таблицу и удаляем его из текущего куска шифра
            if decode_table[row_counter][key_index_to_real_index[column_counter]] != '~':
                decode_table[row_counter][key_index_to_real_index[column_counter]] = encrypted_str[0]
                encrypted_str = encrypted_str[1:]
                if not encrypted_str:
                    break

            if column_counter == number_of_columns - 1 and row_counter == number_of_rows - 1:
                break

            row_counter += 1
            if (row_counter == number_of_rows or row_counter + 1 >
                    empty_place_in_columns[key_index_to_real_index[column_counter]]):
                column_counter += 1
                row_counter = 0

        # # Вывод таблиц
        # print(' ', '    '.join(str(key_index + 1) for key_index in key_index_to_real_index.keys()))
        # print(*decode_table, sep='\n')
        # print()

        for unavailable_cell in unavailable_cells:
            decode_table[unavailable_cell[1]][unavailable_cell[0]] = ''

        for row_list in decode_table:
            for column in row_list:
                decryption_message += column
        if not encrypted_str:
            break

    return decryption_message


def get_is_correct_number_of_columns():
    """
    Валидация столбцов:
    1) Количество столбцов должно быть натуральным числом;
    2) Количество столбцов должно быть больше 1.

    Гарантируется, что функция возвращает абсолютно верное количество столбцов.
    """
    n = input("Введите количество столбцов для размера блока шифрования (ввод должен быть натуральным числом) >> ")
    while not (n.isnumeric() and int(n) > 1):
        n = input("Некорректный ввод количества столбцов\n"
                  "Введите количество столбцов для размера блока шифрования "
                  "Подсказка: введите натуральное число (0 не входит)\n>> ")

    return int(n)


def get_is_correct_number_of_rows():
    """
    Валидация строк:
    1) Количество строк должно быть натуральным числом;
    2) Количество строк должно быть больше 1.

    Гарантируется, что функция возвращает абсолютно верное количество столбцов.
    """
    m = input("Введите количество строк для размера блока шифрования (ввод должен быть натуральным числом) >> ")
    while not (m.isnumeric() and int(m) > 1):
        m = input("Некорректный ввод количества строк\n"
                  "Введите количество строк для размера блока шифрования "
                  "Подсказка: введите натуральное число (0 не входит)\n>> ")

    return int(m)


def get_is_correct_key(number_of_columns: int) -> dict:
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

        if ((len(key_without_dash) != number_of_columns or not all(
                key_char.isdigit() for key_char in key_without_dash) or not all(
            0 < int(key_char) <= number_of_columns for key_char in key_without_dash)) or not check_key(
            key_text)) or not (num_of_digits_in_string(key_text) - key_text.count("-") == 1):
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


def get_unavailable_cells(number_of_columns: int, number_of_rows: int) -> list:
    cell_num = input('Введите количество пустых ячеек: ')

    while not (cell_num.isnumeric() and 1 <= int(cell_num) < number_of_columns * number_of_rows):
        if cell_num.isnumeric():
            print('Вы ввели не корректное число (число должно быть больше 0, но меньше кол-ва ячеек в таблице)')
        else:
            print('Вы ввели не число (число должно состоять только из цифр)')
        cell_num = input('Введите количество пустых ячеек: ')
    unavailable_cells = []

    print('Введите координаты пустых ячеек\n(Формат: 1 1, где первая цифра - номер строки, вторая - номер столбца)\n'
          'Каждая пара координат должна вводиться с новой строки.')

    for cell in range(int(cell_num)):
        cell_row, cell_column = [*input(str(cell + 1) + ") >> ").split(), '', ''][:2]

        while not (cell_column.isnumeric() and 1 <= int(
                cell_column) <= number_of_columns and cell_row.isnumeric() and 1 <= int(cell_row) <= number_of_rows):

            if cell_column.isnumeric() and not (1 <= int(cell_column) <= number_of_columns):
                print(f'Вы ввели некорректное число столбцов (число должно быть больше 0 и меньше числа столбцов: '
                      f'{number_of_columns})')
            elif cell_row.isnumeric() and not (1 <= int(cell_row) <= number_of_rows):
                print(f'Вы ввели некорректное число строк (число должно быть больше 0 и меньше общего числа строк: '
                      f'{number_of_rows})')
            else:
                print('Некорректный ввод. Ожидается ввод чисел')
            cell_row, cell_column = [*input(str(cell + 1) + ") >> ").split(), '', ''][:2]
        unavailable_cells.append((int(cell_column) - 1, int(cell_row) - 1))
    return unavailable_cells


ENCRYPTION = "Зашифрованное сообщение: "
DECRYPTION = "Расшифрованное сообщение: "

laboratory_work()
choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите расшифровать сообщение, введите 2\n>> ")

if choice == "1":
    user_input = input("Введите сообщение >> ")
    require_not_null(user_input)

    columns, rows = get_is_correct_number_of_columns(), get_is_correct_number_of_rows()
    key = get_is_correct_key(columns)
    unavailable_cells_list = get_unavailable_cells(columns, rows)
    print(ENCRYPTION + encrypt(key, columns, rows, user_input, unavailable_cells_list))

elif choice == "2":
    user_input = input("Введите сообщение >> ")
    require_not_null(user_input)

    columns, rows = get_is_correct_number_of_columns(), get_is_correct_number_of_rows()
    key = get_is_correct_key(columns)
    unavailable_cells_list = get_unavailable_cells(columns, rows)

    print(DECRYPTION + "Красуля Максим Дмитриевич")
    print(DECRYPTION + decrypt(key, columns, rows, user_input, unavailable_cells_list))

else:
    incorrect_user_input()
