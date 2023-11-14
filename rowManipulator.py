'''
Класс для обработки и взаимодействия с выборкой
'''
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from math import log


class rowManipulator:
    def __init__(self, row):
        self.row = row
        self.grouped_data = None


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
        return "Минимальное значение: " + min_value + ", Максимальное значение: " + max_value

    '''
    :return размах выборки
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

    def standard_deviation(self):
        return self.dispersion() ** 0.5

    '''
    :return эмпирическую функцию распределения и график к ней
    '''
    def empirical_distribution(self):
        count_set = self.Statistical_series()
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
        plt.plot(list(self.grouped_data.keys()), list(self.grouped_data.values()), c='red')

    '''
    Отображает все графики, сделанные plt
    '''
    def show_images(self):
        plt.show()