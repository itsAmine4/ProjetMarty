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

    def detect_color(self):
        if self.marty:
            try:
                position = "left"
                color = self.marty.get_ground_sensor_reading('left')
                lcolor = 'unknown'  # Initialisation de la variable lcolor
                if 15 <= color <= 17:
                    lcolor = 'black'
                elif 19 <= color <= 22:
                    lcolor = 'darkblue'
                    self.marty.sidestep(direction='right', num_steps=3, step_length=50, move_time=1000, blocking=True)
                elif 30 <= color <= 34:
                    lcolor = 'green'
                    self.marty.walk(num_steps=4, step_length=40, move_time=1500, blocking=True)
                elif 52 <= color <= 55:
                    lcolor = 'skyblue'
                    self.marty.walk(num_steps=4, step_length=40, move_time=1500, blocking=True)
                elif 82 <= color <= 85:
                    lcolor = 'red'
                    self.marty.stop()
                elif 95 <= color <= 98:
                    lcolor = 'pink'
                    self.marty.sidestep(direction='right', num_steps=3, step_length=50, move_time=1000, blocking=True)
                elif 110 <= color <= 118:
                    lcolor = 'white'
                elif 180 <= color <= 185:
                    lcolor = 'yellow'
                    self.marty.walk(num_steps=4, step_length=-25, move_time=1500, blocking=True)
                self.color_label.setText(f"Couleur détectée ({position}) : {lcolor}")
            except Exception as e:
                print(f"Erreur lors de la détection de la couleur : {str(e)}")
                
    def color_to_hex(self, color_name):
        # Dictionnaire de conversion des noms de couleurs en codes hexadécimaux
        color_hex_map = {
            'red': '#FF0000',
            'green': '#00FF00',
            'blue': '#0000FF',
            'yellow': '#FFFF00',
            'cyan': '#00FFFF',
            'magenta': '#FF00FF',
            'black': '#000000',
            'white': '#FFFFFF',
            'orange': '#FFA500',
            'purple': '#800080',
            'pink': '#FFC0CB',
            # Ajoutez d'autres couleurs si nécessaire
        }
        return color_hex_map.get(color_name.lower(), '#000000')