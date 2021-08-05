def vyhodnot(retezec):
    """ This function evaluating if some of condition in given string is True and returns relevant symbol. Base for further code of five-in-row"""
    
    if "xxx" in retezec:
        return "x" # x is winner
    elif "ooo" in retezec:
        return "o" # o is winner
    elif "-" not in retezec:
        return "!" # draw
    else:
       return "-" # x or o aren´t in string

for retezec in "----------", "-----xxx----", " -------ooo------", "xoxoxoxoxoxox":

    print(vyhodnot(retezec))