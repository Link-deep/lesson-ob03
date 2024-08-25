# Создайте класс Author и класс Book.
# Класс Book должен использовать композицию для включения автора в качестве объекта.
#
# Решение.
# Создаем класс Author и в инициализации (init) прописываем базовые характеристики имя
# и национальность (nationality):
#
# class Author():#
# def init(self, name, nationality):#
# self.name = name#
# self.nationality = nationality
#
# Создаем класс Book без наследования и прописываем как функцию инициализации книг
# с характеристиками название (title) и автор (author),
# так и характеристику title для передачи дальше:
#
# class Book():#
# def init(self, title, author):
# self.title = title
#
# С помощью агрегации передаем автора.

class Auhtor():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author  # ПЕРВЫЙ ВАРИАНТ - АГРЕГАЦИЯ
        # author = Auhtor()  ВТОРОЙ ВАРИАНТ - КОМПОЗИЦИЯ
    def info_book(self):
        print(self.title, self.author.name, self.author.nationality)


# 1) ПЕРВЫЙ ВАРИАНТ создаем объекты АГРЕГАЦИЯ
author = Auhtor("Лев Толстой", "Русский")
book = Book("Война и мир", author)
print(author.name)
book.info_book()


