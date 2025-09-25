from dataclasses import dataclass
from DataClassMenedger import DataClassMenedger
import matplotlib.pyplot as plt

@dataclass
class Pipes():
    length: float
    diameter_out: float
    diametr_in: float
    massa: float

class PipesMenedger(DataClassMenedger):
    def __init__(self):
        super().__init__(Pipes)
        self._sections_name = "Pipes"
        self._name_set_sections = ""

    @property
    def sections(self):
        return self.objects 

    def add_section(self, *args, name = '',  length = None, diameter_out = None, diametr_in = None, massa = None):
        
        if len(args) == self._count_field_class:
            section = self._class_for_work(*args)
        else:
            section = self._class_for_work(length, diameter_out, diametr_in, massa)
        
        super().add_objects(name = name, object = section)

    def _setings_show(self):
        for sect in self.sections.values():
            y_coord = [sect.start, sect.stop]
            radius = sect.diameter/2
            plt.plot([-radius, -radius], y_coord, color = "black")
            plt.plot([radius, radius], y_coord, color = "black")

    def show(self):
        plt.figure(figsize=(8, 10))
        plt.title(self._name_set_sections)
        self._setings_show()
        ax = plt.gca()
        ax.invert_yaxis()
        plt.show()


