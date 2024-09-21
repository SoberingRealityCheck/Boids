import simulate, render


class BoidsProgram:
    '''
    Main Boids Program - calls the simulation and rendering functions + contains params that affect the simulation
    '''
    def __init__(self, 
                Width, 
                Height, 
                BoidCount, 
                SimResolution, 
                SimSpeed,
                MaxFramerate,
                Speed,  
                Reactivity, 
                AwarenessRadius, 
                MouseFollowStrength,
                ):
        self.BoidSimulation = simulate.Simulation(BoidCount, SimResolution, SimSpeed, Speed, Reactivity, AwarenessRadius, MouseFollowStrength)
        self.BoidRender = render.PygameRender(Width, Height, BoidCount, SimResolution, MaxFramerate, AwarenessRadius)
        self.Width = Width
        self.Height = Height
        self.SimResolution = SimResolution
        print("Boids Program Initialized.")
        self.RunningLoop()
        
    def RunningLoop(self):
        Running = True
        BoidSimulation = self.BoidSimulation
        BoidRender = self.BoidRender
        while Running:
            BoidSimulation.Update()
            BoidRender.PositionArray = BoidSimulation.PositionArray
            BoidRender.Update()
            Running = BoidRender.Running
            BoidSimulation.MouseX = BoidRender.MouseX * self.SimResolution / self.Width
            BoidSimulation.MouseY = BoidRender.MouseY * self.SimResolution / self.Height

if __name__ == "__main__":
    TestSim = BoidsProgram(
        Width = 1000, 
        Height = 800, 
        BoidCount = 100, 
        SimResolution = 201, 
        SimSpeed = .5,
        MaxFramerate = 120,
        Speed = 12,
        Reactivity = .01,
        AwarenessRadius = 10,
        MouseFollowStrength = .1,
        
        )
    