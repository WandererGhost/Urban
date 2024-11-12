class Hero:
    """
    Основная команда под управлением игрока
    """

    def __init__(self):
        self.war = ['war', 1]
        self.wiz = ['wiz', 1]
        self.pal = ['pal', 1]
        self.th = ['th', 1]

        self.power = 4

        self.lives = 4
        self.rip = False

        self.potions = 0
        self.history_potions = 0

        self.artefacts = []
        self.crystals = []

        self.talent = None
        self.talent_card = None
        self.talent_cost = 0

        self.mission = None
        self.mission_card = None

        self.glory = 0

    def check_rip(self):
        """
        Проверка на то, погибала ли команда игрока. Если да, то в коце игры будет -9 победных очков
        :return:
        """
        if self.lives == 0 and self.rip is False:
            self.rip = True
            self.lives = 4
            return self.rip, self.lives
        if self.lives == 0 and self.rip is True:
            raise ValueError('Умереть второй раз нельзя!')

    def level_up(self, choice):
        """
        Повышение уровня одного из членов команды под управлением игрока
        :param choice: выбор члена отряда
        :return:
        """
        attribute = getattr(self, choice, None)  # Получаем атрибут по имени

        if attribute is not None and isinstance(attribute, list):
            attribute[1] += 1
            self.power += 1
            self.lives += 1
            return self.power, self.lives, attribute
        else:
            raise ValueError(f"Неверный выбор: {choice}.Доступные классы: 'war', 'wiz', 'pal', 'th'")

    def create_potion(self):
        """
        Создание или нахождение в комнате исцеляющего зелья
        :return: возращение обновлённых значений количества зелий и их истории
        """
        self.potions += 1
        self.history_potions += 1
        return self.potions, self.history_potions

    def use_potion(self):
        """
        Использование зелья для восстановления здоровья
        :return: возвращение обновлённых значений количества зелий и количества жизней
        """
        self.potions -= 0.5
        self.lives += 1
        return self.potions, self.lives

    def check_talent(self):
        if self.talent == 'Алхимик':
            self.talent_cost = -1
            self.glory -= 1
            return self.talent_cost, self.glory
        if self.talent == 'Благородный':
            self.talent_cost = -1
            self.glory -= 1
        if self.talent == 'Варвар':
            pass
        if self.talent == 'Вор':
            pass
        if self.talent == 'Кровожадный':
            self.talent_cost = -2
            self.power += 2
            self.glory -= 2
            return self.talent_cost, self.power, self.glory
        if self.talent == 'Мародёр':
            self.talent_cost = -2
            self.glory -= 2
            return self.talent_cost, self.glory
        if self.talent == 'Мастер':
            self.talent_cost = -3
            self.glory -= 3
            return self.talent_cost, self.glory
        if self.talent == 'Мистик':
            self.talent_cost = 2
            self.glory += 2
            return self.talent_cost, self.glory
        if self.talent == 'Провидец':
            self.talent_cost = 2
            self.glory += 2
            return self.talent_cost, self.glory
        if self.talent == 'Разведчик':
            self.talent_cost = -2
            self.glory -= 2
            return self.talent_cost, self.glory
        if self.talent == 'Следопыт':
            self.talent_cost = -1
            self.glory -= 1
            return self.talent_cost, self.glory
        if self.talent == 'Торговец':
            self.talent_cost = -1
            self.glory -= 1
            return self.talent_cost, self.glory
        if self.talent == 'Убийца':
            pass
        if self.talent == 'Умелец':
            self.talent_cost = -3
            self.glory -= 3
            return self.talent_cost, self.glory
        if self.talent == 'Целитель':
            self.talent_cost = 2
            self.glory += 2
            return self.talent_cost, self.glory
        if self.talent == 'Шаман':
            self.talent_cost = 3
            self.glory += 3
            return self.talent_cost, self.glory

    def check_mission(self):
        pass


