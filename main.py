import os
import pyfiglet


class bColors:
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


ascii_banner = pyfiglet.figlet_format("Welcome to Imaginary Calculator  by Marko Polo ")


class Main:
    n = True
    global a1, b1, a2, b2

    while n:

        print(bColors.CBLUE, f"{ascii_banner}")

        print(bColors.CYELLOW, '''
                Введіть опцію обрахувння

                1 - Додавання чисел

                2 - Віднімання чисел
                
                3 - Множення чисед
                
                4 - Ділення чисел
                
                5 - Степінь
                
                6 - Вихід
                
        ''')

        enter_opt = int(input("Введіть опцію : "))
        try:
            a1 = int(input("Введіть  a1  : "))
            b1 = int(input("Введіть  b1  : "))
            a2 = int(input("Введіть  a2  : "))
            b2 = int(input("Введіть  b2  : "))
        except ValueError:
            a2 = 0
            b2 = 0

        first_complex_num = complex(a1, b1)
        second_complex_num = complex(a2, b2)

        if enter_opt == 1:
            print(f"Результат : {first_complex_num + second_complex_num}")
        elif enter_opt == 2:
            print(f"Результат : {first_complex_num - second_complex_num}")
        elif enter_opt == 3:
            print(f"Результат : {first_complex_num * second_complex_num}")
        elif enter_opt == 4:
            print(f"Результат : {first_complex_num / second_complex_num}")
        elif enter_opt == 5:
            print(f"Результат : {first_complex_num ** 2}")
        elif enter_opt == 6:
            n = False
            os.system("clear")


if __name__ == '__main__':
    main = Main()
