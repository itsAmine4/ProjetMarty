# mouvements_emotions.py
class MovementsEmotions:
    def __init__(self, marty):
        self.marty = marty
        

    def stand_straight(self):
        if self.marty:
            self.marty.stand(num_steps=0, step_length=0, move_time=0, blocking=True)

    
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

    def set_emotion(self, emotion):
        if self.marty:
            try:
                if emotion.lower() == "happy":
                    self.marty.move_joint('eyes', 0, move_time=1000)
                    self.marty.move_joint('right_arm', -10, move_time=200)
                    self.marty.move_joint('left_arm', -10, move_time=200)
                    
                elif emotion.lower() == "angry":
                    self.marty.move_joint('eyes', -50, move_time=1000)
                elif emotion.lower() == "sad":
                    self.marty.move_joint('eyes', 50, move_time=1000)
                elif emotion.lower() == "surprised":
                    self.marty.move_joint('eyes', -100, move_time=1000)
                    self.marty.move_joint('right_leg', 50, move_time=200)
                    self.marty.move_joint('left_leg', -50, move_time=200)
                    
                elif emotion.lower() == "confused":
                    self.marty.move_joint('eyes', -50, move_time=1000)
                    self.marty.move_joint('right_arm', 50, move_time=200)
                    self.marty.move_joint('left_arm', -50, move_time=200)
            
                    
                elif emotion.lower() == "excited":
                    self.marty.move_joint('eyes', -5, move_time=200)
                    self.marty.move_joint('eyes', 15, move_time=200)
                    self.marty.move_joint('eyes', -5, move_time=200)
                    self.marty.move_joint('eyes', 15, move_time=200)
                    self.marty.move_joint('eyes', 0, move_time=200)
                    self.marty.move_joint('right_arm', -50, move_time=200)
                    self.marty.move_joint('left_arm', 50, move_time=200)
                    self.marty.move_joint('right_arm', 50, move_time=200)
                    self.marty.move_joint('left_arm', -50, move_time=200)
                else:
                    print("Emotion non reconnue")
            except AttributeError as e:
                print(f"Erreur : {str(e)}")
