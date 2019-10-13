from .utilities import *
from .pysimrel import *
from functools import reduce
from dataclasses import dataclass, field
import numpy as np
import matplotlib.pyplot as plt

@dataclass(init=False)
class SimrelPlot:
    pass


sobj = Simrel()
sobj.parse_parameters()
sobj.compute_properties()

sobj.covariances.cov_xx



