# main.py
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QTimer
from martypy import Marty
from widget import MartyWidget
from mouvements_emotions import MovementsEmotions
from detection import Detection

class MartyControllerApp(MartyWidget):
    def __init__(self):
        super().__init__()
        self.marty = None
        self.timer = QTimer(self)
        self.obstacle_timer = QTimer(self)
        self.color_timer = QTimer(self)

        self.connect_button.clicked.connect(self.connect_to_marty)
        self.disconnect_button.clicked.connect(self.disconnect_from_marty)
        self.set_emotion_button.clicked.connect(self.set_emotion)

        self.forward_button.clicked.connect(self.move_forward)
        self.backward_button.clicked.connect(self.move_backward)
        self.turn_left_button.clicked.connect(self.turn_left)
        self.turn_right_button.clicked.connect(self.turn_right)
        self.dance_button.clicked.connect(self.dance)
        self.celebrate_button.clicked.connect(self.celebrate)

    def connect_to_marty(self):
        ip_address = self.ip_entry.text()
        try:
            self.marty = Marty('wifi', ip_address)
            QMessageBox.information(self, "Connexion", f"Connecté à Marty à {ip_address}")

            self.movements_emotions = MovementsEmotions(self.marty)
            self.detection = Detection(self.marty, self.battery_label, self.obstacle_label, self.color_label)

            self.timer.timeout.connect(self.detection.update_sensors)
            self.timer.start(1000)

            self.obstacle_timer.timeout.connect(self.detection.check_for_obstacles)
            self.obstacle_timer.start(5000)

            self.color_timer.timeout.connect(self.detection.detect_color)
            self.color_timer.start(5000)

        except Exception as e:
            QMessageBox.critical(self, "Connexion", f"Échec de la connexion à Marty: {str(e)}")

    def disconnect_from_marty(self):
        if self.marty:
            del self.marty
            self.marty = None
            QMessageBox.information(self, "Déconnexion", "Déconnecté de Marty")

            self.timer.stop()
            self.obstacle_timer.stop()
            self.color_timer.stop()

    def move_forward(self):
        self.movements_emotions.move_forward()

    def move_backward(self):
        self.movements_emotions.move_backward()

    def turn_left(self):
        self.movements_emotions.turn_left()

    def turn_right(self):
        self.movements_emotions.turn_right()

    def dance(self):
        self.movements_emotions.dance()

    def celebrate(self):
        self.movements_emotions.celebrate()

    def set_emotion(self):
        emotion = self.emotion_entry.text()
        self.movements_emotions.set_emotion(emotion)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyControllerApp()
    ex.show()
    sys.exit(app.exec())
