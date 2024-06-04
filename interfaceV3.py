import os
os.environ['QT_PLUGIN_PATH'] = '/Users/amineelkassbi/opt/anaconda3/lib/python3.9/site-packages/PyQt6/Qt6/plugins'
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize
from martypy import Marty

class MartyControllerApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.marty = None

    def initUI(self):
        self.setWindowTitle('Contrôle de Marty')

        # Change the background color to blue
        self.setStyleSheet("background-color: lightblue;")

        layout = QVBoxLayout()

        # Connexion Section
        self.ip_label = QLabel('Adresse IP de Marty:')
        layout.addWidget(self.ip_label)
        
        self.ip_entry = QLineEdit()
        layout.addWidget(self.ip_entry)
        
        self.connect_button = QPushButton('Connecter')
        self.connect_button.clicked.connect(self.connect_to_marty)
        layout.addWidget(self.connect_button)
        
        self.disconnect_button = QPushButton('Déconnecter')
        self.disconnect_button.clicked.connect(self.disconnect_from_marty)
        layout.addWidget(self.disconnect_button)

        # Control Buttons
        control_layout = QHBoxLayout()
        
        # Ajouter les boutons de flèche avec les images
        fleche_haut_button = QPushButton()
        fleche_haut_button.setIcon(QIcon("fleche_haut.jpeg"))
        fleche_haut_button.setIconSize(QSize(50, 50))
        fleche_haut_button.clicked.connect(self.move_forward)
        control_layout.addWidget(fleche_haut_button)
        
        fleche_bas_button = QPushButton()
        fleche_bas_button.setIcon(QIcon("fleche_bas.jpeg"))
        fleche_bas_button.setIconSize(QSize(50, 50))
        fleche_bas_button.clicked.connect(self.move_backward)
        control_layout.addWidget(fleche_bas_button)
        
        fleche_gauche_button = QPushButton()
        fleche_gauche_button.setIcon(QIcon("fleche_gauche.jpeg"))
        fleche_gauche_button.setIconSize(QSize(50, 50))
        fleche_gauche_button.clicked.connect(self.turn_left)
        control_layout.addWidget(fleche_gauche_button)
        
        fleche_droite_button = QPushButton()
        fleche_droite_button.setIcon(QIcon("fleche_droite.jpeg"))
        fleche_droite_button.setIconSize(QSize(50, 50))
        fleche_droite_button.clicked.connect(self.turn_right)
        control_layout.addWidget(fleche_droite_button)

        layout.addLayout(control_layout)
        
        # Emotion Section
        self.dance_button = QPushButton('Danser')
        self.dance_button.clicked.connect(self.dance)
        layout.addWidget(self.dance_button)
        
        self.celebrate_button = QPushButton('Célébrer')
        self.celebrate_button.clicked.connect(self.celebrate)
        layout.addWidget(self.celebrate_button)
        
        self.emotion_label = QLabel('Émotion:')
        layout.addWidget(self.emotion_label)
        
        self.emotion_entry = QLineEdit()
        layout.addWidget(self.emotion_entry)
        
        self.set_emotion_button = QPushButton('Montrer l\'émotion')
        self.set_emotion_button.clicked.connect(self.set_emotion)
        layout.addWidget(self.set_emotion_button)

        # Ajouter une image de Marty
        self.marty_image_label = QLabel(self)
        self.marty_image_label.setPixmap(QPixmap("marty_image.png"))
        self.marty_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.marty_image_label)

        self.setLayout(layout)

    def connect_to_marty(self):
        ip_address = self.ip_entry.text()
        try:
            self.marty = Marty('wifi', ip_address)
            QMessageBox.information(self, "Connexion", f"Connecté à Marty à {ip_address}")
        except Exception as e:
            QMessageBox.critical(self, "Connexion", f"Échec de la connexion à Marty: {str(e)}")

    def disconnect_from_marty(self):
        if self.marty:
            del self.marty
            self.marty = None
            QMessageBox.information(self, "Déconnexion", "Déconnecté de Marty")

    def move_forward(self):
        if self.marty:
            self.marty.walk(num_steps=2, step_length=25, move_time=1500, blocking=True)
    
    def move_backward(self):
        if self.marty:
            self.marty.walk(num_steps=2, step_length=-25, move_time=1500, blocking=True)
    
    def turn_left(self):
        if self.marty:
            self.marty.walk(num_steps=2, turn=-30, move_time=1500, blocking=True)
    
    def turn_right(self):
        if self.marty:
            self.marty.walk(num_steps=2, turn=30, move_time=1500, blocking=True)
    
    def dance(self):
        if self.marty:
            self.marty.dance()
    
    def celebrate(self):
        if self.marty:
            self.marty.celebrate()
    
    def set_emotion(self):
        emotion = self.emotion_entry.text()
        if self.marty:
            self.marty.set_emotion(emotion)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyControllerApp()
    ex.show()
    sys.exit(app.exec())
