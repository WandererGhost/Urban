class User:
    """
    Класс, отвечающий за данные пользователя. Аргументы класса: имя, пароль и возраст
    Есть проверка, вводит ли пользователь свой возраст
    """

    def __init__(self, nickname, password, age=None):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        if age is None:
            print('Вы не указали свой возраст. Некоторый контент может быть недоступен.\n'
                  'Хотите добавить эту информацию о себе сейчас?\n1 - Да\n2 - Нет')
            check = int(input())
            if check == 1:
                age = int(input('Сколько Вам лет?\n'))
                self.age = age
            else:
                age = None
                self.age = age

    def __str__(self):
        return f'Пользователь: {self.nickname}\nВозраст: {self.age}'


class Video:
    """
    Класс создания и получения информации о видео.
    Атрибуты класса: название видео, его продолжительность и ограничение по возрасту
    """

    def __init__(self, title, duration, adult_mode=False, time_now=0):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __str__(self):
        return f'Название видео: {self.title}\n' \
               f'Продолжительсность воспроизведения: {self.duration}\n' \
               f'Возрастное ограничение: {self.adult_mode}\n'


class UrTube:
    """
    Класс, связывающий пользователя и имеющиеся на сервисе видео.
    Атрибуты класса: база пользователей (users), база с видео (videos) и текущий пользователь (current_user).
    Текущий пользователь по умолчанию None.

    Данный класс позволяет зарегистрировать пользователя или залогинить его. Как и в классе User,
    данный класс запрашивает возраст пользователя при регистрации.
    """
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname not in self.users:
            print('Пользователя с таким именем не существует')
            return None
        stored_password = self.users[nickname]
        if stored_password[0] != hash(password):
            print('Пароль введён неверно')
            return None
        self.current_user = nickname
        return self.current_user

    def register(self, nickname, password, age=None):
        if nickname not in self.users:
            us = User(nickname, password, age)
            self.users[nickname] = [us.password, us.age]
            self.current_user = nickname
            # print(f'Пользователь {nickname} зарегистрирован.')
            return self.current_user, us
        else:
            print(f'Пользователь с таким именем уже существует.')

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self, *videos):
        for video in videos:
            if video.title not in self.videos:
                self.videos[video.title] = [video.duration, video.adult_mode, video.time_now]
        return self.videos

    def get_videos(self, search_word):
        search_word = search_word.lower()
        search = []
        for key in self.videos:
            if search_word in key.lower():
                search.append(key)
        return f'{search}'

    def watch_video(self, title):
        from time import sleep
        if title not in self.videos:
            print('Данного видео не существует') # Данная запись показывает, что программа работает
            # но не проходит дальше этого пункта.
            return
        else:
            inform_video = self.videos[title]
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        else:
            inform_user = self.users[self.current_user]

        if inform_video[1] == True:
            if inform_user[1] is None:
                print('Не хватает информации о пользователе для доступа к данному видео')
                return
            else:
                if inform_user[1] < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return
        for i in range(1, inform_video[0] + 1):
            sleep(1)
            print(i, end=' ')
        print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Проверка добавленных видео
# prit(ur.videos)

# Добавление видео
ur.add(v1, v2)

# Проверка добавленных видео
# prit(ur.videos)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

# Однако по задумке пользователь имеет доступ к видео без ограничения по возрасту:
# ur.watch_video('Лучший язык программирования 2024 года')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Строка от себя на проверку работы запроса возраста от пользователя:
# ur.register('Wanderer', 'iScX4vI')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Проверка выхода из аккаунта
# ur.log_out()
# Проверка входа в уже существующий аккаунт
# ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
