import numpy as np 
import goals, bins


class Simulation:
    def __init__(self, 
                BoidCount = 100, 
                Resolution = 500, 
                SimSpeed = 1,
                Speed = 1,
                Reactivity = 1,
                AwarenessRadius = 1,
                MouseFollowStrength = 1
                ):
        rng = np.random.default_rng(54321)
        self.BoidCount = BoidCount
        self.PositionArray = rng.random((BoidCount,2)) * np.array([Resolution, Resolution])
        self.VelocityArray = (rng.random((BoidCount,2)) - 0.5) * 2 * Speed
        self.GoalsArray = goals.GoalsArray(BoidCount, MouseFollowStrength)
        print("Simulation Initialized.")
        self.MouseX = 0
        self.MouseY = 0
        self.SimSpeed = SimSpeed
        self.Resolution = Resolution
        self.Speed = Speed
        self.Reactivity = Reactivity
        self.AwarenessRadius = AwarenessRadius
        self.BinBin = bins.BinBin(Resolution, AwarenessRadius)

    def UpdatePositions(self):
        OldPositionArray = self.PositionArray
        self.PositionArray = OldPositionArray + self.VelocityArray * self.SimSpeed 
        #Boids loop when reaching edges
        self.PositionArray = self.PositionArray % self.Resolution
        
    def UpdateVelocities(self):
        self.VelocityArray = (self.VelocityArray + self.Reactivity * self.GoalsArray.Goals * self.SimSpeed * self.Speed) / (self.Reactivity * self.SimSpeed + 1)
    
    def UpdateGoals(self):
        self.GoalsArray.Update(self.PositionArray, self.VelocityArray, self.MouseX, self.MouseY)
    
    def UpdateBins(self):
        pass
        
    
    def Update(self):
        self.UpdateBins()
        self.UpdatePositions()
        self.UpdateVelocities()
        self.UpdateGoals()

def TestSimulate():
    TestSim = Simulation(15,100)
    print(TestSim.PositionArray)
    print("updating positions.")
    TestSim.UpdatePositions()
    print(TestSim.PositionArray)


if __name__ == "__main__":
    TestSimulate()