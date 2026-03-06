class SubwayStation:
    def __init__(self, theName, theBorough, theLines):
        self.name = theName
        self.borough = theBorough
        self.lines = theLines
        self.elevator = False
        
    def updateElevator(self, newElevator):
        self.elevator = newElevator

yankeeStadium = SubwayStation("161 St - Yankee Stadium", "Bronx", ["B", "D", 4])
#print(vars(yankeeStadium))

yankeeStadium.newElevator = True

for attr, value in vars(yankeeStadium).items():
    print(f"\t{attr} : {value}")