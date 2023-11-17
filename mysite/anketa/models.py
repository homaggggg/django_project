from django.db import models

# Create your models here.



class Professia(models.Model):
    title = models.TextField(max_length=50, verbose_name = 'Название')

    class Meta:
        ordering = ["-title"]
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессия'

    # def __str__(self):
    #     return self.title
    #
    # def get_fields(self):
    #     return [(field.name, field.value_to_string(self))
    #             for field in Professia._meta.fields]

#class MeTest(models.Model):
#   title = models.TextFile(max_length=50, verbose_name = 'НАЗВАНИЕ')
#    professia = models.ForeignKey(Professia, on_delete=models.PROTECT, verbose_name='Профессия')#


#    class Meta:
#        ordering = ["-title"]
#        verbose_name = 'Мой новый класс'
#        verbose_name_plural = 'Мой новый класс'

#    def __str__(self):
#        return [(field.name, field.value_to_string(self))
#                for field in MeTest._meta.fields]

class Skill(models.Model):
    title = models.TextField(max_length=50, verbose_name = 'Название')

    class Meta:
        ordering = ["-title"]
        verbose_name = 'Навык'
        verbose_name_plural = 'Навык'

    # def __str__(self):
    #     return [(field.name, field.value_to_string(self))
    #             for field in Skill._meta.fields]



class Question(models.Model):
    title = models.TextField(max_length=250, verbose_name = 'Текст вопроса')
    points = models.TextField(max_length=50, verbose_name = 'Бал')
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name='Навык')

    class Meta:
        ordering = ["-title"]
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопрос'

    # def __str__(self):
    #     return [(field.name, field.value_to_string(self))
    #             for field in Question._meta.fields]


class Answer(models.Model):
    title = models.TextField(max_length=50, verbose_name = 'Название')

    class Meta:
        ordering = ["-title"]
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответ'

    # def __str__(self):
    #     return [(field.name, field.value_to_string(self))
    #             for field in Answer._meta.fields]

class ModelProf(models.Model):
    title = models.ForeignKey(Professia, on_delete=models.PROTECT, verbose_name='Название')
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name='Навык')
    count_points = models.TextField(max_length=50, verbose_name = 'Кол-во балов')

    class Meta:
        ordering = ["-title"]
        verbose_name = 'Модельная профессия'
        verbose_name_plural = 'Модельная профессия'

    # def __str__(self):
    #     return [(field.name, field.value_to_string(self))
    #             for field in ModelProf._meta.fields]

class Answers(models.Model):
    user = models.TextField(max_length=50, verbose_name = 'Пользователь')
    skill = models.TextField(max_length=50, verbose_name = 'Навык')
    points = models.TextField(max_length=50, verbose_name = 'Бал')
    date = models.TextField(max_length=50, verbose_name = 'Дата прохождения')

    class Meta:
        ordering = ["-user"]
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'

    # def __str__(self):
    #     return [(field.name, field.value_to_string(self))
    #             for field in Answers._meta.fields]

class ClearSert(models.Model):
    title = models.TextField(max_length=50, verbose_name = 'Название')
    full = models.TextField(max_length=50, verbose_name = 'Полный')
    one = models.TextField(max_length=50, verbose_name = 'Одинарный')

    class Meta:
        ordering = ["-title"]
        verbose_name = 'Пустой сертификат'
        verbose_name_plural = 'Пустой сертификат'

    # def __str__(self):
    #     return [(field.name, field.value_to_string(self))
    #             for field in ClearSert._meta.fields]

class Sert(models.Model):
    sert = models.TextField(max_length=50, verbose_name = 'Сертификат')
    user = models.TextField(max_length=50, verbose_name = "Пользователь")
    key_skill = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name='Ключевой навык',related_name="skillkeyskill")
    all_skills = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name='Все навыки',related_name="skillallskill")

    class Meta:
        ordering = ["-user"]
        verbose_name = 'Cертификат'
        verbose_name_plural = 'Cертификат'

    # def __str__(self):
    #     return [(field.name, field.value_to_string(self))
    #             for field in ModelProf._meta.fields]


# from django.contrib.auth.models import User
# from django.db import models

# # Create your models here.

# class Proffessia(models.Model):
#     title = models.TextField(max_length=50, verbose_name="Профессия")

#     class Meta:
#         ordering = ["-title"]
#         verbose_name = "Профессия"
#         verbose_name_plural = "Профессии"

#     def __str__(self):
#         return self.title

#     def get_fields(self):
#         return [(field.name, field.value_to_string(self)) for field in Proffessia._meta.fields]


# class Naviki(models.Model):
#     title = models.TextField(max_length=50, verbose_name="Навыки")

#     class Meta:
#         ordering = ["-title"]
#         verbose_name = "Навыки"
#         verbose_name_plural = "Навыки"

#     def __str__(self):
#         return self.title

#     def get_fields(self):
#         return [(field.name, field.value_to_string(self)) for field in Naviki._meta.fields]

