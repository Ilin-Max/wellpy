from Well import Well
from Construction.SectionsMenedger import Section
import numpy as np
import time 

t_start = time.time()

well = Well()
well.Name = "P13"
well.KB = 42.15
well.DeapSee = 61.65
well.DensitySeeWather = 1.03

well.Constructions.HoleParametr.add_section(start= 0, stop=567.12, diameter=584.2)
well.Constructions.HoleParametr.add_section(start= 567.12, stop=2843.3, diameter=444.5)
well.Constructions.HoleParametr.add_section(start = 2843.3, stop = 4319.21, diameter=311.2)
well.Constructions.HoleParametr.add_section(start = 4319.21, stop = 7889.09, diameter=219.1)

well.Constructions.CaysingParametr.add_section(section = Section(20, 567.12, 473.1), name = "Conductor")
well.Constructions.CaysingParametr.add_section(section = Section(19.5, 2843.03, 339.72), name = "Tech")
well.Constructions.CaysingParametr.add_section(section = Section(19.2, 4319.31, 244.45), name = "Exp")
well.Constructions.CaysingParametr.add_section(section = Section(4219, 7889.09, 168.3), name = "Hvost")


print(f"Время выполнения программ: {time.time() - t_start}")

well.Constructions.show()
