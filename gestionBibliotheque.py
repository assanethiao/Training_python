class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def afficher(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        print(f"{self.titre} par {self.auteur} - {statut}")

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté : {livre.titre}")

    def afficher_livres(self):
        print("\n📚 Liste des livres :")
        if not self.livres:
            print("Aucun livre.")
        for livre in self.livres:
            livre.afficher()

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                if livre.disponible:
                    livre.disponible = False
                    print(f"✅ Vous avez emprunté : {livre.titre}")
                else:
                    print("⛔ Ce livre est déjà emprunté.")
                return
        print("❌ Livre non trouvé.")

    def rendre_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                if not livre.disponible:
                    livre.disponible = True
                    print(f"👍 Livre rendu : {livre.titre}")
                else:
                    print("📘 Ce livre est déjà disponible.")
                return
        print("❌ Livre non trouvé.")
