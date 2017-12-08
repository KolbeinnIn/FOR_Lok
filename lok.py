#Kolbeinn og Ágúst
#22.11.2017
#Lokaverkefni í forritun - Pöntun á þjónustu



with open("starfsmenn.txt", "r") as skra:
    skra = skra.read().split("\n")
    malarar = skra[0].split(";")
    piparar = skra[1].split(";")
    rafv = skra[2].split(";")
    smidir = skra[3].split(";")

muppl = []
puppl = []
ruppl = []
suppl = []

for x in malarar:
    a = x.strip().split(",")
    muppl.append(a)

for x in piparar:
    a = x.strip().split(",")
    puppl.append(a)

for x in rafv:
    a = x.strip().split(",")
    ruppl.append(a)

for x in smidir:
    a = x.strip().split(",")
    suppl.append(a)

print(muppl)
print(puppl)
print(ruppl)
print(suppl)
print("")

class Thjonusta:
    def __init__(self, thjonusta):
        self.th = thjonusta

    def malari(self):
        stadfestignargjald = 2000
        litur = self.th[0][0]
        flotur = self.th[0][1]
        a = self.th[4]           #a eru tímakaup vinnumannsinns


        #0.25 af því að það eru 15 mínútur (fjórðungur af klukkustund). Það tekur korter að mála einn fermeter
        if self.th[0][2] == 1:
            if 5 > litur > 0:
                verdL = 150
            else:
                verdL = 100
        else:
            if 5 > litur > 0:
                verdL = 200
            else:
                verdL = 150

        timi = flotur * 0.25
        verd = flotur * verdL
        verd += (timi * int(a[3]))
        vsk = verd * 0.24

        return ("\nMálari:" + str(a[0]) + " " + str(a[1]) + " " + str(a[2]) +
                "\nÞað gera " + str(int(verd)) + "kr" +
                "\nStaðfestingargjald " + str(stadfestignargjald) + "kr" +
                "\nVaskur: " + str(vsk) + "kr" +
                "\nSamtals: " + str(int(vsk + verd + stadfestignargjald)) + "kr")

    def pipari(self):
        asd = "asd2"
        return asd

    def rafv(self):
        asd = "asd3"
        return asd

"""
    def smidur(self):
        inadnout=self.th[3][]
        return ("Það gera " + str(int(verd)) + "kr" +
                "\nStaðfestingargjald " + str(stadfestignargjald) + "kr" +
                "\nVaskur: " + str(vsk) + "kr" +
                "\nSamtals: " + str(int(vsk + verd + stadfestignargjald)) + "kr")
                
"""

#listi[0] = hvað málarinn á að gera
#listi[1] = hvað píparinn á að gera
#listi[2] = hvað rafvirkinn á að gera
#listi[3] = hvað smiðurinn á að gera


listi = [["litur", "stærð veggs/lofts", "loft eða veggur"], #Málari
         ["ákveðið verk", 0], 0, [0, [0, 0, 0], [0, 0, 0]], 0]

