#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:10:36 2019

@author: christophegarant
"""
from peroni_bottle import peroni_bottle
from container import Container


c = Container(peroni_bottle)

print(c.container_type)
print(c.r_inner,c.r_outter,c.volume)
print(c.A_inner,c.A_outter,c.thickness)
