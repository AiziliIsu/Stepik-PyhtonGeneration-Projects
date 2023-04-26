import random
print("Добро пожаловать в числовую угадайку! Хоите угадать згаданную компьютером цифру? Тогда...")
print()
print("Прочтите единственное условие: У вас есть 80сом (за один неправильный ответ у вас забирают 20сом), но после того как денег не отсанется за каждый неправильный ответ вам беспощадно отрубят палец. А теперь, поехали!")
def wishing_game():
    print("Компьютер загадал цифру...")
    number = random.randint(1, 100)
    money = 80
    attempts = 10
    while True:
        wish_number = input("Выберите любое число от 1 до 100: ")
        if is_valid(wish_number) == True:
            if int(wish_number) > number:
                print("Слишком много, попробуйте еще раз")
                if money>0:
                    money -= 20
                    print("Теперь у вас осталось", money, "сом")
                else:
                    attempts -= 1
                    print("Вам отрубят палец...Теперь у вас осталось", attempts, "пальцев")
            elif int(wish_number) < number:
                print("Слишком мало, попробуйте еще раз")
                if money>0:
                    money -= 20
                    print("Теперь у вас осталось", money, "сом")
                else:
                    attempts -= 1
                    print("Вам отрубят палец...Теперь у вас осталось", attempts, "пальцев")
            else:
                print("Вы угадали, поздравляем!", "У вас", attempts, "оставшихся пальцев на руках:", sep = '\n')
                print("Хотите поиграть еще раз?", "Если да, введите - да. Если нет, введите - нет")
                answer = input()
                if "нет" == answer:
                    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                    if attempts == 10:
                        print("Вы молодец, вам удалось сохранить все пальцы")
                    else:
                        print(" сожалению игра не обошлась без кровопалитий, теперь у вас", attempts, "пальцев")
                    break
        else:
            print("А может быть все-таки введем целое число в пределах установленной границы?")

def is_valid(wish_number):
    if 1 <= int(wish_number) <= 100:
        return True
    else:
        return False
wishing_game()


