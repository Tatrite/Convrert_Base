from tkinter import *


def dec_to_bin(nb):
# La Fonction dec_to_bin convertit un entier naturel de décimal à binaire
# Paramètres : nb - Entier - IN - L'entier naturel donné en base 10
# Retour : Chaîne de caractères - L'entier naturel nb représenté en base 2
# Précondition : nb est un entier positif ou nul exprimé en notation positionnelle base 10
# Postcondition : La valeur renvoyée est une chaîne de caractères contenant
# la représentation du nombre nb en notation positionnelle base 2 
        sr = ""
        while nb > 0:
            b = nb//2
            c = nb%2
            nb = b
            if c == 0:
                sr = "0"+sr
            else:
                sr = "1"+sr
        return(sr)




def dec_to_hex(nb):
        # La Fonction dec_to_hex convertit un entier naturel de décimal à hexadécimal
# Paramètres : nb - Entier - IN - L'entier naturel donné en base 10
# Retour : Chaîne de caractères - L'entier naturel nb représenté en base 16
# Précondition : nb est un entier positif ou nul exprimé en notation positionnelle base 10
# Postcondition : La valeur renvoyée est une chaîne de caractères contenant
# la représentation du nombre nb en notation positionnelle base 16
        sr = ""
        while nb>0:
            b = nb//16
            c = nb%16
            nb = b
            if c == 0:
                sr = "0"+sr
            else:
                if c < 10:
                    y = str(c)
                else:
                    if c == 10:
                        y = "A"
                    elif c == 11:
                        y = "B"
                    elif c == 12:
                        y = "C"
                    elif c == 13:
                        y = "D"
                    elif c == 14:
                        y = "E"
                    elif c == 15:
                        y = "F"
                sr = y+sr
        return(sr)





def bin_to_dec(nb):
# La Fonction bin_to_dec convertit un entier naturel de binaire à décimal
# Paramètres : nb - Chaîne de caractères - IN - L'entier naturel donné en base 2
# Retour : Entier - L'entier naturel nb représenté en base 10
# Précondition : nb est une chaîne de caractères contenant un entier positif ou nul
# exprimé en notation positionnelle base 2
# Postcondition : La valeur renvoyée est la valeur du nombre nb en notation positionnelle base 10
    c=len(nb)
    f=c-1
    h=0
    for i in range(c):
        g=nb[i]
        g=int(g)
        h=(2**f)*g+h
        f=f-1
    return(h)





def hex_to_dec(nb):
    # La Fonction hex_to_dec convertit un entier naturel de hexadécimal à décimal
# Paramètres : nb - Chaîne de caractères - IN - L'entier naturel donné en base 16
# Retour : Entier - L'entier naturel nb représenté en base 10
# Précondition : nb est une chaîne de caractères contenant un entier positif ou nul
# exprimé en notation positionnelle base 16
# Postcondition : La valeur renvoyée est la valeur du nombre nb en notation positionnelle base 10
    c=len(nb)
    f=c-1
    h=0
    for i in range(c):
        g=nb[i]
        g=convert_digit_from_hex_to_dec(g)
        h=(16**f)*g+h
        f=f-1
    return(h)



def convert_digit_from_hex_to_dec(car):
    # La Fonction convert_digit_from_hex_to_dec convertit un chiffre hexadécimal en décimal
# Paramètres : car - Chaîne de caractères - IN - Le chiffre donné en base 16
# Retour : Entier - L'entier naturel car représenté en base 10
# Précondition : car est une chaîne de caractères contenant un seul chiffre hexadécimal
# Postcondition : La valeur renvoyée est la valeur du nombre car en base 10
    if car=="A":
        car=10
    elif car=="B":
        car=11
    elif car=="C":
        car=12
    elif car=="D":
        car=13
    elif car=="E":
        car=14
    elif car=="F":
         car=15
    else:
        car=int(car)
    return (car)







def bin_to_hex(nb):
    # La Fonction bin_to_hex convertit un entier naturel de binaire à hexadécimal
