from input_validation import incorrect_user_input
import random


def generate_prime():  # Генерация случайного простого числа
    while True:
        p = random.randint(2, 10**6)
        if is_prime(p):
            return p


def is_prime(n):  # Проверка: является ли число простым
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_private_key(p):  # Генерация случайного числа
    return random.randint(2, p - 1)


def generate_public_key(p, g, a):  # Вычисление открытого ключа
    return pow(g, a, p)


# Шифрование сообщения
def encrypt(message, p, g, y):
    result = []
    for char in message:
        m = ord(char)  # Получаем числовое представление символа
        k = generate_private_key(p)
        c1 = pow(g, k, p)
        c2 = (pow(y, k, p) * m) % p
        print(char + " - " + str(c1) + " " + str(c2))
        result.append((c1, c2))
    return result


# Дешифрование сообщения
def decrypt(msg, p, a):
    result = ""
    for c1, c2 in msg:
        s = pow(c1, a, p)
        m = (c2 * pow(s, p - 2, p)) % p
        result += chr(m)  # Преобразуем числовое представление обратно в символ
    return result


choice = input("Если Вы хотите зашифровать сообщение, введите 1\n"
               "Если Вы хотите расшифровать сообщение, введите 2\n>>")

if choice == "1":
    user_input = input("Введите сообщение, которое хотите зашифровать\n>>")
    p = generate_prime()
    g = random.randint(2, p - 1)
    a = generate_private_key(p)
    y = generate_public_key(p, g, a)
    print(f"Ключ (число a): {str(a)}\nЧисло p: {p}\n{encrypt(user_input, p, g, y)}")

elif choice == "2":
    p, a = int(input("Введите p:\n>>")), int(input("Введите a:\n>>"))
    user_input = eval(input("Введите сообщение в виде списка кортежей, в которых содержится по 2 элемента:\n>>"))
    print(decrypt(user_input, p, a))

else:
    incorrect_user_input()
