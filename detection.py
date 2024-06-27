# detection.py
class Detection:
    def __init__(self, marty, battery_label, obstacle_label, color_label, ):
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
                
    def get_color_name(reading):
        if 10 <= reading < 13:
            return "Noir"  # [10,11,12,13]
        elif 14 <= reading < 17:
            return "Bleu"  # [14,15,16,17,18]
        elif 30 <= reading < 39:
            return "Bleu ciel"  # [30,31,33,34,35,36,37,38,39]
        elif 20 <= reading < 25:
            return "Vert"  # [20,21,22,23,24,25]
        elif 95 <= reading < 140:
            return "Jaune"
        elif 50 <= reading <= 66:
            return "Rouge"
        elif 80 <= reading < 90:
            return "Bleu marine"  # Ajoutez la plage correcte pour le bleu marine
        elif 60 <= reading < 70:
            return "Rose"  # Ajoutez la plage correcte pour le rose
        else:
            return "Couleur inconnue"

def detect_color(self):
    if self.marty:
        try:
            sensor_name = 'RiGhtColorSensor'  # Assurez-vous que le nom du capteur est correct

            while True:
                # Obtenez la lecture brute du capteur de couleur
                color_sensor_reading = self.marty.get_ground_sensor_reading(sensor_name)

                # Convertir la lecture brute en nom de couleur
                color_name = (color_sensor_reading)

                # Afficher le nom de la couleur
                print(f"Couleur détectée par le capteur {sensor_name}: {color_name}")

                # Effectuer des actions en fonction de la couleur détectée
                if color_name == "Bleu ciel":
                    self.marty.get_ready()
                    self.marty.walk(num_steps=4, start_foot='auto', turn=0)
                    self.marty.set_emotion('surprised')
                    self.marty.move_joint('eyes', -100, move_time=1000)
                    self.marty.move_joint('right_arm', 50, move_time=200)
                    self.marty.move_joint('left_arm', 50, move_time=200)
                    
                    
                elif color_name == "Jaune":
                    self.marty.walk(num_steps=5, start_foot='auto', turn=0)
                    self.marty.set_emotion('confused')
                    self.marty.move_joint('eyes', -50, move_time=1000)
                    self.marty.move_joint('right_arm', 50, move_time=200)
                    self.marty.move_joint('left_arm', -50, move_time=200)
            
                    
                elif color_name == "Vert":
                    self.marty.walk(num_steps=3, start_foot='auto', turn=0, )
                    self.marty.set_emotion('happy')
                    self.marty.move_joint('eyes', 0, move_time=1000)
                    self.marty.move_joint('right_arm', -10, move_time=200)
                    self.marty.move_joint('left_arm', -10, move_time=200)
                    
                elif color_name == "Bleu":
                    self.marty.walk(num_steps=4, start_foot='auto', step_length=35, )
                    self.marty.set_emotion('sad')
                    self.marty.move_joint('eyes', 50, move_time=1000)
                    
                    

                elif color_name == "Rose":
                    self.marty.sidestep('left',steps=6,step_length=35, move_time=2000)
                    self.marty.move_joint('eyes', 50, move_time=1000)
                    self.marty.move_joint('right_leg', 50, move_time=200)
                    self.marty.move_joint('left_leg', -50, move_time=200)

                elif color_name == "rouge":
                    self.marty.walk(num_steps=6, start_foot='auto', turn=0)
                    self.marty.set_emotion('angry')
                    self.marty.move_joint('eyes', -50, move_time=1000)
                    self.marty.move_joint('right_arm', 120, move_time=200)
                    self.marty.move_joint('left_arm', 120, move_time=200)

                    print("Couleur non reconnue ou aucune action définie pour cette couleur.")

                # Pause pour éviter une boucle infinie trop rapide
                #time.sleep(10)

        except Exception as e:
                 (f"Erreur lors de la détection de couleur : {e}")
        else:
                on_button_click("Marty n'est pas connecté.")
