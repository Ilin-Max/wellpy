import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Inklinometria import Inklinometria
    
class Traektory():
    def __init__(self):
        self._step_of_depth = 0.1

        self._inklinometria = Inklinometria()
        self.X0 = 0
        self.Y0 = 0
        self.Z0 = 0

        self.MD = np.arange(0, np.max(self._inklinometria.MD) + self.step_of_depth, self.step_of_depth)
        self.AZIM = np.zeros_like(self.MD)
        self.INKL = np.zeros_like(self.MD)
        self.__mult_AZIM_INKL()

    def __mult_AZIM_INKL(self):
        for i in np.arange(len(self._inklinometria.MD) - 1):
            mask = (self.MD >= self._inklinometria.MD[i]) & (self.MD <= self._inklinometria.MD[i + 1])
            self.AZIM[mask] = self._inklinometria.AZIM[i]
            self.INKL[mask] = self._inklinometria.INKL[i]
        
        if len(self._inklinometria.MD) > 0:
            last_mask = self.MD >= self._inklinometria.MD[-1]
            self.AZIM[last_mask] = self._inklinometria.AZIM[-1]
            self.INKL[last_mask] = self._inklinometria.INKL[-1]

    def __Update_Traektory(self):
        self.MD = np.arange(0, np.max(self._inklinometria.MD) + self.step_of_depth, self.step_of_depth)
        self.__mult_AZIM_INKL()
    

    @property
    def step_of_depth(self):
        return self._step_of_depth
    
    @step_of_depth.setter
    def step_of_depth(self, value):
        self._step_of_depth = value
        self.__Update_Traektory()
        

    @property
    def delta_MD(self):
        return np.diff(self.MD)
    
    @property
    def middle_point_INKL(self):
        return self.INKL[:-1] + np.diff(self.INKL)/2
    
    @property
    def middle_point_AZIM(self):
        return self.AZIM[:-1] + np.diff(self.AZIM)/2
    
    @property
    def dX(self):
        dx = np.zeros(len(self.MD))
        dx[1:] = self.delta_MD * np.sin(np.radians(self.middle_point_INKL)) * np.sin(np.radians(self.middle_point_AZIM))
        return dx

    @property
    def dY(self):
        dy = np.zeros(len(self.MD))
        dy[1:] = self.delta_MD * np.sin(np.radians(self.middle_point_INKL)) * np.cos(np.radians(self.middle_point_AZIM))
        return dy

    @property
    def dZ(self):
        dz = np.zeros(len(self.MD)) 
        dz[1:] = self.delta_MD * np.cos(np.radians(self.middle_point_INKL))
        return dz

    @property
    def X(self):
         return self.X0 + np.cumsum(self.dX)

    @property
    def Y(self):
        return self.Y0 + np.cumsum(self.dY)

    @property
    def Z(self):
        return self.Z0 - np.cumsum(self.dZ)
    
    @property
    def TVD(self):
        return np.cumsum(self.dZ)
        
    def to_df(self):
        data = {
            "MD": self.MD,
            "AZIM": self.AZIM,
            "INKL": self.INKL,
            "TVD": self.TVD,
            "dX": self.dX,
            "dY": self.dY,
            "dZ": self.dZ,
            "X": self.X,
            "Y": self.Y,
            "Z": self.Z,
            }
        return pd.DataFrame(data)

    def show(self, name = "Traektory"):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.X, self.Y, self.Z, label=name, linewidth=2, color='blue')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Traektory')
        ax.set_zlim([np.min(self.Z), self.Z0])
        ax.legend()
        plt.show()
    



