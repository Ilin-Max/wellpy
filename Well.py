import numpy as np
from openpyxl import load_workbook
from pathlib import Path
from dataclasses import dataclass
from Traektory import Traektory


@dataclass
class Section():
    start: float
    end: float
    diameter: float

class Constructions():
    def __init__(self, ):
        self.sections: dict[str, Section] = {}
        self.count_sections = 0 
    
    def __str__(self):
        text = ""
        for key, value in self.sections.items():
            text += f"{key}: {value}\n"
        return text

    def test_name(self, name):
        return name in self.sections  

    def add_section(self,  section: Section, name = ''):
        self.count_sections += 1

        if not name:
            name = "Section_" + str(self.count_sections)
        
        repit_name = self.test_name(name)
        count_repit_name = 0
        while repit_name:
            count_repit_name += 1
            name = f"{name}_{count_repit_name}"
            repit_name = self.test_name(name)

        self.sections[name] = section
    
    def show(): # Написать логику отображения конструкции
        pass 

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
        self.HoleParametrs = Constructions()
        self.Perforations = Constructions()
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