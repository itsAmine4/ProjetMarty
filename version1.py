import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedLayout, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt6.QtCore import QSize
from martypy import Marty

class MartyControllerApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.marty = None

    def initUI(self):
        self.setWindowTitle('Contrôle de Marty')
        
        # Créer un QStackedLayout
        stacked_layout = QStackedLayout()

        # Ajouter un QLabel pour l'image d'arrière-plan
        background_label = QLabel(self)
        pixmap = QPixmap('background.png')
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)

        # Ajouter le QLabel au QStackedLayout
        stacked_layout.addWidget(background_label)

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        #emotion section
        
        emotion_layout = QHBoxLayout()
        
        self.emotion_label = QLabel('Émotion:')
        emotion_layout.addWidget(self.emotion_label)
        
        self.emotion_entry = QLineEdit()
        emotion_layout.addWidget(self.emotion_entry)
        
        self.set_emotion_button = QPushButton()
        self.set_emotion_button.setIcon(QIcon('path/to/emotion_image.png'))
        self.set_emotion_button.setIconSize(QSize(40, 40))
        self.set_emotion_button.clicked.connect(self.set_emotion)
        emotion_layout.addWidget(self.set_emotion_button)
        
        main_layout.addLayout(emotion_layout)

        # Boutons de contrôle
        controle_layout = QHBoxLayout()
        
        self.forward_button = QPushButton()
        self.forward_button.setIcon(QIcon('avancer.png'))
        self.forward_button.setIconSize(QSize(40, 40))
        self.forward_button.clicked.connect(self.move_forward)
        controle_layout.addWidget(self.forward_button)
        
        self.backward_button = QPushButton()
        self.backward_button.setIcon(QIcon('reculer.png'))
        self.backward_button.setIconSize(QSize(40, 40))
        self.backward_button.clicked.connect(self.move_backward)
        controle_layout.addWidget(self.backward_button)
        
        main_layout.addLayout(controle_layout)
        
        #mouvement lateral
        
        side_layout = QHBoxLayout()
        
        self.turn_right_button = QPushButton()
        self.turn_right_button.setIcon(QIcon('gauche.png'))
        self.turn_right_button.setIconSize(QSize(40, 40))
        self.turn_right_button.clicked.connect(self.turn_right)
        side_layout.addWidget(self.turn_right_button)
        
        self.turn_left_button = QPushButton()
        self.turn_left_button.setIcon(QIcon('droite.png'))
        self.turn_left_button.setIconSize(QSize(40, 40))
        self.turn_left_button.clicked.connect(self.turn_left)
        side_layout.addWidget(self.turn_left_button)
        
        main_layout.addLayout(side_layout)
        
        # DC Section
        dc_layout = QHBoxLayout()
        
        self.dance_button = QPushButton()
        self.dance_button.setIcon(QIcon('dance.png'))
        self.dance_button.setIconSize(QSize(40, 40))
        self.dance_button.clicked.connect(self.dance)
        dc_layout.addWidget(self.dance_button)
        
        self.celebrate_button = QPushButton()
        self.celebrate_button.setIcon(QIcon('celebrer.png'))
        self.celebrate_button.setIconSize(QSize(40, 40))
        self.celebrate_button.clicked.connect(self.celebrate)
        dc_layout.addWidget(self.celebrate_button)
        
        main_layout.addLayout(dc_layout)
        
        # Connexion Section
        self.ip_label = QLabel('Adresse IP de Marty:')
        main_layout.addWidget(self.ip_label)
        
        self.ip_entry = QLineEdit()
        main_layout.addWidget(self.ip_entry)

        self.setLayout(main_layout)
        
        #Connexion et déconnexion
        
        connection_layout = QHBoxLayout()
        
        self.connect_button = QPushButton()
        self.connect_button.setIcon(QIcon('connecter.png'))
        self.connect_button.setIconSize(QSize(40, 40))
        self.connect_button.clicked.connect(self.connect_to_marty)
        connection_layout.addWidget(self.connect_button)
        
        self.disconnect_button = QPushButton()
        self.disconnect_button.setIcon(QIcon('deconnecter.png'))
        self.disconnect_button.setIconSize(QSize(40, 40))
        self.disconnect_button.clicked.connect(self.disconnect_from_marty)
        connection_layout.addWidget(self.disconnect_button)
        
        stacked_layout.addWidget(main_widget)
        main_layout.addLayout(connection_layout)

        

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
            self.marty.walk(num_steps=4, step_length=40, move_time=1500, blocking=True)
    
    def move_backward(self):
        if self.marty:
            self.marty.walk(num_steps=4, step_length=-25, move_time=1500, blocking=True)
    
    def turn_left(self):
        if self.marty:
            self.marty.walk(num_steps=4, turn=-20, move_time=1500, blocking=True)
    
    def turn_right(self):
        if self.marty:
            self.marty.walk(num_steps=4, turn=20, move_time=1500, blocking=True)
    
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
