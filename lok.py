#Kolbeinn og Ágúst
#22.11.2017
#Lokaverkefni í forritun

#Pöntun á þjónustu


class Thjonusta:
    def __init__(self, þjonusta):
        self.þ = þjonusta

    def malari(self, flotur, litur):
        asd = "asd"

    def pipari(self, lagnir):
        asd = "asd"

    def rafvirki(self, klst):
        asd = "asd"

#listi[0] = hvað málarinn á að gera
#listi[1] = hvað píparinn á að gera
#listi[2] = hvað rafvirkinn á að gera
#listi[3] = hvað smiðurinn á að gera
listi = [[0, 0], 0, 0, 0]

print("Valmöguleikar:"
      "\nMálari"
      "\nPípari"
      "\nRafvirki"
      "\nSmiður")

þjon = 0
val = input("Veldu þjónustu: ")
k1 = Thjonusta(listi)
if val == "malari" or val == "Malari" or val == "Málari" or val == "málari":
    print("Valmöguleikar:"
          "\n1. Gulur"
          "\n2. Rauður"
          "\n3. Grænn"
          "\n4. Blár"
          "\n5. Svartur"
          "\n6. Hvítur")
    try:
        litur = int(input("Veldu lit: "))
        if litur > 6 or litur < 1:
            raise ValueError("Rangur innsláttur")
    except ValueError as x:
        print(x)

elif val == "pipari" or val == "Pipari" or val == "Pípari" or val == "pípari":
    þjon = 2
    print("\nValmöguleikar:"
          "\n1. Vaskur"
          "\n2. Klósett"
          "\n3. Stórar lagnir (nýjar lagnir fyrir t.d. baðherbergi)"
          "\n4. Ofn"
          "\n5. Sturta/Bað")
    try:
        verk = int(input("Veldu verk (1-5): "))
        if verk == 1:
            k1(listi).malari(1)
    except ValueError:
        print("Rangt gagnatak")


elif val == "rafvirki" or val == "Rafvirki":
    þjon = 3
elif val == "smiður" or val == "Smiður":
    þjon = 4
else:
    print("Rangur innsláttur")







