import numpy as np
from Traektory import Traektory
from Constructions import Constructions, HoleParametrs

class Well():
    def __init__(self):
        self.Name = ""
        self.DateStartDrilling = "" # make data object
        self.DateEndDrilling = "" # make data object
        self.DeapSee = 0
        self.DensitySeeWather = 1.03
        self.Long = ""
        self.Land = ""
        self.Constructions = Constructions()
        self.HoleParametrs = HoleParametrs()
        self.Perforations = ""
        self.Traektory = Traektory()
        self.Traektory.Z0 = self.KB
        self.DataSet = ""
        self.GIS = ""
        self.TimeLogs = ""
        self.Deaplogs = ""
    

    
    @property
    def KB(self):
        return self.Traektory.Z0
    
    @property
    def X_coord(self):
        return self.Traektory.X0
    
    @property
    def Y_coord(self):
        return self.Traektory.Y0
    
    @KB.setter
    def KB(self, value):
        self.Traektory.Z0 = value
    
    @X_coord.setter
    def X_coord(self, value):
        self.Traektory.X0 = value

    @Y_coord.setter
    def X_coord(self, value):
        self.Traektory.Y0 = value