# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:18:19 2021

@author: alquds
"""

import utils
from logic import *



clauses = [expr("Man(John)"), expr("Women(Jia)"), expr("Healthy(John)"), expr("Wealthy(John)"), expr("Wealthy(Jia)")
    ,expr("(Wealthy(x) & Healthy(x)) ==> Traveler(x)")]

KB = FolKB(clauses)
wealthy = fol_bc_ask(KB, expr("Wealthy(x)"))
healthy = fol_bc_ask(KB, expr("Healthy(x)"))
traveler = fol_bc_ask(KB, expr("Traveler(x)"))
print('Who are healthy ?')
print(list(healthy), '\n')
print('Who are wealthy ?')
print(list(wealthy), '\n')
print('Who can travel ?')
print(list(traveler))