# Задача "Range - это просто":
class StepValueError(ValueError):
    pass
class Iterator:
    # принимающий значения старта и конца итерации, а также шага
    def __init__(self, start, stop, step = 1):
        self.start = start   #целое число, с которого начинается итерация.
        self.stop = stop    # целое число, на котором заканчивается итерация.
        self.step = step    # шаг, с которым совершается итерация.
        #pointer указывает на текущее число в итерации (изначально start)
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        # сбрасывающий значение pointer на start и возвращающий сам объект итератора
    def __iter__(self):
        self.pointer = self.start
        return self
    #  увеличивающий атрибут pointer на step
    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        cur_att = self.pointer
        self.pointer += self.step
        return cur_att


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
    print()
for i in iter3:
    print(i, end=' ')
    print()
for i in iter4:
    print(i, end=' ')
    print()
for i in iter5:
    print(i, end=' ')
    print()
