"""
Класс для обработки и взаимодействия с выборкой
"""

import matplotlib.pyplot as plt
from prettytable import PrettyTable
from math import log
import numpy as np


class rowManipulator:
    def __init__(self, row):
        self.row = row
        self.grouped_data = None

    def variation_series(self):
        """
        Возвращает вариационный ряд
        """

        return sorted(self.row)

    def extremes(self):
        """
       Возвращает экстремальные значения
       """
        min_value = str(self.variation_series()[0])
        max_value = str(self.variation_series()[-1])
        return "Минимальное значение: " + min_value + ", Максимальное значение: " + max_value

    def scope(self):
        """
        :return размах выборки
        """
        min_value = self.variation_series()[0]
        max_value = self.variation_series()[-1]
        return max_value - min_value

    def Statistical_series(self):
        """
        Возвращает статистический ряд
        """
        count_set = {}
        sorted_row = self.variation_series()

        for x in sorted_row:
            # пометка для себя: проверяем последний ключ, тк если элемент повторяется, то он будет подряд и не нужно
            # весь массив
            if count_set and x == list(count_set.keys())[-1]:
                count_set[x] += 1
            else:
                count_set[x] = 1
        return count_set

    def relative_frequency(self):
        """
        Вычисляет относительную частоту для статического ряда
        :return: возвращает массив со значениями p(i) для статического ряда
        """
        n = len(self.variation_series())
        count_set = self.Statistical_series()
        p = [float(format(i / n, '.2f')) for i in list(count_set.values())]
        return p

    def printer_Statistical_series(self):
        """
        Выводит в стандартный поток вывода красивую табличку
        """
        count_set = self.Statistical_series()
        table = PrettyTable()
        table.field_names = ["x(i)", *count_set.keys()]
        table.add_row(["n(i)", *count_set.values()])
        table.add_row(["p(i)", *self.relative_frequency()])
        return table

    def avg_row(self):
        """
        :return среднее значение выборки
        """
        return sum(self.row) / len(self.row)

    def assessment_mathematical_expectation(self):
        """
        :return оценку мат ожидания выборки
        """
        n = len(self.row)
        count_set = self.Statistical_series()
        total = 0
        for x in count_set:
            total += x * count_set[x]
            total = round(total, 2)
        return total / n

    def dispersion(self):
        """
        :return дисперсию выборки
        """
        dispersion = 0
        for x in self.row:
            dispersion += (x - self.avg_row()) * (x - self.avg_row())
        return dispersion

    '''
    :return среднеквадратичное отклонение
    '''

    def standard_deviation(self):
        return self.dispersion() ** 0.5

    def empirical_distribution(self):
        """
       :return эмпирическую функцию распределения и график к ней
       """
        count_set = self.Statistical_series()
        print(len(self.variation_series()))
        plt.subplot(5, 1, 1)
        plt.title("График эмпирической функции распределения")
        n = len(count_set)
        keys = list(count_set.keys())
        y = 0
        frequencyArray = self.relative_frequency()
        print(f'\t\t/ {y}, при x <= {keys[0]}')
        result = ""
        for i in range(n - 1):
            if i < n:
                y += frequencyArray[i]
            #if+else для красивого вывода F(x)
            if i == n / 2:
                left = "F*(x) = "
            else:
                left = "\t\t"
            result += f'{left}| {round(y,2)}, при {keys[i]} < x <= {keys[i + 1]}\n'
            plt.plot([keys[i], keys[i + 1]], [y, y], c='black')
        y += frequencyArray[-1]
        result += f'\t\t\\ {round(y,2)}, при {keys[-1]} < x'
        return result

    '''
    Интервальное статистическое распределение
    '''

    def interval_statistical_distribution(self):
        sorted_row = self.variation_series()
        n = len(self.row)
        m = 1 + round(log(n, 2))
        h = round((sorted_row[-1] - sorted_row[0]) / m, 2)
        curr_x = sorted_row[0] - h / 2
        next_x = curr_x + h
        grouped_data = {curr_x: 0}
        for x in sorted_row:
            if x < next_x:
                grouped_data[curr_x] += 1 / n
            else:
                grouped_data[next_x] = 1 / n
                curr_x = next_x
                next_x = round(next_x + h, 2)
        table = PrettyTable()
        field_names = []
        self.grouped_data = grouped_data
        for x in grouped_data.keys():
            field_names.append(f'[{round(x, 2)}; {round(x + h, 2)})')

        values_list = []
        for x in grouped_data.values():
            values_list.append(round(x, 2))

        table.field_names = field_names
        table.add_row(values_list)

        return table

    '''
    Полигон частот
    '''

    def frequency_polygon(self):
        plt.subplot(5, 1, 3)
        plt.title("Полигон приведенных частот")
        if (self.grouped_data != None):
            plt.plot(list(self.grouped_data.keys()), list(self.grouped_data.values()), c='red')
        else:
            self.interval_statistical_distribution()
            self.frequency_polygon()

    def frequency_histogram(self):
        '''
        Гистограмма частот
        '''
        plt.subplot(5, 1, 5)
        plt.title("Гистограмма частот")

        n = len(self.row)
        sorted_row = self.variation_series()
        m = 1 + round(log(n, 2))
        h = round((sorted_row[-1] - sorted_row[0]) / m, 2)

        x_values = []
        for x in self.grouped_data.keys():
            x_values.append(x + h / 2)

        y_values = list(self.grouped_data.values())
        plt.bar(x_values, y_values, width=h)

        xticks = [round(x + h, 2) for x in self.grouped_data.keys()]
        xticks.insert(0, round(list(self.grouped_data.keys())[0], 2))
        plt.xticks(xticks, xticks)

    '''
    Отображает все графики, сделанные plt
    '''

    def show_images(self):
        plt.show()
