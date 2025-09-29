import numpy as np
from  Inklinometria import Inklinometria
    
class Traektory(Inklinometria):
    def __init__(self, x0=0, y0=0, z0=0,
                 inklinometria=None,
                 MD_array=None, INKL_array=None,
                 AZIM_array=None, step_of_depth=0.1):

        self._step_of_depth = step_of_depth
        self.X0 = x0
        self.Y0 = y0
        self.Z0 = z0
        # create or use object Inklinometria
        if inklinometria is None:
            self.inklinometria = Inklinometria(MD_array=MD_array, INKL_array=INKL_array, AZIM_array=AZIM_array)
        else:
            self.inklinometria = inklinometria
                     
        # create array MD with select step
        self.MD = np.arange(0, np.max(self.inklinometria.MD) + self._step_of_depth, self._step_of_depth)

        # interpolation data
        self.AZIM = np.zeros_like(self.MD)
        self.INKL = np.zeros_like(self.MD)
        self._mult_AZIM_INKL()
        
        # constructor class Inklinometria
        super().__init__(MD_array=self.MD, INKL_array=self.INKL, AZIM_array=self.AZIM)

    def _mult_AZIM_INKL(self):
        # interpolation data
        for i in range(len(self.inklinometria.MD) - 1):
            mask = (self.MD >= self.inklinometria.MD[i]) & (self.MD < self.inklinometria.MD[i + 1])
            self.AZIM[mask] = self.inklinometria.AZIM[i]
            self.INKL[mask] = self.inklinometria.INKL[i]
        
        # last point
        if len(self.inklinometria.MD) > 0:
            last_mask = self.MD >= self.inklinometria.MD[-1]
            self.AZIM[last_mask] = self.inklinometria.AZIM[-1]
        
    def _update_coord(self):
        super()._update_coord()
        # add starting coord
        self.X += self.X0
        self.Y += self.Y0
        self.Z += self.Z0
        self.TVD += self.Z0

MD = np.array([0, 10 , 20 , 100])
Az = np.array([10, 10 , 10 , 15])
inkl = np.array([0, 20 , 30 , 50])

t = Traektory(x0 = 10, y0 = 10, z0 = 20, MD_array = MD, AZIM_array=Az, INKL_array=inkl)
print(t)
t.show()