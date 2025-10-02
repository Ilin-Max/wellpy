import numpy as np
from Construction.Construction import Construction
from Traectory.Traectory import Traektory
from Logs.Logs import CurveItemStorage
import matplotlib.pyplot as plt

class Well():
    def __init__(self):
        self.Name = ""
        self.DateStartDrilling = "" # make data object
        self.DateEndDrilling = "" # make data object
        self.DeapSee = 0
        self.DensitySeeWather = 1.03
        self.Long = ""
        self.Land = ""
        self.Constructions = Construction()
        self.Traektory = Traektory()
        self.Traektory.Z0 = self.KB
        self.DataSet = CurveItemStorage()
        self.TimeLogs = CurveItemStorage()
        self.Deaplogs = CurveItemStorage()

    def new_Traectory(self, MD_array = None, INKL_array = None, AZIM_array = None):
        self.Traektory = Traektory(MD_array = MD_array, INKL_array = INKL_array, AZIM_array = AZIM_array, \
                                   x0 = self.X_coord, y0 = self.Y_coord, z0 = self.KB) 
    
    def show_Traectory(self):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        self.Traektory._setings_show(ax, name = self.Name)

        caysings = self.Constructions.CaysingParametr.sections
        for name, caysing in caysings.items():
            index_coord = np.where(self.Traektory.MD >= caysing.stop)[0][0]
            
            x_shoe = self.Traektory.X[index_coord]
            y_shoe = self.Traektory.Y[index_coord]
            z_shoe = self.Traektory.Z[index_coord]
            ax.scatter(x_shoe, y_shoe, z_shoe, 
                    marker='o', s=10, color='red',)
            ax.text(x_shoe, y_shoe, z_shoe, f"{name}: {caysing.diameter}")
        
        plt.show()
    
    def show_Construction(self):
        self.Constructions.show()

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
        self.Traektory._update_coord()
    
    @X_coord.setter
    def X_coord(self, value):
        self.Traektory.X0 = value
        self.Traektory._update_coord()
    
    @Y_coord.setter
    def Y_coord(self, value):
        self.Traektory.Y0 = value
        self.Traektory._update_coord()