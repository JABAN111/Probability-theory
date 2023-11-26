from rowManipulator import rowManipulator

# восьмой вариант
rowOfEighthVariant = [1.07, 1.59,
                      -1.49, -0.10,
                      0.11, 1.18,
                      0.35, -0.73,
                      1.07, 0.31,
                      -0.26, -1.20,
                      -0.35, 0.73,
                      1.01, -0.12,
                      0.28, -1.32,
                      -1.10, -0.26]

rowController = rowManipulator(rowOfEighthVariant)
print("Вариационный ряд: ")
print(rowController.variation_series())
print("Статистический ряд")
print(rowController.printer_Statistical_series())
print("Экстремальные значения: " + rowController.extremes())
print("Размах: " + str(rowController.scope()))
print("Оценка математического ожидания: " + str(rowController.assessment_mathematical_expectation()))
print("Среднеквадратичное отклонение: " + str(rowController.standard_deviation()))
print("Эмпирическая функция распределения:")
print(rowController.empirical_distribution())
print("Интервальное статистическое распределение:")
print(rowController.interval_statistical_distribution())

rowController.frequency_polygon()
rowController.frequency_histogram()
rowController.show_images()
