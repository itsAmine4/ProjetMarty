# widget.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QSizePolicy
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap

class MartyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contrôle de Marty')

        # Layout principal
        main_layout = QVBoxLayout(self)

        # Ajouter un QLabel pour l'image d'arrière-plan
        self.background_label = QLabel(self)  # Utilisation de self pour rendre l'attribut accessible dans toute la classe
        self.background_pixmap = QPixmap('images/background2.png')
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Conteneur pour les widgets principaux
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Section des émotions
        emotion_layout = QHBoxLayout()
        
        self.emotion_label = QLabel('Émotion:')
        emotion_layout.addWidget(self.emotion_label)

        self.emotion_entry = QLineEdit()
        self.emotion_entry.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        emotion_layout.addWidget(self.emotion_entry)

        self.set_emotion_button = QPushButton()
        self.set_emotion_button.setIcon(QIcon('images/emotion_image.png'))
        self.set_emotion_button.setIconSize(QSize(40, 40))
        emotion_layout.addWidget(self.set_emotion_button)

        content_layout.addLayout(emotion_layout)

        # Affichage des données des capteurs
        self.battery_label = QLabel('Niveau de batterie : ')
        self.battery_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        content_layout.addWidget(self.battery_label)

        self.obstacle_label = QLabel('Obstacle : Non détecté')
        self.obstacle_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        content_layout.addWidget(self.obstacle_label)
        
        self.color_label = QLabel('Couleur : Non détectée')
        self.color_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        content_layout.addWidget(self.color_label)

        # Boutons de contrôle
        control_layout = QHBoxLayout()

        self.forward_button = QPushButton()
        self.forward_button.setIcon(QIcon('images/avancer.png'))
        self.forward_button.setIconSize(QSize(40, 40))
        control_layout.addWidget(self.forward_button)

        self.backward_button = QPushButton()
        self.backward_button.setIcon(QIcon('images/reculer.png'))
        self.backward_button.setIconSize(QSize(40, 40))
        control_layout.addWidget(self.backward_button)

        content_layout.addLayout(control_layout)

        # Mouvement latéral
        side_layout = QHBoxLayout()

        self.turn_left_button = QPushButton()
        self.turn_left_button.setIcon(QIcon('images/gauche.png'))
        self.turn_left_button.setIconSize(QSize(40, 40))
        side_layout.addWidget(self.turn_left_button)

        self.turn_right_button = QPushButton()
        self.turn_right_button.setIcon(QIcon('images/droite.png'))
        self.turn_right_button.setIconSize(QSize(40, 40))
        side_layout.addWidget(self.turn_right_button)

        content_layout.addLayout(side_layout)

        # Section DC
        dc_layout = QHBoxLayout()

        self.dance_button = QPushButton()
        self.dance_button.setIcon(QIcon('images/dance.png'))
        self.dance_button.setIconSize(QSize(40, 40))
        dc_layout.addWidget(self.dance_button)

        self.celebrate_button = QPushButton()
        self.celebrate_button.setIcon(QIcon('images/celebrer.png'))
        self.celebrate_button.setIconSize(QSize(40, 40))
        dc_layout.addWidget(self.celebrate_button)

        content_layout.addLayout(dc_layout)

        # Section Connexion
        self.ip_label = QLabel('Adresse IP de Marty:')
        self.ip_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        content_layout.addWidget(self.ip_label)

        self.ip_entry = QLineEdit()
        self.ip_entry.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        content_layout.addWidget(self.ip_entry)

        connection_layout = QHBoxLayout()

        self.connect_button = QPushButton()
        self.connect_button.setIcon(QIcon('images/connecter.png'))
        self.connect_button.setIconSize(QSize(40, 40))
        connection_layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton()
        self.disconnect_button.setIcon(QIcon('images/deconnecter.png'))
        self.disconnect_button.setIconSize(QSize(40, 40))
        connection_layout.addWidget(self.disconnect_button)

        content_layout.addLayout(connection_layout)
        
        # Ajouter le widget de contenu au layout principal
        main_layout.addWidget(content_widget)
        self.setLayout(main_layout)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustBackground()

    def adjustBackground(self):
        self.background_label.setGeometry(self.rect())
        scaled_pixmap = self.background_pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.background_label.setPixmap(scaled_pixmap)
