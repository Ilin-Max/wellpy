import lasio
import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from time import time
from union_functions import linear_interpolation
import matplotlib.pyplot as plt

@dataclass
class CurveItem():
    mnemonic: str
    unit: str = ""
    value: str = ""
    description: str = ""
    original_mnemonic: str = ""
    data: np.ndarray = field(default_factory=lambda: np.array([]))


class LogsStorage():
    def __init__(self, *args, name_dataset = "Curves"):
        self.name_data_set = name_dataset
        self._mnemonic_unilites_curve = "Data" 

        self.curves = []
        self._list_name_mnemonic = []
        
        for curve in args:
            if type(curve) != CurveItem:
                continue
            else:
                self.curves.extend(args)
                self._list_name_mnemonic.extend(args.mnemonic)

    def __repr__(self):
        return f"CurveItemStorage(name_dataset = {self.name_data_set})"
        
    def __str__(self):
        return f"{self.name_data_set}: {self._list_name_mnemonic}"
    
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        
        if self._count_curve != other._count_curve:
            return False

        if self._count_curve == 0:
            return True

        return self.curves == other.curves

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __len__(self):
        return len(self.curves)
    
    def __getitem__(self, index):
        
        if type(index) == int:
            return self.curves[index]
        
        elif type(index) == str:
            try:
                curve_index = self._list_name_mnemonic.index(index)  
                return self.curves[curve_index]
            
            except ValueError:
                raise Exception(f"Dataset don't have curve '{index}'\n{str(self)}")

            
    @property
    def index(self):
        try: 
            if len(self.curves) > 0:
                index_array = self.curves[0].data
            else:
                index_array = np.array([])
        except Exception as e:
            print(f"Error getting index: {e}")
            index_array = np.array([])
        return index_array
    
    @property
    def steps(self):
        if len(self.index) != 0:
            return np.diff(self.index)
        else: return []
    
    @property
    def step(self):
        steps = self.steps
        if len(steps) != 0:
            constant_step =  steps[0]
            if np.all(steps != constant_step):
                raise Exception(f"{self.name_data_set}: index array dont have constant step")
            else:
                return(constant_step)
    
    def read_las(self, las_file):
        def add_curves_from_lasioLASFile(self, las):
            for curve in las.curves:
                mnemonic = curve.mnemonic
                unit = curve.unit
                value = curve.value
                description = curve.descr
                original_mnemonic = curve.original_mnemonic
                data = curve.data
                curve = CurveItem(mnemonic, unit, value, description, original_mnemonic,data)
                self._list_name_mnemonic.append(mnemonic)
                self.curves.append(curve)
        if type(las_file) == lasio.LASFile:
            add_curves_from_lasioLASFile(self, las_file)
        else:
            try:
                las = lasio.read(las_file)
                add_curves_from_lasioLASFile(self, las)
            except Exception as e:
                print(e)
    
    def read_exel(self):
        pass

    def to_df():
        pass

    def to_exel():
        pass
    
    def to_las():
        pass


las_path = r"C:\Users\User7\Desktop\pa-13_WBS.las"

data_set = LogsStorage()
data_set.read_las(r"C:\Users\User7\Desktop\pa-13_WBS.las")


curve = data_set['CMW_MAX_TEN'].data
md = np.arange(0, 10000, 0.1)
new_curve = linear_interpolation(md, data_set.index, curve)
print(new_curve)

plt.plot(curve, data_set.index)
plt.plot(new_curve, md)
plt.show()
