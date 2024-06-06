# detection.py
class Detection:
    def __init__(self, marty, battery_label, obstacle_label, color_label):
        self.marty = marty
        self.battery_label = battery_label
        self.obstacle_label = obstacle_label
        self.color_label = color_label

    def update_sensors(self):
        if self.marty:
            try:
                battery_level = self.marty.get_battery_remaining()
                self.battery_label.setText(f"Niveau de batterie : {battery_level}%")
            except Exception as e:
                print(f"Erreur lors de la mise à jour des capteurs : {str(e)}")

    def check_for_obstacles(self):
        if self.marty:
            try:
                obstacle = self.marty.get_distance_sensor()
                if obstacle < 5:
                    self.obstacle_label.setText(f"Obstacle : Détecté à {obstacle} cm")
                else:
# detection.py (suite)
                    self.obstacle_label.setText(f"Obstacle : Non détecté, Distance : {obstacle} cm")
            except Exception as e:
                print(f"Erreur lors de la détection des obstacles : {str(e)}")

    def detect_color(self):
        if self.marty:
            try:
                # Remplacez 'centre' par 'left' ou 'right' selon votre configuration
                color = self.marty.get_color_sensor_color('left')
                self.color_label.setText(f"Couleur détectée : {color}")
            except Exception as e:
                print(f"Erreur lors de la détection de la couleur : {str(e)}")
