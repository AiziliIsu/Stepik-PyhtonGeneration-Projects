direction = input("шифрование или дешифрование?").strip()
key = int(input("шаг сдвига (со сдвигом вправо?)").strip())
letter = list(input())

def decryption(letter, key):
    for i in range(len(letter)):
        num = ord(letter[i])
        if 65 <= num <= 90:
            if num + key <= 90:
                letter[i] = chr((num + key) % 91)
            else:
                letter[i] = chr(65 + ((num + key) % 91))

        elif 97 <= num <= 122:
            if num + key <= 90:
                letter[i] = chr((num + key) % 123)
            else:
                letter[i] = chr(97 + (num + key) % 123)
    return "".join(letter)

def encryption(letter, key):
    for i in range(len(letter)):
            num = ord(letter[i])
            if 65 <= num <= 90:
                if num + key <= 90:
                    letter[i] = chr((num+key)%91)
                else:
                    letter[i] = chr(65+((num + key) % 91))

            elif 97 <= num <= 122:
                if num + key <= 90:
                    letter[i] = chr((num+key)%123)
                else:
                    letter[i] = chr(97+(num + key) % 123)


    return "".join(letter)

if direction == "шифрование":
    print(encryption(letter, key))
else:
    print(decryption(letter, key))
