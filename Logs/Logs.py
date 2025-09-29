import lasio
import numpy as np
import pandas as pd
from dataclasses import dataclass, field

@dataclass
class CurveItem():
    mnemonic: str
    unit: str = ""
    description: str = ""
    data: np.ndarray = field(default_factory=lambda: np.array([]))

class CurveStorage():
    def __init__(self, name_dataset = ""):
        self.сurves = []
        self._count_curve = 0
        self._object_name = "Curve"
        self._name_data_set = name_dataset
    
    # def __str__(self):
    #     df = self.to_df()
    #     return str(df)
   
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        
        if self._count_curve != other._count_curve:
            return False

        if self._count_curve == 0:
            return True

        return self.сurves == other.сurves

    def __ne__(self, other):
        return not self.__eq__(other)
    
    # def __getitem__(self, index):
    #     if type(index) == int:
    #         keys = list(self.objects)
    #         index =  keys[index]
    #     return self.objects[str(index)]
    
    # def __len__(self):
    #     return self._count_object
    
    # def _test_name(self, name):
    #     return name in self.objects

    # def add_objects(self, *args, object = None,  name = ''):
    #     if not name:
    #         name = self._object_name + "_" + str(self._count_object)
        
    #     repit_name = self._test_name(name)
    #     count_repit_name = 0
        
    #     while repit_name:
    #         count_repit_name += 1
    #         name = f"{name}_{count_repit_name}"
    #         repit_name = self._test_name(name)
        
    #     self.objects[name] = object
    #     self._count_object += 1

    # def to_df(self):        
    #     if self._count_object == 0:
    #         return pd.DataFrame(columns=["name"] + self._field_class_names)
        
    #     data = []
    #     for name, obj in self.objects.items():
    #         row = [name] + [getattr(obj, f.name) for f in fields(obj)]
    #         data.append(row)
        
    #     df = pd.DataFrame(data, columns=["name"] + self._field_class_names)
    #     return df

las = lasio.read(r"C:\Users\User7\Desktop\pa-13_WBS.las")
print(las.curves["CMW_MAX_TEN"])
CMW_MAX_TEN = las.curves["CMW_MAX_TEN"]
 
t = CurveItem("CMW_MAX_TEN", unit = CMW_MAX_TEN.unit, description = CMW_MAX_TEN.descr, data = CMW_MAX_TEN.data)
set = CurveStorage()
set.сurves.append(t)
print(set)