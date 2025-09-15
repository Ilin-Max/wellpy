from dataclasses import dataclass, field
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Inklinometria():
    def __init__(self, MD_array = None, INKL_array = None, AZIM_array = None):
        
        self._MD = np.arange(0, 1000, 10) if MD_array is None else MD_array
        self.__shape = len(self._MD)
        
        if INKL_array is None:
            self._INKL = np.zeros(self.__shape)
        else:
            self._INKL  = INKL_array
        
        if AZIM_array is None:
            self._AZIM = np.zeros(self.__shape)
        else:
            self._AZIM  = AZIM_array    

        self.dX = np.zeros(self.__shape)
        self.dY = np.zeros(self.__shape)   
        self.dZ = np.zeros(self.__shape)
        self.X = np.zeros(self.__shape)
        self.Y = np.zeros(self.__shape)
        self.Z = np.zeros(self.__shape)
        self.TVD = np.zeros(self.__shape)
        
        self.__update_inkl()



    def __repr__(self):
        return f"Inklinometria (MD_array = {self.MD}, INKL_array = {self.INKL}), AZIM_array = {self.AZIM}"
    
    def __str__(self):
        return f"{self.to_df()}"
    
    def __eq__(self, other):
        if not isinstance(other, Inklinometria):
            return False
        
        return (
            np.array_equal(self.MD, other.MD) and
            np.array_equal(self.INKL, other.INKL) and
            np.array_equal(self.AZIM, other.AZIM)
        )
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __update_inkl(self):
        delta_MD = np.diff(self.MD)
        middle_point_INKL = self.INKL[:-1] + np.diff(self.INKL)/2
        middle_point_AZIM = self.AZIM[:-1] + np.diff(self.AZIM)/2
        self.dX[1:] = delta_MD * np.sin(np.radians(middle_point_INKL)) * np.sin(np.radians(middle_point_AZIM))
        self.dY[1:] = delta_MD * np.sin(np.radians(middle_point_INKL)) * np.cos(np.radians(middle_point_AZIM))
        self.dZ[1:] = -delta_MD * np.cos(np.radians(middle_point_INKL))
        self.X = np.cumsum(self.dX)
        self.Y = np.cumsum(self.dY)
        self.Z = np.cumsum(self.dZ)
        self.TVD = self.Z

    @property
    def MD(self):
        return self._MD
    
    @property
    def INKL(self):
        return self._INKL
    
    @property
    def AZIM(self):
        return self._AZIM
    
    @MD.setter
    def MD(self, value):
        self._MD = value
        self.__update_inkl()
    
    @INKL.setter
    def INKL(self, value):
        self._INKL = value
        self.__update_inkl()
    
    @AZIM.setter
    def AZIM(self, value):
        self._AZIM = value
        self.__update_inkl()


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
        ax.legend()
        plt.show()

    
class Traektory():
    def __init__(self):
        self._step_of_depth = 0.1

        self.inklinometria = Inklinometria()
        self.X0 = 0
        self.Y0 = 0
        self.Z0 = 0

        self.MD = np.arange(0, np.max(self._inklinometria.MD) + self.step_of_depth, self.step_of_depth)
        self.AZIM = np.zeros_like(self.MD)
        self.INKL = np.zeros_like(self.MD)
        self.__mult_AZIM_INKL()

        self.__old_inklinometria = self.inklinometria

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
    


md = np.arange(0, 1000, 10)
azim = np.ones_like(md)
inkl = np.ones_like(md) * 30
inkl_test = Inklinometria(MD_array=md, INKL_array=inkl, AZIM_array = azim)

inkl_test.show()