# Paramètres : nb - Chaîne de caractères - IN - L'entier naturel donné en base 2
# Retour : Chaîne de caractères - L'entier naturel nb représenté en base 16
# Précondition : nb est une chaîne de caractères contenant un entier positif ou nul
# exprimé en notation positionnelle base 2
# Postcondition : La valeur renvoyée est une chaîne de caractères contenant
# la représentation du nombre nb en notation positionnelle base 16
    nb=bin_to_dec(nb)
    nb=dec_to_hex(nb)
    return(nb)







def hex_to_bin(nb):
    # La Fonction hex_to_bin convertit un entier naturel de hexadécimal à binaire
# Paramètres : nb - Chaîne de caractères - IN - L'entier naturel donné en base 16
# Retour : Chaîne de caractères - L'entier naturel nb représenté en base 2
# Précondition : nb est une chaîne de caractères contenant un entier positif ou nul
# exprimé en notation positionnelle base 16
# Postcondition : La valeur renvoyée est une chaîne de caractères contenant
# la représentation du nombre nb en notation positionnelle base 2
    nb=hex_to_dec(nb)
    nb=dec_to_bin(nb)
    return(nb)





def oct_to_dec(nb):
    c=len(nb)
    f=c-1
    h=0
    for i in range(c):
        g=nb[i]
        g=int(g)
        h=(8**f)*g+h
        f=f-1
    return(h)

def dec_to_oct(nb):
        sr = ""
        while nb > 0:
            b = nb//8
            c = nb%8
            nb = b
            sr = str(c)+sr
        return(sr)


def oct_to_bin(nb):
    nb=oct_to_dec(nb)
    nb=dec_to_bin(nb)
    return(nb)

def bin_to_oct(nb):
    nb=bin_to_dec(nb)
    nb=dec_to_oct(nb)
    return(nb)

def oct_to_hex(nb):
    nb=oct_to_dec(nb)
    nb=dec_to_hex(nb)
    return(nb)

def hex_to_oct(nb):
    nb=hex_to_dec(nb)
    nb=dec_to_oct(nb)
    return(nb)







