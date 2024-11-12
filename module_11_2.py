"""
Для работы был выбран имеющийся модуль, который взят из собственного проекта
Для удобства просмотра работы кода он так же подкреплён на GitHub.
"""

from Hero import Hero, Talents


def introspection_info(obj):
    print_dict = None
    if print_dict is None:
        print_dict = {'Тип объекта': type(obj),
                      'Атрибуты объекта': dir(obj),
                      'Уникальные атрибуты': [attr for attr in dir(obj) if not callable(getattr(obj, attr))
                                              and not attr.startswith("__")],
                      'Методы объекта': [method for method in dir(obj) if callable(getattr(obj, method))
                                         and not method.startswith("__")],
                      'Модуль': obj.__module__}

        for key, value in print_dict.items():
            print(f'{key}: {value}')


if __name__ == '__main__':
    example_Hero = Hero()
    example_Talent = Talents()

    introspection_info(example_Hero)
    print('\n\n')
    introspection_info(example_Talent)
