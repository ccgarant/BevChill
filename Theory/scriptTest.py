#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:10:36 2019

@author: christophegarant
"""

import math as m
import numpy as np

from peroni_bottle import peroni_bottle
from container import Container
from beer import Beverage


bottle = Container(peroni_bottle)
beer = Beverage(peroni_bottle)

Pr = .7132
top = (.75*Pr)**(1/2)
bottom = (.609+1.221*Pr**(1/2)+1.238*Pr)**(1/4)
g = top/bottom

print(top,bottom,g)