def choix_base(base):
    #Opérations effectuées lors d'un changement de base
    #(clic sur un des 3 boutons de choix de la base)
    global base_courante
    if base == 16:
        base_courante = 16
        # Application des couleurs dans les 3 boutons
        B_Hex.config(fg = "white", width = 6)
        B_Dec.config(fg = "black", width = 5)
        B_Bin.config(fg = "black", width = 5)
        B_Oct.config(fg = "black", width = 5)
        B_2.config(bg = "grey")
        B_3.config(bg = "grey")
        B_4.config(bg = "grey")
        B_5.config( bg = "grey")
        B_6.config( bg = "grey")
        B_7.config( bg = "grey")
        B_8.config( bg = "grey")
        B_9.config( bg = "grey")
        B_A.config( bg = "grey")
        B_B.config( bg = "grey")
        B_C.config( bg = "grey")
        B_D.config( bg = "grey")
        B_E.config( bg = "grey")
        B_F.config( bg = "grey")

        # Effacement du texte des 3 labels
        L_Hex.config(text = "")
        L_Dec.config(text = "")
        L_Bin.config(text = "")
        L_Oct.config(text = "")
    elif base == 10:
        base_courante = 10
        # Application des couleurs dans les 3 boutons
        B_Hex.config(fg = "black", width = 5)
        B_Dec.config(fg = "white", width = 6)
        B_Bin.config(fg = "black", width = 5)
        B_Oct.config(fg = "black", width = 5)
        B_2.config(bg = "grey")
        B_3.config(bg = "grey")
        B_4.config(bg = "grey")
        B_5.config( bg = "grey")
        B_6.config( bg = "grey")
        B_7.config( bg = "grey")
        B_8.config( bg = "grey")
        B_9.config( bg = "grey")
        B_A.config( bg = "black")
        B_B.config( bg = "black")
        B_C.config( bg = "black")
        B_D.config( bg = "black")
        B_E.config( bg = "black")
        B_F.config( bg = "black")
        # Effacement du texte des 3 labels
        L_Hex.config(text = "")
        L_Dec.config(text = "")
        L_Bin.config(text = "")
        L_Oct.config(text = "")
    elif base == 8:
        base_courante = 8
        # Application des couleurs dans les 3 boutons
        B_Hex.config(fg = "black", width = 5)
        B_Dec.config(fg = "black", width = 5)
        B_Bin.config(fg = "black", width = 5)
        B_Oct.config(fg = "white", width = 6)
        B_2.config(bg = "grey")
        B_3.config(bg = "grey")
        B_4.config(bg = "grey")
        B_5.config( bg = "grey")
        B_6.config( bg = "grey")
        B_7.config( bg = "grey")
        B_8.config( bg = "black")
        B_9.config( bg = "black")
        B_A.config( bg = "black")
        B_B.config( bg = "black")
        B_C.config( bg = "black")
        B_D.config( bg = "black")
        B_E.config( bg = "black")
        B_F.config( bg = "black")

        # Effacement du texte des 3 labels
        L_Hex.config(text = "")
        L_Dec.config(text = "")
        L_Bin.config(text = "")
        L_Oct.config(text = "")
    elif base == 2:
        base_courante = 2
        # Application des couleurs dans les 3 boutons
        B_Hex.config(fg = "black", width = 5)
        B_Dec.config(fg = "black", width = 5)
        B_Bin.config(fg = "white", width = 6)
        B_Oct.config(fg = "black", width = 5)
        B_2.config(bg = "black")
        B_3.config(bg = "black")
        B_4.config(bg = "black")
        B_5.config( bg = "black")
        B_6.config( bg = "black")
        B_7.config( bg = "black")
        B_8.config( bg = "black")
        B_9.config( bg = "black")
        B_A.config( bg = "black")
        B_B.config( bg = "black")
        B_C.config( bg = "black")
        B_D.config( bg = "black")
        B_E.config( bg = "black")
        B_F.config( bg = "black")
        # Effacement du texte des 3 labels
        L_Hex.config(text = "")
        L_Dec.config(text = "")
        L_Bin.config(text = "")
        L_Oct.config(text = "")


def ecrire(nb):
    #Écriture des caractères lors de l'appui sur un bouton de l'interface
    modifie = False

    if base_courante == 16:
        Label = L_Hex
        modifie = True
    elif base_courante == 10:
        if "0" <= nb <= "9":
            Label = L_Dec
            modifie = True
    elif base_courante == 8:
        if "0" <= nb <= "7":
            Label = L_Oct
            modifie = True
    elif base_courante == 2:
        if "0" <= nb <= "1":
            Label = L_Bin
            modifie = True

    if modifie:
        Label.config(text = Label.cget("text") + nb)


def ecrire2(event, nb):
    #Écriture des caractères lors de l'appui sur une touche appropriée du clavier
    ecrire(nb)


def convertir():
    #Écriture des résultats lors de l'appui sur le bouton '='

    if base_courante == 16:
        if L_Hex.cget("text") != "":
            nb = L_Hex.cget("text")
            nb10 = hex_to_dec(nb)
            L_Dec.config(text = str(nb10))
            nb2 = hex_to_bin(nb)
            L_Bin.config(text = str(nb2))
            nb8 = hex_to_oct(nb)
            L_Oct.config(text = str(nb8))
    elif base_courante == 10:
        if L_Dec.cget("text") != "":
            nb = L_Dec.cget("text")
            nb16 = dec_to_hex(int(nb))
            L_Hex.config(text = nb16)
            nb2 = dec_to_bin(int(nb))
            L_Bin.config(text = nb2)
            nb8 = dec_to_oct(int(nb))
            L_Oct.config(text = str(nb8))

    elif base_courante == 8:
        if L_Oct.cget("text") != "":
            nb = L_Oct.cget("text")
            nb16 = oct_to_hex(nb)
            L_Hex.config(text = nb16)
            nb2 = oct_to_bin(nb)
            L_Bin.config(text = nb2)
            nb10 = oct_to_dec(nb)
            L_Dec.config(text = str(nb10))
    elif base_courante == 2:
        if L_Bin.cget("text") != "":
            nb = L_Bin.cget("text")
            nb16 = bin_to_hex(nb)
            L_Hex.config(text = nb16)
            nb10 = bin_to_dec(nb)
            L_Dec.config(text = str(nb10))
            nb8 = bin_to_oct(nb)
            L_Oct.config(text = str(nb8))


