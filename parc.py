class parc:
    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listevoitures = []

    def entrer_une_voiture(self, voiture):
        if voiture in self.listevoitures:
            print("la voiture existe deja dans le parc")
            return
        if len(self.listevoitures) >= self.capacite:
            print("parc est plein")
            return
        self.listevoitures.append(voiture)
        print("voiture ajoutee avec succes")

