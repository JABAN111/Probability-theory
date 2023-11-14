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
#другой вариант для сравнения
data = [-0.53, -0.87, -0.93, -0.41, 0.48, 0.81, -1.55, -1.42, -1.34, -0.61,
        -0.04, -0.33, -0.84, -1.33, 0.57, 0.62, 0.76, -0.48, 0.30, -0.35]

rowController = rowManipulator(data)
print("Вариационный ряд: ")
print(rowController.variation_series())
print("Экстремальные значения: " + rowController.extremes())
print("Размах: " + str(rowController.scope()))
print("Оценка математического ожидания: " + str(rowController.assessment_mathematical_expectation()))
print("Среднеквадратичное отклонение: " + str(rowController.standard_deviation()))
print("Эмпирическая функция распределения:")
print(rowController.empirical_distribution())
print("Интервальное статистическое распределение:")
print(rowController.interval_statistical_distribution())


rowController.frequency_polygon()
rowController.show_images()