import pygame
import pygame.freetype
import numpy as np



class PygameRender:
    def __init__(self, Width, Height, BoidCount, Resolution, MaxFramerate, AwarenessRadius):
        self.Width = Width
        self.Height = Height
        self.screen = pygame.display.set_mode((Width, Height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
        self.font = pygame.freetype.SysFont("Times New Roman", 12)
        self.PositionArray = np.zeros((BoidCount, 3))
        self.Resolution = Resolution
        self.MaxFramerate = MaxFramerate
        self.AwarenessRadius = AwarenessRadius
        self.MouseX = 0
        self.MouseY = 0
        self.Running = True
        print("Render Initialized.")
        
    def RenderBoids(self):
        PositionArray = self.PositionArray
        Resolution = self.Resolution
        Width = self.Width
        Height = self.Height
        for Boid in PositionArray:
            color = [float(255*Boid[0]/Resolution), float(255*Boid[1]/Resolution), 150]
            RenderPosition = (Width*Boid[0]/Resolution, Height*Boid[1]/Resolution)
            pygame.draw.circle(self.screen, color, RenderPosition, 2)
        
    def RenderFPS(self):
        dt = self.clock.tick(self.MaxFramerate) / 1000
        if dt != 0:
            fps = int(10/dt)/10
            self.font.render_to(self.screen,(20,20),f"fps: {fps}",(255,255,255))
            
    def RenderBins(self):
        Resolution = self.Resolution
        AwarenessRadius = self.AwarenessRadius 
        PartitionCount = int(Resolution / AwarenessRadius)
        ScaledRadiusX = AwarenessRadius * self.Width / Resolution
        ScaledRadiusY = AwarenessRadius * self.Height / Resolution
        for i in range(PartitionCount):
            pygame.draw.line(self.screen,(50,50,50),(i*ScaledRadiusX,0),(i*ScaledRadiusX, self.Height))
        for i in range(PartitionCount):
            pygame.draw.line(self.screen,(50,50,50),(0,i*ScaledRadiusY),(self.Width,i*ScaledRadiusY))
    
    def UpdateInputs(self):
        MouseX, MouseY = pygame.mouse.get_pos()
        self.MouseX = MouseX
        self.MouseY = MouseY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False
    
    def Update(self):
        self.screen.fill((10,10,10))
        self.UpdateInputs()
        self.RenderBoids()
        self.RenderFPS()
        self.RenderBins()
        pygame.display.update() 
        
        
