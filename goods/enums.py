from enum import Enum


class ProductTypeEnum(Enum):
    BOOK = 'Книга'
    MOVIE = 'Фильм'
    MUSIC = 'Музыка'
    PICTURE = 'Картина'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]
