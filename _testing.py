from Well import Well
from Constructions import Section
import numpy as np

well = Well()
well.Name = "PA-101"
well.KB = 67

hole1 = Section(start = 0, stop = 505, diameter=650)
hole2 = Section(start = 505, stop = 1805, diameter=500)
conductor = Section(start=0, stop=500, diameter=600)
tech  = Section(start = conductor.stop, stop = 1800, diameter=420)

well.Constructions.add_section(section = conductor, name = "Conductor")
well.Constructions.add_section(section = tech, name = "Tech")
well.HoleParametrs.add_section(start = 0, stop = 505, diameter=650)
well.HoleParametrs.add_section(start = 505, stop = 1805, diameter=500)

print(well.Constructions)
print(well.HoleParametrs)
