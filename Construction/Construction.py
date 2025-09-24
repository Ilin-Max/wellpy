from .SectionsMenedger import SectionsMenedger
from .PipesMenedger import PipesMenedger
import matplotlib.pyplot as plt

class CaysingParametr(SectionsMenedger):
    def __init__(self):
        super().__init__()
        self._sections_name = "Casing"
        self._name_set_sections = "CaysingParametr"
        self.cementic = True
    
    def _setings_show(self):
        for sect in self.sections.values():
            y_coord = [sect.start, sect.stop]
            radius = sect.diameter/2
            plt.plot([-radius, -radius], y_coord, color = "Blue")
            plt.plot([radius, radius], y_coord, color = "Blue")

class HoleParametrs(SectionsMenedger):
    def __init__(self):
        super().__init__()
        self._sections_name = "Hole section"
        self._name_set_sections = "HoleParametrs"

class CementBridges(SectionsMenedger):
    def __init__(self):
        super().__init__()
        self._sections_name = "Cement bridge"
        self._name_set_sections = "CementBridges"

class Perforations(SectionsMenedger):
    def __init__(self):
        super().__init__()
        self._sections_name = "Perforation interval"
        self._name_set_sections = "Perforations"

class Construction():
    def __init__(self):
        self.HoleParametr = HoleParametrs()
        self.CaysingParametr = CaysingParametr()
        self.CementBridge = CementBridges()
        self.Perforations = Perforations()
    
    def __str__(self):
        Hole = str(self.HoleParametr)
        Caysing = str(self.CaysingParametr)
        Cement = str(self.CementBridge)
        Perfor = str(self.Perforations)
        return f"{str(Hole)}\n\n{str(Caysing)}\n\n{str(Cement)}\n\n{str(Perfor)}"
    
    def _setings_show(self):
        self.CaysingParametr._setings_show()
        self.HoleParametr._setings_show() 
        
    def show(self):
        plt.figure(figsize=(8, 10))
        plt.title("Construction")
        
        self._setings_show()
        
        ax = plt.gca()
        ax.invert_yaxis()
        ax.set_aspect(0.5)

        plt.show()