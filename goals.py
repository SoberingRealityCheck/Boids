import numpy as np


class GoalsArray:
    def __init__(self, BoidCount, MouseFollowStrength):
        self.BoidCount = BoidCount
        self.Goals = np.zeros((BoidCount, 2))
        self.PositionArray = np.zeros((BoidCount, 2))
        self.VelocityArray = np.zeros((BoidCount, 2))
        self.MouseX = 0
        self.MouseY = 0
        self.MouseFollowStrength = MouseFollowStrength
        
    
    def FollowMouse(self):
        MouseFollowStrength = self.MouseFollowStrength
        MouseGoals = np.array([self.MouseX, self.MouseY]) - self.PositionArray
        MouseGoalIntensity = np.reshape(np.linalg.norm((MouseGoals),axis=1),(-1,1))
        MouseGoals= MouseFollowStrength * MouseGoals / MouseGoalIntensity
        self.Goals += MouseGoals
    
    def NormalizeGoals(self):
        GoalIntensity = np.reshape(np.linalg.norm((self.Goals),axis=1),(-1,1))
        self.Goals = self.Goals / GoalIntensity
        
    def Update(self, PositionArray, VelocityArray, MouseX, MouseY):
        #update class values with given inputs
        self.PositionArray = PositionArray
        self.VelocityArray = VelocityArray
        self.MouseX = MouseX
        self.MouseY = MouseY
        
        #goal logic
        self.FollowMouse()
        self.NormalizeGoals()
        