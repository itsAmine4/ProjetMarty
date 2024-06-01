import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
import cv2
import qreader
from martypy import Marty

class MartyControllerApp(QWidget):
    def _init_(self):
        super()._init_()
        
        self.initUI()
        self.marty = None

    def initUI(self):
        self.setWindowTitle('Contrôle de Marty')

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
        self.forward_button = QPushButton('Avancer')
        self.forward_button.clicked.connect(self.move_forward)
        layout.addWidget(self.forward_button)
        
        self.backward_button = QPushButton('Reculer')
        self.backward_button.clicked.connect(self.move_backward)
        layout.addWidget(self.backward_button)
        
        self.turn_left_button = QPushButton('Tourner à gauche')
        self.turn_left_button.clicked.connect(self.turn_left)
        layout.addWidget(self.turn_left_button)
        
        self.turn_right_button = QPushButton('Tourner à droite')
        self.turn_right_button.clicked.connect(self.turn_right)
        layout.addWidget(self.turn_right_button)
        
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

        self.setLayout(layout)

    def connect_to_marty(self):
        ip_address = self.ip_entry.text()
        try:
            self.marty = Marty(ip_address)
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
            self.marty.walk_forward()
    
    def move_backward(self):
        if self.marty:
            self.marty.walk_backward()
    
    def turn_left(self):
        if self.marty:
            self.marty.turn_left()
    
    def turn_right(self):
        if self.marty:
            self.marty.turn_right()
    
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

    
if __name__ == '_main_':
    app = QApplication(sys.argv)
    ex = MartyControllerApp()
    ex.show()
    sys.exit(app.exec())