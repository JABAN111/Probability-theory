'''
Класс для обработки и взаимодействия с выборкой
'''


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
