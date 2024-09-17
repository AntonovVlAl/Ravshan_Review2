import time


class Car:
    brand = input('Марка машины: ')
    price = int(input('Цена машины: '))

    @classmethod
    def price_cash(cls):
        return print(f'Цена {cls.brand}а за наличные {cls.price}')

    @classmethod
    def price_of_credit(cls):
        return print(f'Цена {cls.brand}а в кредит {cls.price - (cls.price // 100 * 10)}')

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Время выполнения функции {func.__name__}: {elapsed_time:.6f} секунд')
        return result
    return wrapper


@time_decorator
def car_sale(type_sale):
    if type_sale.lower() == 'наличные':
        return Car.price_cash()
    elif type_sale.lower() == 'кредит':
        return Car.price_of_credit()


time_decorator(car_sale(input('Введите тип покупки: ')))