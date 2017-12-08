# Kolbeinn og Ágúst
# 22.11.2017
# Lokaverkefni í forritun - Pöntun á þjónustu



with open("starfsmenn.txt", "r") as skra:
    skra = skra.read().split("\n")
    malarar = skra[0].split(";")
    piparar = skra[1].split(";")
    rafv = skra[2].split(";")
    smidir = skra[3].split(";")

# fyrsti stafur vinnu + uppl fyrir upplýsingar
muppl = []
puppl = []
ruppl = []
suppl = []

# Hér eru for lykkjur sem bæta verktökum í viðeigandi lista
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


class Thjonusta:
    def __init__(self, thjonusta):
        self.th = thjonusta

    def malari(self):
        stadfestignargjald = 2000
        litur = self.th[0][0]
        flotur = self.th[0][1]
        a = self.th[4]  # a eru upplýsingarnar um verktakann


        # 0.25 af því að það eru 15 mínútur (fjórðungur af klukkustund). Það tekur korter að mála einn fermeter
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
        verd += (timi * int(a[3]))  # a[3] eru tímakaup verktakans
        vsk = verd * 0.24

        return ("\nMálari: " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]) +
                "\nÞað gera " + str(int(verd)) + "kr" +
                "\nStaðfestingargjald " + str(stadfestignargjald) + "kr" +
                "\nVaskur: " + str(vsk) + "kr" +
                "\nSamtals: " + str(int(vsk + verd + stadfestignargjald)) + "kr")

    def pipari(self):
        a = self.th[4]
        uppl = self.th[1]

        verd = 0
        timi = 0
        if uppl[0] == 1:  # Vaskur
            uppsetning = 10000
            verd += uppsetning
            timi = 2
            if uppl[1] == "y":
                verd += 50000
                timi += 10  # klst
            if uppl[2] == 1:
                verd += 9950
            elif uppl[2] == 2:
                verd += 22950
            elif uppl[2] == 3:
                verd += 72850


        elif uppl[0] == 2:  # Klósett
            uppsetning = 13000
            verd += uppsetning
            timi = 2
            if uppl[1] == "y":
                verd += 50000
                timi += 12  # klst
            if uppl[2] == 1:
                verd += 22950
            elif uppl[2] == 2:
                verd += 35950
            elif uppl[2] == 3:
                verd += 72850
        elif uppl[0] == 3:  # Ofn
            uppsetning = 7000
            verd += uppsetning
            timi = 0.75  #45 min
            fjofna = uppl[2]
            print(uppl)
            timi = timi * fjofna
            if uppl[1] == 1:   #Skipta um ofna
                verd = verd * fjofna
            else:              #Setja lagnir og setja upp nýjan ofn
                lagnir = fjofna * 50000
                verd = verd * fjofna
                verd += lagnir


        elif uppl[0] == 4:
            if uppl[1] == "y":      #Nýjar lagnir
                verd += 50000
                timi += 12  # klst

            if uppl[2] == 1:        #Bað
                timi += 6
                if uppl[2] == 1:        #Ódýrt bað
                    verd += 25950
                elif uppl[2] == 2:      #Gott bað á góðu verði
                    verd += 39950
                elif uppl[2] == 3:      #Lúxus bað
                    verd += 74950


            elif uppl[2] == 2:      #Sturta
                timi += 5
                if uppl[2] == 1:        #Ódýr sturta
                    verd += 34950
                elif uppl[2] == 2:      #Góð sturta á góðu verði
                    verd += 44950
                elif uppl[2] == 3:      #Lúxus sturta
                    verd += 54950


        timakaup = timi * int(a[3])
        vsk = verd * 0.24               #virðisaukaskattur er bætt við verð, ekki tímakaup
        verd = verd + timakaup

        if vsk == 0:
            return "Eitthvað fór úrskeiðis"
        else:
            return ("\nPípari: " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]) +
                    "\nÞað gera " + str(int(verd)) + "kr" +
                    "\nVirðisaukaskattur: " + str(vsk) + "kr" +
                    "\nSamtals: " + str(int(vsk + verd)) + "kr")

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

# listi[0] = hvað málarinn á að gera
# listi[1] = hvað píparinn á að gera
# listi[2] = hvað rafvirkinn á að gera
# listi[3] = hvað smiðurinn á að gera


