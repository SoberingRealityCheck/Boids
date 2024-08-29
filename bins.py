class Bin:
    def __init__(self, id):
        self.id = id
        self.XRange = []
        self.YRange = []
        self.PositionArray = []
        self.BoidIDArray = []


class BinBin:
    #Bin of Bins for all the Bins
    def __init__(self, Resolution, AwarenessRadius):
        self.BinCount = (int(Resolution / AwarenessRadius) ** 2)
        print(f"Binning Initialized. Resolution: {Resolution}, Awareness Radius: {AwarenessRadius}, Bin Count: {self.BinCount}")
        self.Resolution = Resolution
        self.AwarenessRadius = AwarenessRadius
        self.BinDict = {}
        self.CreateBins()
    
    def CreateBins(self):
        for BinNumber in range(self.BinCount):
            
            NewBin = Bin(BinNumber)
            self.BinDict[BinNumber] = NewBin

