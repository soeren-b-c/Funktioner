
import random


def koef():
    koef = 0
    while koef == 0:
        koef = random.randint(-9, 9)
    return koef

def koef2():
    tilf = random.random()
    if  tilf < 0.1:
        return random.randint(-8, 8)
    elif (tilf < 0.8):
        return random.randint(-4, 4)
    else:
        return 0


def koef_a():
    return random.randint(-2, 3)


def big_koef():
    koef = 0
    while koef == 0:
        koef = random.randint(-99, 99)
    return koef



def andengradspolynomium():
    a = koef()
    while a == 0:
        a = koef_a()
    b = koef()
    c = koef()
    if a == 1:
        ax = "x^2"
    elif a == -1:
        ax = "-x^2"
    else:
        ax = str(a) + "x^2"
    if b == 0:
        bx = ""
    elif b == 1:
        bx = "+x"
    elif b== -1:
        bx = "-x"
    elif b > 0:
        bx = "+" + str(b)+"x"
    else:
        bx = str(b)+"x"
    if c == 0:
        cc = ""
    elif c > 0:
        cc = "+" + str(c)
    else:
        cc = str(c)
    return ax + bx + cc

def mange_andengradspolynomier():
    for int in range(30): # antal her!
        print("\item")
        print("$\qquad")
        print("f(x)=" + andengradspolynomium())
        print("$")


def mange_andengradsligninger():
    for int in range(30): # antal her!
        print("\item")
        print("$\qquad")
        print(andengradsligning())
        print("$")



def tilffunkt():
    liste = ["x", "x^2", "x^7", "e^x", "e^{-3\cdot x}", "x^{-1}", "\sqrt{x}", "\ln(x)", "x^{-5}", "e^{2\cdot x}", "x^{\\frac{1}{2}}", "\\frac{1}{x}"]
    return liste[random.randint(0,len(liste)-1)]


def funktion(): 
    first = True
    streng = ""
    for int in range(random.randint(2,3)):
        k = koef()
        if k > 0 and first:
            if k == 1:
                k = ""
            else:
                k = str(k) + "\cdot "
        else:
            if k > 1:
                k = "+" + str(k) + "\cdot "
            else:
                if k == 1:
                    k = "+"
                else:
                    if k < 0:
                        k = str(k)+"\cdot "
        streng += k + tilffunkt()
        first = False
    if (random.randint(0,10) < 8): #
        konstant = big_koef()
        if konstant > 0:
            konstant = "+" + str(konstant)
        else:
            konstant = str(konstant)
        streng += konstant
    return streng


def mange_funktioner():
    for int in range(1,29):     # Antal elever her
        elevid = "hej"
        if int < 10:
            elevid = "0"+str(int)
        else:
            elevid = str(int)
        print("\item Elev id: 2i " + elevid)
        print("\\begin{enumerate}")
        for i in range(4):      # Antal opgaver pr. elev her
            print("\item ")
            print("$$")
            print("f(x)=" + funktion())
            print("$$")
        print("\end{enumerate}")


def andengradsligning():
    a = koef_a()
    while a == 0:
        a = koef_a()
    r1 = koef2()
    r2 = koef2()

    b = a * (-r1 -r2)
    c = a * r1 * r2
    # uden loesning
    if random.randint(0,10) > 7:
        a = -a
    if a == 1:
        ax = "x^2"
    elif a == -1:
        ax = "-x^2"
    else:
        ax = str(a) + "x^2"
    if b == 0:
        bx = ""
    elif b == 1:
        bx = "+x"
    elif b== -1:
        bx = "-x"
    elif b > 0:
        bx = "+" + str(b)+"x"
    else:
        bx = str(b)+"x"
    if c == 0:
        cc = ""
    elif c > 0:
        cc = "+" + str(c)
    else:
        cc = str(c)
    return "" + ax + bx + cc + "=0"



# Mange differentiable funktioner, med elev-id!
mange_funktioner()

# Mange andengradspolynomier, pa formen f(x)=ax2+bx+c
#mange_andengradspolynomier()

# Mange andengradsligninger pa formen ax2+bx+c=0.
# Nogle uden losning, altsa d<0
#mange_andengradsligninger()


