from input_validation import incorrect_user_input
import random
import struct


def generate_prime():  # Генерация случайного простого числа
    while True:
        p = random.randint(2, 10 ** 6)
        if is_prime(p):
            return p


def is_prime(n):  # Проверка: является ли число простым
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_random_value(first, second):  # Генерация случайного числа
    return random.randint(first, second)


def generate_public_key(p, g, a):  # Вычисление открытого ключа1
    return pow(g, a, p)


# Шифрование сообщения
def encrypt(message, p, g, y):
    result = []
    # print("Представление символов в виде пары чисел c1 и c2:\n Символ\t  c1\t  c2")
    # print('-' * (len(" Символ  c1  c2") + 4 * 2))
    for char in message:
        m = ord(char)  # Получаем числовое представление символа
        k = generate_random_value(2, p - 1)
        c1 = pow(g, k, p)
        c2 = (pow(y, k, p) * m) % p
        # print("   " + char + "\t" + str(c1) + "\t" + str(c2))
        result.append((c1, c2))
    return result


# Дешифрование сообщения
def decrypt(a, p, msg):
    result = ""
    for c1, c2 in msg:
        s = pow(c1, a, p)
        m = (c2 * pow(s, p - 2, p)) % p
        result += chr(m)  # Преобразуем числовое представление обратно в символ
    return result


def save_data_to_file(path, a: int, p: int, pairs):
    with open(path, "wb") as file:
        file.write(struct.pack("i", a))
        file.write(struct.pack("i", p))

        for pair in pairs:
            file.write(struct.pack("ii", pair[0], pair[1]))


def load_data_from_file(path):
    with open(path, "rb") as file:
        a = struct.unpack("i", file.read(4))[0]
        p = struct.unpack("i", file.read(4))[0]
        pairs = []
        while True:
            try:
                c1, c2 = struct.unpack("ii", file.read(8))
                pairs.append((int(c1), int(c2)))
            except struct.error:
                break
    return a, p, pairs


FILE_PATH = r"M:\Data\Projects\PyProjects\Information Security\save encoded message.txt"

choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите расшифровать сообщение, введите 2\n"
               "Если Вы хотите посмотреть сведения о методе шифрование, введите 3\n>>")

if choice == "1":
    p = generate_prime()
    g = generate_random_value(2, p - 1)
    a = generate_random_value(2, p - 2)
    y = generate_public_key(p, g, a)
    print("1 этап: Генерация ключей.\n\n"
          "1) Выбирается случайное простое число p\n"
          f"\tp = {p};\n"
          "2) Выбирается случайное g от 2 до (p - 1)\n"
          f"\tg = {g};\n"
          "3) Выбирается случайное простое а от 2 до (p - 2)\n"
          f"\ta = {a};\n"
          "4) Вычисляется y по формуле y = g^a mod p\n"
          f"\ty = {y}.\n\n"
          "2 этап: Шифрование.\n\n"
          "1) С помощью функции 'ord()' текущий символ представляется в виде числа m;\n"
          "2) Выбирается число k от 2 до (p - 1);\n"
          "3) Считается пара чисел c1 и c2:\n\t\tc1 = g^k mod p;\n\t\tc2 = ((y^k mod p) * m) mod p.\n"
          "Пара чисел c1 и c2 представляют собой зашифрованный вид текущего символа.")
    user_input = input("Введите сообщение, которое хотите зашифровать\n>>")
    encoded_message = encrypt(user_input, p, g, y)
    # print(f"Зашифрованное сообщение:\n{encrypt(user_input, p, g, y)}")
    save_data_to_file(FILE_PATH, a, p, encoded_message)

elif choice == "2":
    print("Расшифрование.\n\n"
          "Чтобы расшифровать сообщение, нужно знать число p и число a.\n"
          "Восстановление зашифрованного символа:\n"
          "\t[Необязательно] 0) В данной программе рассчитывается вспомогательное число s по формуле s = c1^a mod p;\n"
          "\t1) Восстанавливается численное представление символа по формуле m = (c2 * (s^(p - 2) mod p)) mod p;\n"
          "\t2) С помощью функции 'chr()' число m переводится обратно в символ;\n"
          "Далее все символы собираются в строку, которая представляет собой сообщение, "
          "которое было зашифровано.\n")
    # p, a = int(input("Введите p:\n>>")), int(input("Введите a:\n>>"))
    # user_input = eval(input("Введите сообщение в виде списка кортежей, в которых содержится по 2 элемента:\n>>"))
    # print(decrypt(user_input, p, a))
    a, p, msg = load_data_from_file(FILE_PATH)
    print(f"Расшифрованное сообщение: {decrypt(a, p, msg)}")

elif choice == "3":
    print("Общие сведения по шифрованию\n\n"
          "1 этап: Генерация ключей.\n\n"
          "1) Выбирается случайное простое число p\n"
          "2) Выбирается случайное g от 2 до (p - 1)\n"
          "3) Выбирается случайное простое а от 2 до (p - 2)\n"
          "4) Вычисляется y по формуле y = g^a mod p.\n\n"
          "2 этап: Шифрование.\n\n"
          "1) С помощью функции 'ord()' текущий символ представляется в виде числа m;\n"
          "2) Выбирается число k от 2 до (p - 1);\n"
          "3) Считается пара чисел c1 и c2:\n\t\tc1 = g^k mod p;\n\t\tc2 = ((y^k mod p) * m) mod p.\n"
          "Пара чисел c1 и c2 представляют собой зашифрованный вид текущего символа.\n\n"
          "3 этап: Расшифрование.\n\n"
          "Чтобы расшифровать сообщение, нужно знать число p и число a.\n"
          "Восстановление зашифрованного символа:\n"
          "\t[Необязательно] 0) В данной программе рассчитывается вспомогательное число s по формуле s = c1^a mod p;\n"
          "\t1) Восстанавливается численное представление символа по формуле m = (c2 * (s^(p - 2) mod p)) mod p;\n"
          "\t2) С помощью функции 'chr()' число m переводится обратно в символ;\n"
          "Далее все символы собираются в строку, которая представляет собой сообщение, "
          "которое было зашифровано.")

else:
    incorrect_user_input()
