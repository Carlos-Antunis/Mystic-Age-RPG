import json

class player:
    level = 1
    def __init__(self,PlayerName, PlayerRace, PlayerOccupation):
        #Name of the player
        self.name = PlayerName
        #Race of the player
        self.race = PlayerRace.lower()
        with open(f'./Assets/Races/{self.race}.json') as source:
            self.stats = json.load(source)
            self.stats["HP"]["Current"] = self.stats["HP"]["full"]
            self.stats["MP"]["Current"] = self.stats["MP"]["full"]
        #Occupation of the player
        self.occupation = PlayerOccupation.lower()
        with open(f'./Assets/Occupations/{self.occupation}.json') as source:
            self.evolve = json.load(source)