class Talents:
    """
    На начало игры карта, дающая плюхи. Карта остаётся до конца игры
    """

    def __init__(self):
        self.tal_cards = [{'Алхимик': 'textures/Card/Talents/Alchemist.png'},
                          {'Благородный': 'textures/Card/Talents/Noble.png'},
                          {'Варвар': 'textures/Card/Talents/Barbarian.png'},
                          {'Вор': 'textures/Card/Talents/Thief.png'},
                          {'Кровожадный': 'textures/Card/Talents/Bloodthirsty.png'},
                          {'Мародёр': 'textures/Card/Talents/Marauder.png'},
                          {'Мастер': 'textures/Card/Talents/Master.png'},
                          {'Мистик': 'textures/Card/Talents/Mystic.png'},
                          {'Провидец': 'textures/Card/Talents/Seer.png'},
                          {'Разведчик': 'textures/Card/Talents/Scout.png'},
                          {'Следопыт': 'textures/Card/Talents/Ranger.png'},
                          {'Торговец': 'textures/Card/Talents/Merchant.png'},
                          {'Убийца': 'textures/Card/Talents/Assassin.png'},
                          {'Умелец': 'textures/Card/Talents/Craftsman.png'},
                          {'Целитель': 'textures/Card/Talents/Healer.png'},
                          {'Шаман': 'textures/Card/Talents/Shaman.png'}]

        self.first_card_t, self.second_card_t = self.to_select_a_talent()

    def to_select_a_talent(self):
        import random
        self.first_card_t = random.choice(self.tal_cards)
        self.second_card_t = random.choice(self.tal_cards)
        if self.first_card_t == self.second_card_t:
            self.second_card_t = random.choice(self.tal_cards)
        return self.first_card_t, self.second_card_t


class Missions:
    """
    Личная цель игры на протяжении всей игры.
    Также отвечает за распределение цветов кубиков в команде игрока.
    """

    def __init__(self):
        """
        игра получает выбранный номер карты
        mis_cards - это список из словарей. Каждая внесённая в список карточка даёт распределение
        для команды по цветам кубика.
        """
        self.mis_cards = [{'Артефакты': ['b', 'b', 'w', 'w', 'textures/Card/Missions/artefacts_2_4_7.png']},
                          {'Столбцы': ['b', 'w', 'w', 'b', 'textures/Card/Missions/columns_4_rooms_4_5_6.png']},
                          {'По углам': ['b', 'w', 'b', 'w', 'textures/Card/Missions/corner_rooms_1_2_3.png']},
                          {'Самоцветы': ['b', 'w', 'w', 'b', 'textures/Card/Missions/crystals_2_5_7.png']},
                          {'Ряды': ['w', 'b', 'b', 'w', 'textures/Card/Missions/full_rows_1_2_3.png']},
                          {'Слава': ['w', 'b', 'b', 'w', 'textures/Card/Missions/glory_for_boss_10_15_20.png']},
                          {'Сбор зелий': ['w', 'b', 'w', 'b', 'textures/Card/Missions/history_potion_6_9_12.png']},
                          {'Профессионал': ['w', 'w', 'b', 'b', 'textures/Card/Missions/lev5_2_3_4.png']},
                          {'Периметр': ['b', 'b', 'w', 'w', 'textures/Card/Missions/outer_rooms_10_13_16.png']},
                          {'Мощь': ['w', 'b', 'w', 'b', 'textures/Card/Missions/pow_12_16_20.png']},
                          {'Любопытство': ['b', 'w', 'b', 'w', 'textures/Card/Missions/roms_20_25_30.png']},
                          {'Преграды': ['w', 'w', 'b', 'b',
                                        'textures/Card/Missions/traps_and_water_obstacles_or_walls_4_7_10.png']},
                          {'Приспешники 3ур.': ['b', 'w', 'b', 'w', 'textures/Card/Missions/win_mobs_lev3_2_3_4.png']},
                          {'Приспешники 4ур.': ['b', 'w', 'w', 'b', 'textures/Card/Missions/win_mobs_lev4_2_3_4.png']},
                          {'Приспешники 5ур.': ['w', 'b', 'b', 'w', 'textures/Card/Missions/win_mobs_lev5_2_3_4.png']},
                          {'Зачистка': ['w', 'w', 'b', 'b', 'textures/Card/Missions/win_mobs_4_7_10.png']}]

        self.first_card_m, self.second_card_m = self.to_select_a_mission()

    def to_select_a_mission(self):
        import random
        self.first_card_m = random.choice(self.mis_cards)
        self.second_card_m = random.choice(self.mis_cards)
        if self.first_card_m == self.second_card_m:
            self.second_card_m = random.choice(self.mis_cards)
        return self.first_card_m, self.second_card_m
