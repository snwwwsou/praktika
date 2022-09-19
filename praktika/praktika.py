def sym(key, stroka):
    if len(stroka) % len(key) != 0:
        for i in range(len(key) - (len(stroka) % len(key))):
            stroka += str("*")
    a = ''
    b = ''
    for i in range(0, len(stroka), len(key)):
        a = [stroka[i + j] for j in range(len(key))]
        for j in range(len(key)):
            b += a[key[j]]
    print(b)

def rsym(key, stroka):
        a = ''
        b = ''
        for i in range(0, len(stroka), len(key)):
            a = [stroka[i + j] for j in range(len(key))]
            for j in range(len(key)):
                 b += a[key[j]]
        b = b.replace("*", "")
        print (b)


def gr(key, stroka):
    grgr = int(input("kolvo simvolov\n"))
    w = [stroka[i:i + grgr] for i in range(0, len(stroka), grgr)]
    if len(w[-1]) != grgr:
        for i in range(grgr - (len(w[-1]) % grgr)):
            w[-1] += str("*")
    if len(w) != len(key):
        for i in range(len(key) - (len(w) % len(key))):
            w.append("*" * grgr)
    a = ''
    b = ''
    for i in range(0, len(w), len(key)):
        a = [w[i + j] for j in range(len(key))]
        for j in range(len(key)):
            b += a[key[j]]
    print (b)

def rgr(key, stroka):
    grgr = int(input("kolvo simvolov\n"))
    w = [stroka[i:i + grgr] for i in range(0, len(stroka), grgr)]
    a = ''
    b = ''
    for i in range(0, len(w), len(key)):
        a = [w[i + j] for j in range(len(key))]
        for j in range(len(key)):
            b += a[key[j]]
    print(b)

def slov(key, stroka):
    if len(stroka.split(" ")) != len(key):
        for i in range(len(key) - (len(stroka.split(" ")) % len(key))):
            stroka.split(" ").append("*" * 5)
    a = ''
    b = ''
    for i in range(0, len(stroka.split(" ")),len(key)):
        a = [stroka.split(" ")[i + j] for j in range(len(key))]
        for j in range(len(key)):
            b += a[key.index(j)]
            b += " "
    print(b)

def rslov(key, stroka):
    a = ''
    b = ''
    for i in range(0, len(stroka.split()), len(key)):
        a = [stroka.split()[i + j] for j in range(len(key))]
        for j in range(len(key)):
            b += a[key[j]]
            b += " "
    b = b.replace("*", "")
    print(b)

def shifr():
    key = []
    stroka = input("vvedite text\n")
    klyuch = input("vvedite klyuch\n"
                  "primer - [1 0 3 2])\n")

    gotoviiklyuch = klyuch.split()
    for f in gotoviiklyuch:
        key.append(int(f))
    sposob = int(input("sposob shifra\n"
                    "'1' - simvol\n"
                    "'2' - gruppa\n"
                    "'3' - slovo\n"))
    if sposob == 1:
        sym(key, stroka)
    if sposob == 2:
        gr(key, stroka)
    if sposob == 3:
        slov(key, stroka)

def rasshifr():
    key = []
    stroka = input("vvedite text\n")
    klyuch = input("vvedite klyuch\n"
                  "(primer - [1 0 3 2])\n")
    gotoviiklyuch = klyuch.split()
    for f in gotoviiklyuch:
        key.append(int(f))
    sposob = int(input("sposob rasshifra\n"
                    "'1' - simvol\n"
                    "'2' - gruppa\n"
                    "'3' - slovo\n"))
    if sposob == 1:
        rsym(key, stroka)
    if sposob == 2:
        rgr(key, stroka)
    if sposob == 3:
        rslov(key, stroka)

def privet():
    a = int(input("shifr - '1', rasshifr - '2'\n"))
    if a == 1:
        shifr()
    if a == 2:
        rasshifr()
start = True

while start:
    privet()
    start = False
