import random
import os

FICHIER_CITATIONS = "citations.txt"

def charger_citations():
    """Charge les citations depuis le fichier, sinon retourne une liste par défaut."""
    if not os.path.exists(FICHIER_CITATIONS):
        return [
            "Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme.",
            "La meilleure façon de prédire l'avenir, c'est de le créer.",
            "Ne regarde pas l’horloge ; fais ce qu’elle fait. Continue."
        ]
    with open(FICHIER_CITATIONS, "r", encoding="utf-8") as f:
        return [ligne.strip() for ligne in f if ligne.strip()]

def sauvegarder_citations(citations):
    """Sauvegarde la liste de citations dans le fichier."""
    with open(FICHIER_CITATIONS, "w", encoding="utf-8") as f:
        for citation in citations:
            f.write(citation + "\n")

def afficher_menu():
    print("\n=== GÉNÉRATEUR DE CITATIONS ===")
    print("1. Voir une citation au hasard")
    print("2. Ajouter une citation")
    print("3. Quitter")

def main():
    citations = charger_citations()

    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            print("\n💡 " + random.choice(citations))
        elif choix == "2":
            nouvelle = input("Entrez votre citation : ").strip()
            if nouvelle:
                citations.append(nouvelle)
                sauvegarder_citations(citations)
                print("✅ Citation ajoutée avec succès.")
        elif choix == "3":
            print("À bientôt 👋")
            break
        else:
            print("❌ Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
