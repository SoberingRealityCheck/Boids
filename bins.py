from numba import jit

class Bin:
    def __init__(self, id):
        self.id = id
        self.XRange = []
        self.YRange = []
        self.PositionArray = []
        self.BoidIDArray = []


class BinBin:
    #Bin of Bins for all the Bins
    def __init__(self, Resolution, AwarenessRadius, PositionArray):
        self.BinCount = (int(Resolution / AwarenessRadius) ** 2)
        print(f"Binning Initialized. Resolution: {Resolution}, Awareness Radius: {AwarenessRadius}, Bin Count: {self.BinCount}")
        self.Resolution = Resolution
        self.AwarenessRadius = AwarenessRadius
        self.PositionArray = PositionArray
        self.BinDict = {}
        self.CreateBins()
    
    def CreateBins(self):
        BinNumber = 0
        for XNumber in range(int(self.Resolution / self.AwarenessRadius)):
            for YNumber in range(int(self.Resolution / self.AwarenessRadius)):
                NewBin = Bin(BinNumber)
                NewBin.XRange = XNumber * self.AwarenessRadius
                NewBin.YRange = YNumber * self.AwarenessRadius
                print("X: ", NewBin.XRange, " - - - Y: ", NewBin.YRange)
                self.BinDict[BinNumber] = NewBin
                BinNumber += 1
        print("Bins Created.")
        print("Bin Dict:")
        print(self.BinDict)
        
    def AssignBoidsToBins(self):
        for BoidNumber, BoidPosition in enumerate(self.PositionArray):
            BoidXNumber = int(BoidPosition[0] / self.AwarenessRadius)
            BoidYNumber = int(BoidPosition[1] / self.AwarenessRadius)
            #Need to finish this. Currently thinking of initially assigning all the bins on startup
            #but just checking when boids "swap bins" after that for a much faster binning experience
            #unsure exactly how much faster that is but it should definitely improve performance as opposed to 
            #resetting and reassigning bins every single frame, which was what the original idea was. 
            
            #if this plan doesn't work, a solid workable middle ground would probably be only binning once every four frames
            #although with the current setup, doing that might create pretty annoying stutter on those frames
            #MatchingBinId = BoidYNumber
            
            #structure of this approach:
                #initially define bin ranges
                #sort boids into bins (by putting their pos index in a new 'bins' list?)
                #each step of the simulation: 
                    #check if boids have exited the range of their specific bin
                        #if so, check & reassign boid to new bin
                    #return boids their bin + neighbor bins as "neighbors" array for movement logic calculations
                

