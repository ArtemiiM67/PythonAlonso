# PY5 IMPORTED MODE CODE
class tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.happiness = 100
        self.cleanliness = 100
        self.energy = 100
        self.alive = True
        self.age_frames = 0
        self.message = "Take care of your pet!"

        self.destroying = False
        self.destroy_start_frame = 0
        self.destroy_stage = 0

    def update(self):
        if self.destroying:
            elapsed = frame_count - self.destroy_start_frame

            if elapsed < 60:
                self.destroy_stage = 3
                self.message = self.name + " is now up for destruction in 3..."
            elif elapsed < 120:
                self.destroy_stage = 2
                self.message = self.name + " is now up for destruction in 2..."
            elif elapsed < 180:
                self.destroy_stage = 1
                self.message = self.name + " is now up for destruction in 1..."
            elif elapsed < 240:
                self.destroy_stage = 0
                self.message = "BOOM."
            else:
                self.destroying = False
                self.alive = False
                self.message = self.name + " has destroyed itself..."
            return

        if not self.alive:
            return

        self.age_frames += 1

        if frame_count % 45 == 0:
            self.hunger -= 2
        if frame_count % 60 == 0:
            self.happiness -= 2
        if frame_count % 75 == 0:
            self.cleanliness -= 2
        if frame_count % 90 == 0:
            self.energy -= 1

        self.hunger = max(0, min(100, self.hunger))
        self.happiness = max(0, min(100, self.happiness))
        self.cleanliness = max(0, min(100, self.cleanliness))
        self.energy = max(0, min(100, self.energy))

        if (
            self.hunger <= 0
            or self.happiness <= 0
            or self.cleanliness <= 0
            or self.energy <= 0
        ):
            self.alive = False
            self.message = self.name + " could not be cared for anymore..."

    def feed(self):
        if not self.alive or self.destroying:
            return
        self.hunger = min(100, self.hunger + 20)
        self.energy = max(0, self.energy - 2)
        self.message = "You fed " + self.name + "!"

    def play(self):
        if not self.alive or self.destroying:
            return
        self.happiness = min(100, self.happiness + 22)
        self.hunger = max(0, self.hunger - 6)
        self.energy = max(0, self.energy - 5)
        self.cleanliness = max(0, self.cleanliness - 4)
        self.message = self.name + " had fun!"

    def clean(self):
        if not self.alive or self.destroying:
            return
        self.cleanliness = min(100, self.cleanliness + 30)
        self.happiness = max(0, self.happiness - 2)
        self.message = self.name + " is nice and clean!"

    def secret_ending(self):
        if not self.alive or self.destroying:
            return
        self.destroying = True
        self.destroy_start_frame = frame_count
        self.destroy_stage = 3
        self.message = self.name + " is now up for destruction in 3..."

    def restart(self):
        self.hunger = 100
        self.happiness = 100
        self.cleanliness = 100
        self.energy = 100
        self.alive = True
        self.age_frames = 0
        self.message = "Take care of your pet!"
        self.destroying = False
        self.destroy_start_frame = 0
        self.destroy_stage = 0

    def age_seconds(self):
        return self.age_frames // 60

    def face_mood(self):
        if self.happiness > 60:
            return "happy"
        if self.happiness > 30:
            return "neutral"
        return "sad"