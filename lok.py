#Kolbeinn og Ágúst
#22.11.2017
#Lokaverkefni í forritun

#Pöntun á þjónustu

print("Valmöguleikar:"
      "\nMálari"
      "\nPípari"
      "\nRafvirki"
      "\nSmiður")
val = input("Veldu þjónustu: ")



a = 0
try:
    if val == "malari" or val == "Malari" or val == "Málari" or val == "málari":
        a = 0
    elif val == "pipari" or val == "Pipari" or val == "Pípari" or val == "pípari":
        a = 2
    elif val == "rafvirki" or val == "Rafvirki":
        a = 3
    elif val == "smiður" or val == "Smiður":
        a = 4
    else:
        print("Rangur innsláttur")
except:
    print("Óvænt villa")


class Thjonusta:
    def __init__(self, þjonusta):
        self.þ = þjonusta

    def malari(self, flotur):
        asd = "asd"

    def pipari(self, lagnir):
        asd = "asd"

    def rafvirki(self, asd):
        asd = "asd"

k1 = Thjonusta(a)