teljari2 = 1
verk = 0
k1 = Thjonusta(listi)
asd = True
while asd:
    asd = False
    print("Valmöguleikar:"
          "\nMálari"
          "\nPípari"
          "\nRafvirki"
          "\nSmiður")
    try:
        val = input("Veldu þjónustu: ")
        val = val.lower()

        if val == "malari" or val == "málari" or val == "1":
            teljari = 1
            for x in muppl:
                print(teljari, end=". ")
                teljari2 = 1
                for i in x:
                    print(i, end=" ")
                    if teljari2 == 3:
                        print(" Tímakaup:", end=" ")
                    elif teljari2 == 4:
                        print("kr",end=" ")
                    teljari2 += 1
                print("")
                teljari += 1
            manni = int(input("Veldu málara (1-3): "))
            listi[4] = muppl[manni-1]
            print("1. Veggur/ir"
                  "\n2. Þak")
            while True:
                veggthak = int(input("Veldu 1-2: "))
                if veggthak < 1 or veggthak > 2:
                    print("Rangur innsláttur")
                else:
                    listi[0][2] = veggthak
                    break

            print("\nValmöguleikar:"
                  "\n1. Gulur"
                  "\n2. Rauður"
                  "\n3. Grænn"
                  "\n4. Blár"
                  "\n5. Svartur"
                  "\n6. Hvítur")
            try:
                litur = int(input("Veldu lit: "))
                flotur = float(input("Hversu stór flötur (m²): "))
                listi[0][1] = flotur
                if litur > 6 or litur < 1:
                    raise ValueError("Rangur innsláttur")
                else:
                    listi[0][0] = litur
                    print(k1.malari())

            except ValueError as x:
                print(x)

        elif val == "pipari" or val == "pípari" or val == "2":
            teljari = 1
            for x in puppl:
                print(teljari, end=". ")
                teljari2 = 1
                for i in x:
                    print(i, end=" ")
                    if teljari2 == 3:
                        print(" Tímakaup:", end=" ")
                    elif teljari2 == 4:
                        print("kr", end=" ")
                    teljari2 += 1
                print("")
                teljari += 1
            manni = int(input("Veldu pípara (1-3): "))
            listi[4] = puppl[manni - 1]
            print("\nValmöguleikar:"
                  "\n1. Vaskur"
                  "\n2. Klósett"
                  "\n4. Ofn"
                  "\n5. Sturta/Bað")
            try:
                verk = int(input("Veldu verk (1-5): "))
            except ValueError:
                print("Rangt gagnatak")

            if verk == 1:               #vaskur
                lagnir = input("Þarf að leggja nýjar lagnir fyrir vaskinn (Y/N)? ")
                lagnir = lagnir.lower()
                while True:
                    if lagnir == "y":
                        listi[1][1] = lagnir

                        break
                    elif lagnir == "n":
                        listi[1][1] = lagnir
                        break
                    else:
                        print("Rangur innsláttur")

                listi[1][0] = verk
                k1.pipari()

            elif verk == 2:             #klósett
                lagnir = input("Þarf að leggja nýjar lagnir fyrir klósettið (Y/N)? ")
                lagnir = lagnir.lower()
                while True:
                    if lagnir == "y":
                        listi[1][1] = lagnir

                        break
                    elif lagnir == "n":
                        listi[1][1] = lagnir
                        break
                    else:
                        print("Rangur innsláttur")
                listi[1][0] = verk
                k1.pipari()

            elif verk == 3:             #ofn
                skipta = int(input("1. Skipta um ofn/ofna"
                                   "\n2. Setja upp nýjan ofn"
                                   "\nVeldu (1-2): "))

                if skipta == 1:
                    fjofn = int(input("Fjöldi ofna? "))
                    if fjofn > 0:
                        listi[1][1] = fjofn
                    else:
                        print("Enginn ofn")
                    listi[1][0] = verk
                    k1.pipari()
                elif skipta == 2:
                   asd="asd"
                else:
                    print("Rangur innsláttur")

            elif verk == 4:             #sturta/bað
                lagnir = input("Þarf að leggja nýjar lagnir fyrir sturtuna/baðið (Y/N)? ")
                lagnir = lagnir.lower()
                while True:
                    if lagnir == "y":
                        listi[1][1] = lagnir
                        break
                    elif lagnir == "n":
                        listi[1][1] = lagnir
                        break
                    else:
                        print("Rangur innsláttur")
                listi[1][0] = verk
                k1.pipari()

        elif val == "rafvirki" or val == "3":
            teljari = 1
            for x in ruppl:
                print(teljari, end=". ")
                teljari2 = 1
                for i in x:
                    print(i, end=" ")
                    if teljari2 == 3:
                        print(" Tímakaup:", end=" ")
                    elif teljari2 == 4:
                        print("kr", end=" ")
                    teljari2 += 1
                print("")
                teljari += 1
            manni = int(input("Veldu rafvirkja (1-3): "))
            listi[4] = ruppl[manni - 1]

            print("Valmöguleikar:"
                  "\n1. Skipta um rafmagstöflu"
                  "\n2. Viðgerðir á sambandsleysi í vegg"
                  "\n3. Tengja raftæki við vegg/loft")
            valR = int(input("Veldu (1-3): "))
            if valR == 1:
                staerd = int(input("Sláðu inn stæð hússins í m²: "))
                listi[2][1]

        elif val == "smiður" or val == "smidur" or val == "4":
            teljari = 1
            for x in suppl:
                print(teljari, end=". ")
                teljari2 = 1
                for i in x:
                    print(i, end=" ")
                    if teljari2 == 3:
                        print(" Tímakaup:", end=" ")
                    elif teljari2 == 4:
                        print("kr", end=" ")
                    teljari2 += 1
                print("")
                teljari += 1
            manni = int(input("Veldu smið (1-3): "))
            listi[4] = suppl[manni - 1]
            print("\nValmöguleikar:"
                  "\n1. Utandyra"
                  "\n2. Innandyra")
            try:
                utin = int(input("Veldu annað hvort: "))

                if utin == 1:
                    print("\nValmöguleikar:"
                          "\n1. Þak"
                          "\n2. Gluggar"
                          "\n3. Pallur")
                    utinn = int(input("Veldu verk (1-3): "))
                    if utinn == 1:
                        st = int(input("Hver er stærð þaksins í fermetrum? "))
                        fm = 3200
                        skurt = fm * st
                        print(skurt)
                    elif utinn == 2:
                        fj = int(input("Hversu margir eru gluggarnir? "))
                        teljari = 0
                        jolasveinn = []
                        for x in range(fj):
                            teljari += 1
                            print("--- Gluggi", teljari, "---")
                            ster1 = int(input("Sláðu inn hæð glugga í cm "))
                            ster2 = int(input("Sláðu inn breidd glugga í cm "))
                            ster3 = ster1 * ster2
                            jolasveinn.append(ster3)
                        print(jolasveinn)
                        jolatre = 3000
                        for x in jolasveinn:
                            jolatre = x + jolatre
                        print(jolatre)

                    elif utinn == 3:
                        pall = int(input("Sláðu inn stærð palls í fermetrum "))
                        vegg = input("Viltu vegg? J/N").upper()
                        if vegg == "J":
                            ha = int(input("Hversu hár á hann að vera? "))
                            qwert=ha*15000
                            vallur=qwert+(pall*2500)
                        else:
                            vallur=pall*2500
                        print(vallur)
                    else:
                        print("Rangur innsláttur")

                elif utin == 2:
                    print("\nValmöguleikar:"
                          "\n1. Veggur"
                          "\n2. Innrétting"
                          "\n3. Gólf")
                    utinn = int(input("Veldu verk (1-3): "))
                    if utinn == 1:
                        bubbi = int(input("Brjóta eða byggja vegg (1-2): "))
                        if bubbi == 1:
                            skurtskurt = 0
                            fj = int(input("Hversu margir eru veggirnir? "))
                            for x in range(fj):
                                skurtskurt=x*500+skurtskurt
                                skurtskurt=skurtskurt+8000
                            skurtskurt+=5000
                            print(skurtskurt)
                        elif bubbi == 2:
                            fj = int(input("Hversu margir eru veggirnir? "))
                            teljari = 0
                            jolasvein = []
                            for x in range(fj):
                                teljari += 1
                                print("--- Veggur", teljari, "---")
                                sterd = int(input("Sláðu inn stærð veggs í fermetrum "))
                                jolasvein.append(sterd)
                            skurtskurt = 0
                            for x in jolasvein:
                                skurtskurt=x*1000+skurtskurt
                                skurtskurt=skurtskurt+8000
                            print(skurtskurt)
                        else:
                            print("Rangur innsláttur")
                    elif utinn == 2:
                        print("Staðsetning:"
                              "\n1. Eldhúsið"
                              "\n2. Baðherberginu")
                        berg = int(input(">>"))
                        if berg == 1:
                            kost = 150000
                        elif berg == 2:
                            kost = 200000
                        else:
                            print("Rangur innsláttur")
                        print(kost)
                    elif utinn == 3:
                        jolakotturinn = int(input("Stærð gólfs í fermetrum: "))
                        jolakotturinn=jolakotturinn*5000
                        print(jolakotturinn)

                    else:
                        print("Rangur innsláttur")
            except:
                print("Rangur innsláttur")
        else:
            raise ValueError("Rangt gagnatak")

    except ValueError as x:
        print(x, "\n")
        pass
        asd = True