import lasio
import numpy as np
import pandas as pd
from dataclasses import dataclass, field

@dataclass
class CurveItem():
    mnemonic: str
    unit: str = ""
    value: str = ""
    description: str = ""
    original_mnemonic: str = ""
    data: np.ndarray = field(default_factory=lambda: np.array([]))


class CurveItemStorage():
    def __init__(self, *args, name_dataset = "CurveStorange"):
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
        return self._count_object
    
    def read_las(self, las_file):
        print(type(las_file))
        
        def add_curves_from_lasioLASFile(self, las):
            for i in range(len(las.curves())):
                las_curve = las.curves[i]
                mnemonic = las_curve.mnemonic
                unit = las_curve.unit
                value = las_curve.value
                description = las_curve.descr
                original_mnemonic = las_curve.original_mnemonic
                data = las_curve.data
                curve = CurveItem(mnemonic, unit, value, description, original_mnemonic,data)
                print(curve)
                self._list_name_mnemonic.append()
                self.curves.append(curve)
        

        if type(las_file) == lasio.LASFile:
            add_curves_from_lasioLASFile(self, las_file)
        
        else:
            try:
                las = lasio.read(las_file)
                add_curves_from_lasioLASFile(self, las)
            
            except Exception as e:
                print(e)
    
    def to_df():
        pass

    def to_exel():
        pass

las = lasio.read(r"C:\Users\User7\Desktop\pa-13_WBS.las")
print(las.curves["CMW_MAX_TEN"])
CMW_MAX_TEN = las.curves["CMW_MAX_TEN"]
 
t = CurveItem("CMW_MAX_TEN", unit = CMW_MAX_TEN.unit, description = CMW_MAX_TEN.descr, data = CMW_MAX_TEN.data)

data_set = CurveItemStorage()
data_set.read_las(las)

print(data_set)


