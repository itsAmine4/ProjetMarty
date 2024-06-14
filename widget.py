import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSizePolicy
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
from detection import Detection

class MartyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.detection = Detection(marty=None, battery_label=None, obstacle_label=None, color_label=None)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contrôle de Marty')

        # Layout principal
        main_layout = QVBoxLayout(self)

        # Ajouter un QLabel pour l'image d'arrière-plan
        self.background_label = QLabel(self)
        self.background_pixmap = QPixmap('images/backgrounds.png')
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
        self.set_emotion_button.setIcon(QIcon('images/emotion.png'))
        self.set_emotion_button.setIconSize(QSize(20, 20))
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

        # Ajouter un bouton pour aller à la nouvelle page
        #self.new_page_button = QPushButton("mapage")
        #self.new_page_button.clicked.connect(self.show_new_page)
        #content_layout.addWidget(self.new_page_button)
        
        # Ajouter le widget de contenu au layout principal
        main_layout.addWidget(content_widget)
        self.setLayout(main_layout)

    def on_dropdown_changed(self, index):
        sensor_position = self.dropdown.currentText()
        color_value = self.detection.get_color_value(sensor_position)
        self.color_label.setText(f'Valeur du capteur {sensor_position} : {color_value}')

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustBackground()

    def adjustBackground(self):
        self.background_label.setGeometry(self.rect())
        scaled_pixmap = self.background_pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.background_label.setPixmap(scaled_pixmap)

    def show_new_page(self):
        self.new_page = NewPageWidget(self.background_pixmap, self.detection)
        self.new_page.show()

class NewPageWidget(QWidget):
    def __init__(self, background_pixmap, detection):
        super().__init__()
        self.setWindowTitle('Nouvelle Page')
        self.background_pixmap = background_pixmap
        self.detection = detection
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)

        # Ajouter un QLabel pour l'image d'arrière-plan
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.background_label.setGeometry(self.rect())
        main_layout.addWidget(self.background_label)

        # Ajouter la liste déroulante
        dropdown_layout = QVBoxLayout()

        self.dropdown_label = QLabel('Choisissez une option:')
        dropdown_layout.addWidget(self.dropdown_label)

        self.dropdown = QComboBox()
        self.dropdown.addItems(["yellow", "red", "black", "green", "darkblue", "skyblue", "pink"])
        self.dropdown.currentIndexChanged.connect(self.on_dropdown_changed)
        dropdown_layout.addWidget(self.dropdown)

        main_layout.addLayout(dropdown_layout)

        # Assurez-vous que le layout principal n'essaie pas de se redimensionner indéfiniment
        self.setLayout(main_layout)
        self.setFixedSize(400, 300)  # Définir une taille fixe pour la fenêtre

    def on_dropdown_changed(self, index):
        sensor_position = self.dropdown.currentText()
        color_value = self.detection.get_color_value(sensor_position)
        print(f'Valeur du capteur {sensor_position} : {color_value}')  # Afficher la valeur dans la console

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustBackground()

    def adjustBackground(self):
        self.background_label.setGeometry(self.rect())
        scaled_pixmap = self.background_pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.background_label.setPixmap(scaled_pixmap)

# Code pour exécuter l'application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyWidget()
    ex.show()
    sys.exit(app.exec())
