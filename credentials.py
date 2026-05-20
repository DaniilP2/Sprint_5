import random
import string

class Credentials():
    # Данные для предрегистрации/проверки входа
    my_name = 'Daniil'  # Имя
    my_email = 'pronichkin_46@gmail.ru'  # Почта
    my_password = '123qwe'  # Корректный пароль
    
    # Проверить ошибку для некорректного пароля. Минимальный пароль — шесть символов.
    negative_password = '123qw'  # Некорректный пароль - 5 символов

    @staticmethod
    def email(): # Генерация почты для регистрации в формате: имя_фамилия_номер когорты_любые 3 цифры@домен
        return f'pronichkin_46_{random.randint(100, 999)}@gmail.ru'
    
    @staticmethod
    def password(): # Генерация пароля, минимальный пароль — шесть символов
        return ''.join(random.choices(string.digits, k=6))