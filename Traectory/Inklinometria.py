import numpy as np
import matplotlib.pyplot as plt
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
        return f"Inklinometria (MD_array = {str(self.MD)}, INKL_array = {str(self.INKL)}), AZIM_array = {str(self.AZIM)}"
    
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