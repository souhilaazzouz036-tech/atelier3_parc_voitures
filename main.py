from voiture import Voiture
from parc import parc

parc = parc(1, "toronto", 3)

v1 = Voiture("A23", "toyota", "rouge")
v2 = Voiture("B256", "BMW", "BLANC")
v3 = Voiture("C789", "HONDA", "NOIR")

parc.entrer_une_voiture(v1)
parc.entrer_une_voiture(v2)
parc.entrer_une_voiture(v3)







