import random
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
punctuation = ["!", "#", "$", "%", "&", "*", "+", "-", "=", "?", "@", "^", "_", "."]
chars = []
print("Сколько паролей хотите создать?")
number_of_passwords = int(input())
print("Какой длины пароль хотите?")
lenth = int(input())
print("Включать ли цифры (0123456789)?")
if input() == "да":
    chars.extend(digits)
print("Включать ли прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)?")
if input() == "да":
    chars.extend(uppercase_letters)
print("Включать ли строчные буквы (abcdefghijklmnopqrstuvwxyz)?")
if input() == "да":
    chars.extend(lowercase_letters)
print("Включать ли символы (!#$%&*+-=?@^_)?")
if input() == "да":
    chars.extend(punctuation)
print("Исключать ли неоднозначные символы (il1Lo0O)?")
special_answer = input()

def generate_password(lenth, number_of_passwords):
    a = []
    for i in range(lenth):
        b = random.choice(chars)
        if special_answer == 'да' and str(b) in 'l1Lo0O':
            continue
        a.append(b)
    return a

for i in range(number_of_passwords):
    print(*generate_password(lenth, number_of_passwords), sep = '')



