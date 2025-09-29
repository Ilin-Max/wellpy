from Well import Well
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

well.Constructions.CaysingParametr.add_section(start = 20, stop = 567.12, diameter = 473.1, name = "Conductor")
well.Constructions.CaysingParametr.add_section(start = 19.5, stop = 2843.03, diameter = 339.72, name = "Tech")
well.Constructions.CaysingParametr.add_section(start = 19.2, stop = 4319.31, diameter = 244.45, name = "Exp")
well.Constructions.CaysingParametr.add_section(start = 4219, stop = 7889.09, diameter = 168.3, name = "Hvost")

print(f"Время выполнения программ: {time.time() - t_start}")

well.Constructions.show()
