from .utilities import *
from .pysimrel import *
from functools import reduce
from dataclasses import dataclass, field
import numpy as np

@dataclass(init=False)
class SimrelPlot:
    pass

if __name__ == "__main__":
    sobj = Simrel()
    sobj.properties


