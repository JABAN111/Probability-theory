from math import log
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from rowManipulator import rowManipulator
#выборка восьмого варианта
rowOfEighthVariant =[1.07, 1.59,
                     -1.49, -0.10,
                    0.11,1.18,
                     0.35,-0.73,
                     1.07,0.31,
                     -0.26,-1.20,
                     -0.35,0.73,
                     1.01,-0.12,
                     0.28,-1.32,
                     -1.10,-0.26]
rowController = rowManipulator(rowOfEighthVariant)
print(rowController.manipulate_row())
