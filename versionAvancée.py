import os
os.environ['QT_PLUGIN_PATH'] = '/Users/amineelkassbi/opt/anaconda3/lib/python3.9/site-packages/PyQt6/Qt6/plugins'
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QSizePolicy
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QIcon, QPixmap
from martypy import Marty

class MartyControllerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.marty = None
        self.timer = QTimer(self)

    def initUI(self):
        self.setWindowTitle('Contrôle de Marty')

        # Définir la feuille de style pour le texte et les boutons
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-size: 18px;
                color: lightblue;
                font-family: Arial, Helvetica, sans-serif;
            }
            QPushButton#emotionButton {
                background-color: green;
            }
            QPushButton {
                background-color: white;
                border: 2px solid #cccccc;
                padding: 5px;
                border-radius: 10px;
                width: 60px;
                height: 60px;
            }
            #batteryLabel {
                font-size: 24px;
                color: green;
            }
        """)

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
        self.set_emotion_button.setIconSize(QSize(60, 60))
        self.set_emotion_button.clicked.connect(self.set_emotion)
        self.set_emotion_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.set_emotion_button.setObjectName('emotionButton')

        emotion_layout.addWidget(self.set_emotion_button)

        content_layout.addLayout(emotion_layout)

        # Affichage des données des capteurs
        self.battery_label = QLabel('Niveau de batterie : ')
        self.battery_label.setObjectName('batteryLabel')  # Identifiant pour appliquer la couleur
        self.battery_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        content_layout.addWidget(self.battery_label)

        # Boutons de contrôle
        control_layout = QHBoxLayout()

        self.forward_button = QPushButton()
        self.forward_button.setIcon(QIcon('images/avancer.png'))
        self.forward_button.setIconSize(QSize(60, 60))
        self.forward_button.clicked.connect(self.move_forward)
        self.forward_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        control_layout.addWidget(self.forward_button)

        self.backward_button = QPushButton()
        self.backward_button.setIcon(QIcon('images/reculer.png'))
        self.backward_button.setIconSize(QSize(60, 60))
        self.backward_button.clicked.connect(self.move_backward)
        self.backward_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        control_layout.addWidget(self.backward_button)

        content_layout.addLayout(control_layout)

        # Mouvement latéral
        side_layout = QHBoxLayout()

        self.turn_left_button = QPushButton()
        self.turn_left_button.setIcon(QIcon('images/gauche.png'))
        self.turn_left_button.setIconSize(QSize(60, 60))
        self.turn_left_button.clicked.connect(self.turn_left)
        self.turn_left_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        side_layout.addWidget(self.turn_left_button)

        self.turn_right_button = QPushButton()
        self.turn_right_button.setIcon(QIcon('images/droite.png'))
        self.turn_right_button.setIconSize(QSize(60, 60))
        self.turn_right_button.clicked.connect(self.turn_right)
        self.turn_right_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        side_layout.addWidget(self.turn_right_button)

        content_layout.addLayout(side_layout)

        # Section DC
        dc_layout = QHBoxLayout()

        self.dance_button = QPushButton()
        self.dance_button.setIcon(QIcon('images/dance.png'))
        self.dance_button.setIconSize(QSize(60, 60))
        self.dance_button.clicked.connect(self.dance)
        self.dance_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        dc_layout.addWidget(self.dance_button)

        self.celebrate_button = QPushButton()
        self.celebrate_button.setIcon(QIcon('images/celebrer.png'))
        self.celebrate_button.setIconSize(QSize(60, 60))
        self.celebrate_button.clicked.connect(self.celebrate)
        self.celebrate_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
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
        self.connect_button.setIconSize(QSize(60, 60))
        self.connect_button.clicked.connect(self.connect_to_marty)
        self.connect_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        connection_layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton()
        self.disconnect_button.setIcon(QIcon('images/deconnecter.png'))
        self.disconnect_button.setIconSize(QSize(60, 60))
        self.disconnect_button.clicked.connect(self.disconnect_from_marty)
        self.disconnect_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        connection_layout.addWidget(self.disconnect_button)

        content_layout.addLayout(connection_layout)
        
        # Ajouter le widget de contenu au layout principal
        main_layout.addWidget(content_widget)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustBackground()

    def adjustBackground(self):
        self.background_label.setGeometry(self.rect())
        scaled_pixmap = self.background_pixmap.scaled(self.size(),Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.background_label.setPixmap(scaled_pixmap)
        
    def connect_to_marty(self):
        ip_address = self.ip_entry.text()
        try:
            self.marty = Marty('wifi', ip_address)
            QMessageBox.information(self, "Connexion", f"Connecté à Marty à {ip_address}")

            # Démarrer le timer pour mettre à jour les capteurs toutes les secondes
            self.timer.timeout.connect(self.update_sensors)
            self.timer.start(1000)  # mise à jour toutes les secondes

        except Exception as e:
            QMessageBox.critical(self, "Connexion", f"Échec de la connexion à Marty: {str(e)}")

    def disconnect_from_marty(self):
        if self.marty:
            del self.marty
            self.marty = None
            QMessageBox.information(self, "Déconnexion", "Déconnecté de Marty")

            # Arrêter le timer
            self.timer.stop()

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

    def update_sensors(self):
        if self.marty:
            try:
                battery_level = self.marty.get_battery_remaining()
                self.battery_label.setText(f"Niveau de batterie : {battery_level}%")
            except Exception as e:
                print(f"Erreur lors de la mise à jour des capteurs : {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyControllerApp()
    ex.show()
    sys.exit(app.exec())