def convertir2(event):
    #Écriture des résultats lors de l'appui sur la touche '=' du clavier
    convertir()

def AC2():
    AC()

def AC():
    L_Hex.config(text = "")
    L_Dec.config(text = "")
    L_Bin.config(text = "")
    L_Oct.config(text = "")
def DEL2():
    DEL()

def DEL():
    if base_courante==2:
        nb=L_Bin.cget("text")
        L_Dec.config(text = nb[:-1])
    elif base_courante==8:
        nb=L_Oct.cget("text")
        L_Dec.config(text = nb[:-1])
    elif base_courante==10:
        nb=L_Dec.cget("text")
        L_Dec.config(text = nb[:-1])
    elif base_courante==16:
        nb=L_Hex.cget("text")
        L_Dec.config(text = nb[:-1])

# Programme principal
base_courante = 10

# Création de la fenêtre
fen = Tk()
fen.title("Calculatrice")
fen.geometry("400x400")
fen.configure(bg='black')

# Création des widgets
B_Hex = Button(fen, text = "HEX", width = 5, font="Arial, 14", bg = "grey", command = lambda base = 16:choix_base(base))
B_Dec = Button(fen, text = "DEC", width = 6, font="Arial, 14", bg = "grey", fg = "white", command = lambda base = 10:choix_base(base))
B_Bin = Button(fen, text = "BIN", width = 5, font="Arial, 14", bg = "grey", command = lambda base = 2:choix_base(base))
B_Oct = Button(fen, text = "OCT", width = 5, font="Arial, 14", bg = "grey", command = lambda base = 8:choix_base(base))

L_Hex = Label(fen, font = "Arial, 14", bg = "black", fg = "white")
L_Dec = Label(fen, font = "Arial, 14", bg = "black", fg = "white")
L_Bin = Label(fen, font = "Arial, 14", bg = "black", fg = "white")
L_Oct = Label(fen, font = "Arial, 14", bg = "black", fg = "white")

B_0 = Button(fen, text = "0", width = 12, font = "Arial, 12", bg = "grey", command = lambda nb = "0":ecrire(nb))
B_1 = Button(fen, text = "1", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "1":ecrire(nb))
B_2 = Button(fen, text = "2", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "2":ecrire(nb))
B_3 = Button(fen, text = "3", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "3":ecrire(nb))
B_4 = Button(fen, text = "4", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "4":ecrire(nb))
B_5 = Button(fen, text = "5", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "5":ecrire(nb))
B_6 = Button(fen, text = "6", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "6":ecrire(nb))
B_7 = Button(fen, text = "7", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "7":ecrire(nb))
B_8 = Button(fen, text = "8", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "8":ecrire(nb))
B_9 = Button(fen, text = "9", width = 3, font = "Arial, 12", bg = "grey", command = lambda nb = "9":ecrire(nb))
B_A = Button(fen, text = "A", width = 3, font = "Arial, 12", bg = "black", command = lambda nb = "A":ecrire(nb))
B_B = Button(fen, text = "B", width = 3, font = "Arial, 12", bg = "black", command = lambda nb = "B":ecrire(nb))
B_C = Button(fen, text = "C", width = 3, font = "Arial, 12", bg = "black", command = lambda nb = "C":ecrire(nb))
B_D = Button(fen, text = "D", width = 3, font = "Arial, 12", bg = "black", command = lambda nb = "D":ecrire(nb))
B_E = Button(fen, text = "E", width = 3, font = "Arial, 12", bg = "black", command = lambda nb = "E":ecrire(nb))
B_F = Button(fen, text = "F", width = 3, font = "Arial, 12", bg = "black", command = lambda nb = "F":ecrire(nb))
B_Egal = Button(fen, text = "=", width = 7, font = "Arial, 12", bg = "grey", command = convertir)
B_AC = Button(fen, text = "AC", width = 8, font = "Arial, 12", bg = "grey", command = AC)
B_DEL = Button(fen, text = "<=", width = 8, font = "Arial, 12", bg = "grey", command = DEL)

