from random import randrange

herni_radek = "-" * 20

def vyhodnot(herni_radek):
    """ This function evaluating if some of condition in given string is True and returns relevant symbol."""
    
    if "xxx" in herni_radek:
        return "x"
    elif "ooo" in herni_radek:
        return "o"
    elif "-" not in herni_radek:
        return "!"
    else:
       return "-"

def tah(herni_radek, pozice, symbol):
    """This function returns X or O symbol and add them to row"""
    
    return herni_radek[:pozice] + symbol + herni_radek[pozice+1:]

def tah_hrace(herni_radek):
    """This function return players turn"""
    
    while True:
        pozice = input("Zadej pozici, kam chceš umístit x: ")
        try:
            symbol = "x"

            pozice = int(pozice)
            if pozice < 0 or pozice > len(herni_radek)-1:
                print("Zadal jsi pozici mimo herní pole.")
            elif herni_radek[pozice] != "-":
                print("Toto pole je již obsazeno, zadej jiné")
            else:
                return tah(herni_radek, pozice, symbol)
        except ValueError:
            print("Nezadal/a jsi správnou hodnotu!")


def tah_pocitace(herni_radek):
    """This function return computers turn"""
   
    while True:
        symbol = "o"
        pozice = randrange(0, 20)
        if herni_radek[pozice] != "-":
            False
        else:
            return tah(herni_radek, pozice, symbol)
            return herni_radek


def piskvorky1d(herni_radek):
    """This function loads turns of player and computer , evaluates them a show the output to user."""
    
    while True:
        herni_radek = tah_hrace(herni_radek)
        kolo = herni_radek.count("x") + herni_radek.count("o")
        print(f"{kolo}. kolo:", herni_radek)
        print(vyhodnot(herni_radek))

        if vyhodnot(herni_radek) == "x" or vyhodnot(herni_radek) == "o"  or vyhodnot(herni_radek) == "!":
            break

        herni_radek = tah_pocitace(herni_radek)
        kolo = herni_radek.count("x") + herni_radek.count("o")
        print(f"{kolo}. kolo:", herni_radek)
        print(vyhodnot(herni_radek))

        if vyhodnot(herni_radek) == "x" or vyhodnot(herni_radek) == "o" or vyhodnot(herni_radek) == "!":
            break
        
piskvorky1d(herni_radek)