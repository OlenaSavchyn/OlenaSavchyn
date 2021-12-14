
def shifrrr(mss):
    alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    krok = -3
    result = ""
    for i in mss:
        mes = alfavit.find(i)
        nwmes = mes + krok
        if i in alfavit:
            result += alfavit[nwmes]
        else:
            result += i
    return  result