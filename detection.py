import threading  

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
                    self.obstacle_label.setText(f"Obstacle : Non détecté, Distance : {obstacle} cm")
            except Exception as e:
                print(f"Erreur lors de la détection des obstacles : {str(e)}")

    def act_on_color1(self, color):
        if color == "BleuC":
            self.marty.eyes('wiggle')
            self.marty.walk(num_steps=6, step_length=30, move_time=2000, blocking=True)
        elif color == "Rouge":
            self.marty.dance()
            self.marty.stop()
        elif color == "Jaune":
            self.marty.walk(num_steps=4, step_length=-30, move_time=2000, blocking=True)
        elif color == "Vert":
            self.marty.walk(num_steps=6, step_length=30, move_time=2000, blocking=True)
        elif color == "BleuM":
            self.marty.sidestep('right', steps=6, step_length=35, move_time=2000, blocking=True)
            self.marty.stand_straight()
        elif color == "Rose":
            self.marty.sidestep('left', steps=6, step_length=35, move_time=2000, blocking=True)
            self.marty.stand_straight()

    def detectMazeColors(self):
        directions1 = []
        for _ in range(2):
            detected_color = self.get_color_name()
            print("Couleur détectée", detected_color)
            directions1.append(detected_color)
            self.marty.walk(num_steps=3, step_length=25, move_time=2000, blocking=True)
        self.marty.sidestep('right', steps=4, step_length=25, move_time=2000, blocking=True)
        detected_color = self.get_color_name()
        directions1.append(detected_color)
        print("Couleur détectée", detected_color)
        for _ in range(2):
            self.marty.walk(num_steps=3, step_length=-25, move_time=2000, blocking=True)
            detected_color = self.get_color_name()
            print("Couleur détectée", detected_color)
            directions1.append(detected_color)
        self.marty.sidestep('right', steps=4, step_length=25, move_time=2000, blocking=True)
        detected_color = self.get_color_name()
        directions1.append(detected_color)
        print("Couleur détectée", detected_color)
        for _ in range(2):
            detected_color = self.get_color_name()
            print("Couleur détectée", detected_color)
            directions1.append(detected_color)
            self.marty.walk(num_steps=4, step_length=25, move_time=2000, blocking=True)

    def start_color_detection(self):
        if self.marty:
            mon_thread1 = threading.Thread(target=self.act_on_color1, args=(self.get_color_name(),))
            mon_thread1.start()

    def MazeColorDetect(self):
        matrice1, matrice2 = None, None
        if self.marty:
            mon_thread1 = threading.Thread(target=self.detectMazeColors)
            mon_thread1.start()
            matrice1 = self.detectMazeColors()
        if self.marty:
            mon_thread2 = threading.Thread(target=self.detectMazeColors)
            mon_thread2.start()
            matrice2 = self.detectMazeColors()
        if matrice1 and matrice2:
            self.merge_and_act_on_colors(matrice1, matrice2)

    def merge_and_act_on_colors(self, matrice1, matrice2):
        merged_colors = []
        for color1, color2 in zip(matrice1, matrice2):
            if color1 != "noir":
                merged_colors.append(color1)
            elif color2 != "noir":
                merged_colors.append(color2)

        for color in merged_colors:
            if self.marty:
                self.act_on_color1(color)

    def get_color_value(self, position):
        if self.marty:
            try:
                # Obtenez la valeur du capteur de couleur à la position spécifiée
                color_value = self.marty.get_color_sensor_reading(position)
                return color_value
            except Exception as e:
                print(f"Erreur lors de la détection de la couleur : {str(e)}")
                return None