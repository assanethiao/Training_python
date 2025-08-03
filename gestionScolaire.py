class Eleve:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        if 0 <= note <= 20:
            self.notes.append(note)
            print(f"Note {note} ajoutée à {self.nom}.")
        else:
            print("❌ Note invalide (doit être entre 0 et 20).")

    def moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

    def afficher_infos(self):
        print(f"\n👨‍🎓 Élève : {self.nom}")
        print("Notes :", self.notes)
        print(f"Moyenne : {self.moyenne():.2f}")
