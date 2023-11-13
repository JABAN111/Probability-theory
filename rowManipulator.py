
'''
Класс для обработки и взаимодействия с выборкой
'''


class rowManipulator:
    def __init__(self, row):
        self.row = row
    def variation_series(self):
        return sorted(self.row)