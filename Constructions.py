from dataclasses import dataclass
import pandas as pd


@dataclass
class Section():
    start: float
    stop: float
    diameter: float

    def __str__(self):
        return f"{self.start}-{self.stop} diameter = {self.diameter}"
    

class SectionsMenedger():
    def __init__(self, ):
        self.sections: dict[str, Section] = {}
        self._count_sections = 0
        self._sections_name = "Section"
        self._name_set_sections = ""
    
    def __str__(self):
        title = self._name_set_sections
        separator = "=" * len(title)

        if self.count_sections == 0:
            return f"{separator}\n{title}\n{separator}"
        
        df = self.to_df()

        if title:
            return f"{separator}\n{title}\n{separator}\n{df}\n{separator}"
        else:
            return str(df)
   
    def __eq__(self, other):
        
        if type(self) is not type(other):
            return False
        
        if self._count_sections != other._count_sections:
            return False

        if self._count_sections == 0:
            return True

        for i in range(self._count_sections):
            keys_self = list(self.sections.keys())
            keys_other = list(other.sections.keys())
            if self.sections[keys_self[i]] != other.sections[keys_other[i]]:
                return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __getitem__(self, index):
        if type(index) == int:
            keys = list(self.sections.keys())
            index =  keys[index]
        return self.sections[str(index)]
    
    def __len__(self):
        return len(self._count_sections)
    
    @property
    def count_sections(self):
        return self._count_sections
    
    def _test_name(self, name):
        return name in self.sections

    def add_section(self, name = '',  section = None, start = None, stop = None, diameter = None):
        def add(name, section):
            if not name:
                name = self._sections_name + "_" + str(self._count_sections)
            
            repit_name = self._test_name(name)
            count_repit_name = 0
            
            while repit_name:
                count_repit_name += 1
                name = f"{name}_{count_repit_name}"
                repit_name = self._test_name(name)

            self.sections[name] = section
            self._count_sections += 1

        if section is not None:
            add(name, section)
        else:
            add(name, Section(start=start, stop = stop, diameter = diameter))

    def to_df(self):
        name = []
        start = []
        stop = []
        diametr = []
        for key, value in self.sections.items():
            name.append(key)
            start.append(value.start)
            stop.append(value.stop)
            diametr.append(value.diameter)
        data = {
                "Name": name,
                "Start": start,
                "Stop": stop,
                "diametr": diametr
            }
        return pd.DataFrame(data)
    
    def show(self): # Написать логику отображения секций
        pass 

class CaysingParametr(SectionsMenedger):
    def __init__(self):
        super().__init__()
        self._sections_name = "Casing"
        self._name_set_sections = "CaysingParametr"
        self.cementic = True

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
    
    