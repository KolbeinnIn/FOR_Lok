#Kolbeinn og Ágúst
#22.11.2017
#Lokaverkefni í forritun

#Pöntun á þjónustu



with open("starfsmenn.txt", "r") as skra:
    skra = skra.read().split("\n")
    malarar = skra[0].split(";")
    piparar = skra[1].split(";")
    rafv = skra[2].split(";")
    smidir = skra[3].split(";")


class Thjonusta:
    def __init__(self, þjonusta):
        self.þ = þjonusta

    def malari(self):
        stadfestignargjald = 2000
        litur = self.þ[0][0]
        flotur = self.þ[0][1]
        if 5 > litur > 0:
            verdL = 150
        else:
            verdL = 100

        #0.25 af því að það eru 15 mínútur (fjórðungur af klukkustund). Það tekur korter að mála einn fermeter
        timi = flotur * 0.25
        verd = flotur * verdL
        verd += (timi * 2900)
        vsk = verd * 0.24
        return ("Það gera " + str(int(verd)) + "kr" +
                "\nStaðfestingargjald " + str(stadfestignargjald) + "kr" +
                "\nVaskur: " + str(vsk) + "kr" +
                "\nSamtals: " + str(int(vsk+verd+stadfestignargjald)) + "kr")

    def pipari(self):
        asd = "asd2"
        return asd

    def rafvirki(self):
        asd = "asd3"
        return asd

#listi[0] = hvað málarinn á að gera
#listi[1] = hvað píparinn á að gera
#listi[2] = hvað rafvirkinn á að gera
#listi[3] = hvað smiðurinn á að gera

listi = [[0, 0], [0, 0], 0, [0, [0, 0, 0], [0, 0, 0]]]


þjon = 0
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
        if val == "malari" or val == "málari":
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

        elif val == "pipari" or val == "pípari":
            þjon = 2
            print("\nValmöguleikar:"
                  "\n1. Vaskur"
                  "\n2. Klósett"
                  "\n3. Stórar lagnir (nýjar lagnir fyrir t.d. baðherbergi)"
                  "\n4. Ofn"
                  "\n5. Sturta/Bað")
            try:
                verk = int(input("Veldu verk (1-5): "))
            except ValueError:
                print("Rangt gagnatak")

            if verk == 1:               #vaskur
                listi[1][0] = 1
                k1.pipari()
            elif verk == 2:             #klósett
                listi[1][0] = 2
                k1.pipari()
            elif verk == 3:             #stórar lagnir
                listi[1][0] = 3
                k1.pipari()
            elif verk == 4:             #ofn
                listi[1][0] = 4
                k1.pipari()
            elif verk == 5:             #sturta/bað
                listi[1][0] = 5
                k1.pipari()

        elif val == "rafvirki":
            þjon = 3
        elif val == "smiður" or val == "smidur":
            þjon = 4
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
                        fm = 1200 + 2000
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
                        fj = int(input("Hversu margir eru veggirnir? "))
                        teljari = 0
                        jolasvein = []
                        for x in range(fj):
                            teljari += 1
                            print("--- Veggur", teljari, "---")
                            sterd = int(input("Sláðu inn stærð veggs í fermetrum "))
                            jolasvein.append(sterd)
                        if bubbi == 1:
                            skurtskurt = 0
                            for x in jolasvein:
                                skurtskurt=x*500+skurtskurt
                                skurtskurt=skurtskurt+8000
                            print(skurtskurt)
                        elif bubbi == 2:
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
                            kost = "kost"
                        elif berg == 2:
                            kost = "kostinn"
                        else:
                            print("Rangur innsláttur")
                    elif utinn == 3:
                        jolakotturinn = int(input("Stærð gólfs í fermetrum: "))

                    else:
                        print("Rangur innsláttur")
            except ValueError:
                print("Rangt gagnatak")
        else:
            raise ValueError("Rangt gagnatak")

    except ValueError as x:
        print(x, "\n")
        pass
        asd = True







