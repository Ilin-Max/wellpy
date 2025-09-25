
from dataclasses import dataclass, fields
import pandas as pd
import matplotlib.pyplot as plt

class DataClassMenedger():
    def __init__(self, class_for_work):
        self.objects = {}
        self._class_for_work = class_for_work
        self._field_class_names = [f.name for f in fields(self._class_for_work)]
        self._count_field_class = len(self._field_class_names)
        self._count_object = 0
        self._object_name = "Object"
        self._name_set_sections = ""
    
    def __str__(self):
        title = self._name_set_sections
        separator = "=" * len(title)

        if self._count_object == 0:
            return f"{separator}\n{title}\n{separator}"
        
        df = self.to_df()

        if title:
            return f"{separator}\n{title}\n{separator}\n{df}\n{separator}"
        else:
            return str(df)
   
    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        
        if self._count_object != other._count_object:
            return False

        if self._count_object == 0:
            return True

        for i in range(self._count_object):
            keys_self = list(self.objects.keys())
            keys_other = list(other.objects.keys())
            if self.objects[keys_self[i]] != other.objects[keys_other[i]]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __getitem__(self, index):
        if type(index) == int:
            keys = list(self.objects.keys())
            index =  keys[index]
        return self.objects[str(index)]
    
    def __len__(self):
        return self._count_object
    
    def _test_name(self, name):
        return name in self.objects

    def add_objects(self, *args, object = None,  name = ''):
        if not name:
            name = self._object_name + "_" + str(self._count_object)
        
        repit_name = self._test_name(name)
        count_repit_name = 0
        
        while repit_name:
            count_repit_name += 1
            name = f"{name}_{count_repit_name}"
            repit_name = self._test_name(name)
        
        self.objects[name] = object
        self._count_object += 1

    def to_df(self):        
        if self._count_object == 0:
            return pd.DataFrame(columns=["name"] + self._field_class_names)
        
        data = []
        for name, obj in self.objects.items():
            row = [name] + [getattr(obj, f.name) for f in fields(obj)]
            data.append(row)
        
        df = pd.DataFrame(data, columns=["name"] + self._field_class_names)
        return df   
        