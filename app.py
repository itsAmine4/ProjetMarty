from PyQt6 import QtWidgets

from PyQt6.QtWidgets import QApplication, QLabel

def main():
    # Créer une instance de l'application PyQt6
    app = QApplication([])

    # Créer une étiquette avec un message
    label = QLabel("PyQt6 fonctionne correctement !")
    label.show()

    # Exécuter l'application
    app.exec()

if __name__ == "__main__":
    main()