# Positionnement des widgets dans la fenêtre
B_Hex.place(x = 10, y = 10, anchor = "nw")
B_Dec.place(x = 10, y = 60, anchor = "nw")
B_Bin.place(x = 10, y = 160, anchor = "nw")
B_Oct.place(x = 10, y = 110, anchor = "nw")

L_Hex.place(x = 90, y = 15, anchor = "nw")
L_Dec.place(x = 90, y = 65, anchor = "nw")
L_Bin.place(x = 90, y = 165, anchor = "nw")
L_Oct.place(x = 90, y = 115, anchor = "nw")

B_0.place(x = 10, y = 360, anchor = "nw")
B_Egal.place(x = 134, y = 360, anchor = "nw")
B_AC.place(x = 250, y = 290, anchor = "nw")
B_DEL.place(x = 250, y = 230, anchor = "nw")
B_1.place(x = 10, y = 325, anchor = "nw")
B_2.place(x = 50, y = 325, anchor = "nw")
B_3.place(x = 90, y = 325, anchor = "nw")
B_4.place(x = 10, y = 290, anchor = "nw")
B_5.place(x = 50, y = 290, anchor = "nw")
B_6.place(x = 90, y = 290, anchor = "nw")
B_7.place(x = 10, y = 255, anchor = "nw")
B_8.place(x = 50, y = 255, anchor = "nw")
B_9.place(x = 90, y = 255, anchor = "nw")
B_A.place(x = 130, y = 325, anchor = "nw")
B_B.place(x = 170, y = 325, anchor = "nw")
B_C.place(x = 130, y = 290, anchor = "nw")
B_D.place(x = 170, y = 290, anchor = "nw")
B_E.place(x = 130, y = 255, anchor = "nw")
B_F.place(x = 170, y = 255, anchor = "nw")

# Gestion des touches du clavier
fen.bind("0", lambda event, nb = "0":ecrire2(event, nb))
fen.bind("1", lambda event, nb = "1":ecrire2(event, nb))
fen.bind("2", lambda event, nb = "2":ecrire2(event, nb))
fen.bind("3", lambda event, nb = "3":ecrire2(event, nb))
fen.bind("4", lambda event, nb = "4":ecrire2(event, nb))
fen.bind("5", lambda event, nb = "5":ecrire2(event, nb))
fen.bind("6", lambda event, nb = "6":ecrire2(event, nb))
fen.bind("7", lambda event, nb = "7":ecrire2(event, nb))
fen.bind("8", lambda event, nb = "8":ecrire2(event, nb))
fen.bind("9", lambda event, nb = "9":ecrire2(event, nb))
fen.bind("A", lambda event, nb = "A":ecrire2(event, nb))
fen.bind("B", lambda event, nb = "B":ecrire2(event, nb))
fen.bind("C", lambda event, nb = "C":ecrire2(event, nb))
fen.bind("D", lambda event, nb = "D":ecrire2(event, nb))
fen.bind("E", lambda event, nb = "E":ecrire2(event, nb))
fen.bind("F", lambda event, nb = "F":ecrire2(event, nb))
fen.bind("a", lambda event, nb = "A":ecrire2(event, nb))
fen.bind("b", lambda event, nb = "B":ecrire2(event, nb))
fen.bind("c", lambda event, nb = "C":ecrire2(event, nb))
fen.bind("d", lambda event, nb = "D":ecrire2(event, nb))
fen.bind("e", lambda event, nb = "E":ecrire2(event, nb))
fen.bind("f", lambda event, nb = "F":ecrire2(event, nb))
fen.bind("<Return>", lambda event:convertir2(event))
fen.bind("!", lambda event:AC2())
fen.bind("<BackSpace>", lambda event:DEL2())

# Lancement de la surveillance de la fenêtre
fen.mainloop()
