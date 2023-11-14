'''
Класс для обработки и взаимодействия с выборкой
'''
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from math import log


class rowManipulator:
    def __init__(self, row):
        self.row = row

    '''
    Возвращает вариационный ряд
    '''

    def variation_series(self):
        return sorted(self.row)

    '''
    Возвращает экстремальные значения
    '''

    def extremes(self):
        min_value = str(self.variation_series()[0])
        max_value = str(self.variation_series()[-1])
        return "Минимальное значение: " + min_value + ", максимальное значение: " + max_value

    '''
    Возвращает размах выборки
    '''

    def scope(self):
        min_value = self.variation_series()[0]
        max_value = self.variation_series()[-1]
        return max_value - min_value

    '''
    Возвращает статистический ряд
    Нужен для нахождения мат ожидания и дисперсии
    :return словарь, где ключ 
    '''

    def Statistical_series(self):
        # создаем пустой словарь для хранения пары ключ-значение
        count_set = {}
        sortedRow = self.variation_series()

        for x in sortedRow:
            # Если словарь не пустой и проверяет совпадение с последним добавленным ключом
            if count_set and x == list(count_set.keys())[-1]:
                count_set[x] += 1
            else:
                count_set[x] = 1
        return count_set

    '''
    Возвращает красивой табличкой данные 
    p.s. для вывода таблички print(printer_Statistical_series())
    '''

    def printer_Statistical_series(self):
        count_set = self.Statistical_series()
        table = PrettyTable()
        table.field_names = ["x(i)", *count_set.keys()]
        table.add_row(["n(i)", *count_set.values()])
        return table

    '''
    :return среднее значение выборки
    '''

    def avgRow(self):
        return sum(self.row) / len(self.row)

    '''
    :return оценку мат ожидания выборки
    '''

    def assessment_mathematical_expectation(self):
        n = len(self.row)
        count_set = self.Statistical_series()
        total = 0
        for x in count_set:
            total += x*count_set[x]
        return total/n

    '''
    :return дисперсию выборки
    '''

    def dispersion(self):
        dispersion = 0
        for x in self.row:
            dispersion += (x - self.avgRow()) * (x - self.avgRow())
        return dispersion

    '''
    :return среднеквадратичное отклонение
    '''

    def avgSqrt(self):
        return self.dispersion() ** 0.5

    '''
    :return эмпирическую функцию распределения и график к ней
    '''

    def empiricFunRasp(self):
        count_set = self.Statistical_series()
        print("Эмпирическая функция:")
        plt.subplot(5, 1, 1)
        plt.title("График эмпирической функции распределения")
        n = len(count_set)
        keys = list(count_set.keys())
        y = 0
        print(f'\t\t/ {round(y, 2)}, при x <= {keys[0]}')
        result = ""
        for i in range(n - 1):
            if i < n:
                y += count_set[keys[i]] / n
            else:
                y += 0

            if i == n / 2:
                left = "F*(x) = "
            else:
                left = "\t\t"

            result += f'{left}| {round(y, 2)}, при {keys[i]} < x <= {keys[i + 1]}\n'
            plt.plot([keys[i], keys[i + 1]], [y, y], c='black')
        result += f'\t\t\\ {round(y, 2)}, при {keys[-1]} < x'
        plt.show()
        return result





