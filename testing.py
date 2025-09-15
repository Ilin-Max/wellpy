from Well import Well, Section
from Traektory import Traektory, Inklinometria
import numpy as np



well = Well()
well.Name = "PA-101"
well.KB = 67

hole1 = Section(start = 0, end = 505, diameter=650)
hole2 = Section(start = 505, end = 1805, diameter=500)
conductor = Section(start=0, end=500, diameter=600)
tech  = Section(start = conductor.end, end = 1800, diameter=420)

well.Constructions.add_section(conductor, name = "Conductor")
well.Constructions.add_section(tech, name = "Tech")
well.HoleParametrs.add_section(hole1)
well.HoleParametrs.add_section(hole2)

well.Traektory.inklinometria.INKL = np.ndarray[45, 45]

print(well.Constructions)
print(well.HoleParametrs)
print(well.Traektory.show())
