""" This code represents rock-paper-scissors game between you and computer"""

from random import randrange

otazka = input("Chceš si zahrát [ano/ne]? ").lower()


while otazka == "ano":

    tah_pocitace = randrange(3)

    if tah_pocitace == 0:
        tah_pocitace = "kámen"

    elif tah_pocitace == 1:
        tah_pocitace = "papír"

    elif tah_pocitace == 2:
        tah_pocitace = "nůžky"

    tah_hrace = input("Vyber si svůj symbol z kámen / nůžky / papír: ")

    if tah_hrace == "kámen" or tah_hrace == "nůžky" or tah_hrace ==  "papír":

        print("Tah hráče:", tah_hrace)
        print("Tah počítače:", tah_pocitace)


        if tah_hrace == "kámen" and tah_pocitace == "papír" or tah_hrace == "nůžky" and tah_pocitace == "kámen" or tah_hrace == "papír" and tah_pocitace == "nůžky":
            print("Prohrál/a jsi!")

        elif tah_hrace == "kámen" and tah_pocitace == "nůžky" or tah_hrace == "nůžky" and tah_pocitace == "papír" or tah_hrace == "papír" and tah_pocitace == "kámen":
            print("Vyhrál/a jsi!")

        else:
            print("Remíza")
    else:
        print("Omlouvám se, znám jen kámen, nůžky nebo papír.")

    print()
    
    otazka = input("Chceš pokračovat [ano/ne]? ").lower()
    
    if otazka == "konec" or otazka == "ne":
        break          
        
    while True:
        if otazka == "ano":
            break
        

print()
print("Hra je u konce.")