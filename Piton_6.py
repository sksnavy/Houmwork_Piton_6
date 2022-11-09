# Задача №1: Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Задача №2: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# Задача №3: Создайте программу для игры в "Крестики-нолики".

# Задача №4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах. 


print ('Введите номер задания (1-4): ')
n = int (input ())

if n==1: # № 1

    delete_abc = lambda st: " ".join( list ( filter ( lambda i: 'абв' not in i, st.split())) )

    print ('Введите слово: ')
    st = input ()
    if st == '':
        st = 'абв Hello word!'
        print (st+'->')
    
    print( delete_abc (st) )

elif n==2: # № 2

    from random import randint

    def ch_konf (name, n_konf): # Определение количества конфет
        print (f"{name}, ведите количество конфет, которое возьмете (1-{n_konf}): ")
        ch = int (input ())
        while ch < 1 or ch > n_konf:
            print (f"{name}, не будьте таким жадным. Введите количество конфет, которое возьмете (1-{n_konf}): ")
            ch = int (input ())
        return ch

    def ch_konf_komp (konf, n_konf): # Сколько конфет возьмет комп
        ch = konf  % ( n_konf + 1 )   
        return ch
        
    def play_game (hum): 
        print ("Введите количество конфет: ")
        konf = int (input ())
        print ("Введите максимальное количество конфет, которое можно взять: ")
        n_konf = int (input ())            

        if hum: # Человек против человека
            print ("Игра человека против человека")
            print ("Введите имя первого человека: ")
            hum_1 = input ()
            print ("Введите имя второго человека: ")
            hum_2 = input ()
            
        else: # Игра против компьютера   
            print ("Игра человека против компьютера")
            print ("Введите имя человека: ")
            hum_1 = input ()
            hum_2 = 'Компьютер'
            
        one = randint (0,2)  # кто первый берет конфеты
    
        if one:
            print(f"Ходит {hum_1}")
        else:
            print(f"Ходит {hum_2}")

        ch1 = 0 
        ch2 = 0
        while konf > 0:
            if one:
                n = ch_konf (hum_1, n_konf)
                ch1 = ch1 + n
                konf = konf - n
                one = False
                print (f"Первый игорк взял {n} конфет. В сумме у него {ch1}. Осталось {konf} конфет.")
            else:
                if hum:
                    n = ch_konf (hum_2, n_konf)
                else:
                    n = ch_konf_komp (konf, n_konf)
                
                ch2 = ch2 + n
                konf = konf - n
                one = True
                if hum:    
                    st1="Второй игрок" 
                else:
                    st1="Компьютер"
                
                print (f"{st1} взял {n} конфет. В сумме у него {ch2}. Осталось {konf} конфет.")    

        if one:
            print (f"Выиграл {hum_2}")
        else:
            print (f"Выиграл {hum_1}")

    print ("Выберите тип игры: 1-человек с человеком, иначе-человек с компьютером: ")
    if (int(input ())==1):
        play_game (True)
    else:
        play_game (False)    

elif n==3: # №3
    
    x0 = list ( range (1,10) )

    def ris_pole ( x0 ): # Рисуем поле
        
        for i in range (3):
            print ("|", x0 [ 0+i*3 ], "|", x0 [ 1+i*3 ], "|", x0 [ 2+i*3 ], "|")
            
    def hod ( x1 ): # Определение параметров хода
       
       yes = False
       while not yes:
            num = input ("Введите номер клетки (1-9), " + x1 +": ")
            try:
                num = int ( num )
            except:
                print ("Неверно. Введите номер клетки (1-9) в виде целого числа, " + x1 +": ")
                continue

            if num >= 1 and num <= 9:
                
                if ( str ( x0 [ num-1 ]) not in "X0"):
                    print ("Ход принят")
                    x0 [ num-1 ] = x1
                    yes = True
                else:
                    print ("Клетка занята")
            else:
                print ("Номер клетки должен быть от 1 до 9, " + x1 +": ")

    def opr_pobeda ( x0 ): # Определение состояния победы

        pobeda_num = ( (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6) )
        for i in pobeda_num:
            if x0 [i[0]] == x0 [i[1]] == x0 [i[2]]:
                return x0 [i[0]]
        return False

    def play (x0): # Основное тело игры
        ch = 0
        pobeda = False

        while not pobeda:

            ris_pole (x0)
            if ch % 2 == 0:
                hod ("X")
            else:
                hod ("0")
            ch = ch + 1
            
            if ch > 4:
                
                if opr_pobeda ( x0 ):
                    print (opr_pobeda ( x0 ), "выиграл!")
                    pobeda = True
                    break

            if ch == 9:
                print ("Ничья")
                break

        ris_pole (x0)

    play (x0)

elif n==4: # №4

    def sjat ( st ):
        ch = 1
        st1 = ''

        for i in range (len ( st ) - 1):
            if st [i] == st [i+1]:
                ch = ch +1
            else:
                st1 = st1 + str (ch) + st [i]
                ch = 1

        if ch > 1 or ( st [len (st)-2] != st [-1]):
            st1 = st1 + str (ch) + st [-1]
        return st1

    def razvernut ( st ):
        st1 = ''
        st2 = ''
        for i in range (len ( st )):
            if not st [i].isalpha():
                st1 += st [i]
            else:
                st2 = st2 + st [i] * int (st1)
                st1 = ''
        return st2

    st = 'WWWWWWWWWWNNNNNNNNNSSSSSSS'
    with open ('text.txt', 'w', encoding='utf-8') as file:
        file.write (st)
    
    print (f"Исходный текст: {st}")
    
    st1 = sjat (st)
    print (f"Текст после сжатия: {st1}")
    with open ('text_sjat.txt', 'w', encoding='utf-8') as file:
        file.write (st1)
    
    st2 = razvernut (st1)
    print (f"Текст после разворачивания: {st2}")
    with open ('text_razvernut.txt', 'w', encoding='utf-8') as file:
        file.write (st2)

else:
    print ('Номер задания должен быть от 1 до 4 !!!')


