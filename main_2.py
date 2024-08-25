# Пример агрегации

class Teacher():
    def teach(self):
        print("Учитель преподаёт")


class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()
        print("Начинаем урок")

my_teacher = Teacher()
my_school = School(my_teacher)

# 1) Создаем класс Teacher (учителя)
# 2) Создаем класс School (школы)
# 3) Создаем объект Учителя: my_teacher = Teacher()
# 4) Создаем объект Школы и передаем туда учителя: my_school = School(my_teacher)
# 5) В классе школы принимает этого учителя. и создаем для него хар-ку: self.teacher = new_teacher
# 6) Теперь можно вызвать метод учителя: self.teacher.teach()



