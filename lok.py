#Kolbeinn og Ágúst
#22.11.2017
#Lokaverkefni í forritun

#Pöntun á þjónustu


class Thjonusta:
    def __init__(self, þjonusta):
        self.þ = þjonusta

    def malari(self):
        litur = self.þ[0][0]
        flotur = self.þ[0][1]
        verdL = 0
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
                "\nVaskur: " + str(vsk) +
                "\nSamtals: " + str(vsk+verd))

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

listi = [[0, 0], 0, 0, [0, [0, 0, 0], [0, 0, 0]]]



þjon = 0
verk = 0
k1 = Thjonusta
asd = True
while asd:
    print("Valmöguleikar:"
          "\nMálari"
          "\nPípari"
          "\nRafvirki"
          "\nSmiður")
    asd = False
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
                    print(k1(listi).malari())

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
            if verk == 1:
                k1(listi).pipari()
            elif verk == 2:
                k1(listi).pipari()
        elif val == "rafvirki":
            þjon = 3
        elif val == "smiður" or val == "smidur":
            þjon = 4
        else:
            raise ValueError("Rangt gagnatak")

    except ValueError as x:
        print(x, "\n")
        pass
        asd = True