listi = [["litur", "stærð veggs/lofts", "loft eða veggur"],  # Málari
         ["ákveðið verk", "Nýjar lagnir eða ekki / skipta eða setja nýja ofna", "tegund vöru", "sturta eða bað"], #Pípari
         0,  # Rafvirki
         [0, [0, 0, 0], [0, 0, 0]],  # Smiður
         0]  # Upplýsignar um verktaka

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

            # Á milli '#' eru for lykkjur sem sýna valkosti og upplýsingar um verktaka, sama hvað notandi velur (nenni ekki að commena fyrir hvert einasta)
            #####################################################################
            teljari = 1
            for x in muppl:
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
            #####################################################################

            while True:
                manni = int(input("Veldu pípara (1-3): "))
                if manni == 1 or manni == 2 or manni == 3:
                    listi[4] = puppl[manni - 1]
                    break
                else:
                    print("Rangur innsláttur")
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
            #####################################################################
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
            #####################################################################
            while True:
                manni = int(input("Veldu pípara (1-3): "))
                if manni == 1 or manni == 2 or manni == 3:
                    listi[4] = puppl[manni - 1]
                    break
                else:
                    print("Rangur innsláttur")
            print("\nValmöguleikar:"
                  "\n1. Vaskur"
                  "\n2. Klósett"
                  "\n3. Ofn"
                  "\n4. Sturta/Bað")
            try:
                verk = int(input("Veldu verk (1-5): "))
            except ValueError:
                print("Rangt gagnatak")

            if verk == 1:  # vaskur
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
                while True:
                    smancy = int(input("\n1. Ódýr vaskur"
                                       "\n2. Góður vaskur á góðu verði"
                                       "\n3. Lúxus vaskur"
                                       "\nVeldu (1-3): "))
                    if smancy == 1 or smancy == 2 or smancy == 3:
                        listi[1][2] = smancy
                        break
                    else:
                        print("Rangur innsláttur")

                listi[1][0] = verk

            elif verk == 2:  # klósett
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
                while True:
                    smancy = int(input("\n1. Ódýrt klósett"
                                       "\n2. Gott klósett á góðu verði"
                                       "\n3. Lúxus klósett"
                                       "\nVeldu (1-3): "))
                    if smancy == 1 or smancy == 2 or smancy == 3:
                        listi[1][2] = smancy
                        break
                    else:
                        print("Rangur innsláttur")
                listi[1][0] = verk

            elif verk == 3:  # ofn
                skipta = int(input("1. Skipta um ofn/ofna"
                                   "\n2. Setja upp nýjan ofn"
                                   "\nVeldu (1-2): "))

                if skipta == 1:
                    while True:
                        fjofn = int(input("Fjöldi ofna? "))
                        if fjofn > 0:
                            listi[1][2] = fjofn
                            break
                        else:
                            print("Enginn ofn")
                    listi[1][0] = verk
                    listi[1][1] = skipta
                    k1.pipari()
                elif skipta == 2:
                    while True:
                        fjofn = int(input("Fjöldi ofna? "))
                        if fjofn > 0:
                            listi[1][2] = fjofn
                            break
                        else:
                            print("Enginn ofn")
                    listi[1][0] = verk
                    listi[1][1] = skipta
                else:
                    print("Rangur innsláttur")

            elif verk == 4:  # sturta/bað
                while True:
                    burta = int(input("1. Bað"
                                      "\n2. Sturta"
                                      "\nVeldu (1-2): "))
                    if burta == 1 or burta == 2:
                        break
                    else:
                        print("Rangur innsláttur")

                lagnir = input("Þarf að leggja nýjar lagnir fyrir sturtuna/baðið (Y/N)? ")
                lagnir = lagnir.lower()
                #Nyjar lagnir eða ekki
                while True:
                    if lagnir == "y":
                        listi[1][1] = lagnir
                        break
                    elif lagnir == "n":
                        listi[1][1] = lagnir
                        break
                    else:
                        print("Rangur innsláttur")

                while True:
                    if burta == 1:
                        print("ATH! Öll baðkör eru 160 x 70 cm")
                        while True:
                            bad = int(input("\n1. Ódýrt bað"
                                               "\n2. Gott bað á góðu verði"
                                               "\n3. Lúxus bað"
                                               "\nVeldu (1-3): "))
                            if bad == 1 or bad == 2 or bad == 3:
                                listi[1][2] = bad
                                break
                            else:
                                print("Rangur innsláttur")
                        listi[1][0] = verk
                        break
                    elif burta == 2:
                        print("ATH! einungis er sett upp sturtuklefa og lagnir að þörf, ekki sér sturtu -veggi né -botna")
                        while True:
                            sturta = int(input("\n1. Ódýr sturta"
                                               "\n2. Góð sturta á góðu verði"
                                               "\n3. Lúxus sturta"
                                               "\nVeldu (1-3): "))
                            if sturta == 1 or sturta == 2 or sturta == 3:
                                listi[1][2] = sturta
                                break
                            else:
                                print("Rangur innsláttur")
                        listi[1][0] = verk
                        break
                    else:
                        print("Rangur innsláttur")

            print(k1.pipari())

        elif val == "rafvirki" or val == "3":
            #####################################################################
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
            #####################################################################
            while True:
                manni = int(input("Veldu pípara (1-3): "))
                if manni == 1 or manni == 2 or manni == 3:
                    listi[4] = puppl[manni - 1]
                    break
                else:
                    print("Rangur innsláttur")

            print("Valmöguleikar:"
                  "\n1. Skipta um rafmagstöflu"
                  "\n2. Viðgerðir á sambandsleysi í vegg"
                  "\n3. Tengja raftæki við vegg/loft")
            valR = int(input("Veldu (1-3): "))
            if valR == 1:
                staerd = int(input("Sláðu inn stæð hússins í m²: "))
                listi[2][1] = "asd"

        elif val == "smiður" or val == "smidur" or val == "4":
            #####################################################################
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
            #####################################################################
            while True:
                manni = int(input("Veldu pípara (1-3): "))
                if manni == 1 or manni == 2 or manni == 3:
                    listi[4] = puppl[manni - 1]
                    break
                else:
                    print("Rangur innsláttur")
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
                            qwert = ha * 15000
                            vallur = qwert + (pall * 2500)
                        else:
                            vallur = pall * 2500
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
                                skurtskurt = x * 500 + skurtskurt
                                skurtskurt = skurtskurt + 8000
                            skurtskurt += 5000
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
                                skurtskurt = x * 1000 + skurtskurt
                                skurtskurt = skurtskurt + 8000
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
                        jolakotturinn = jolakotturinn * 5000
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