import random
import json
import csv
from datetime import datetime

player_name = ""
teacher_name = ""

data_file = "data.json"
csv_file = "data.csv"
saved_data = []

def introduction():
    print("Добро пожаловать в игру 'Звездные войны'!")
    print("Ваша задача спасти галактику, на вас вся надежда.")
    print("Да прибудет с вами сила!\n")
    print("Введите (Сохранить игру) что бы сохранить игру ")
    show_menu()

def load_data():
    global saved_data
    try:
        with open(data_file, 'r') as json_file:
            saved_data = json.load(json_file)
    except FileNotFoundError:
        saved_data = []

def save_data():
    global saved_data
    with open(data_file, 'w') as json_file:
        json.dump(saved_data, json_file)

def show_menu():
    load_data()
    print("Меню:")
    print("1. Начать игру")
    print("2. Просмотр сохраненных данных")
    print("3. Удалить сохранение")
    print("4. Выход")
    handle_menu_choice()

def handle_menu_choice():
    global player_name
    while True:
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            start_game()
        elif choice == "2":
            view_saved_data()
        elif choice == "3":
            delete_save()
        elif choice == "4":
            print("Спасибо за игру. До свидания!")
            save_data()
            exit()
        elif choice == "Сохранить игру":
            print("Выша игра сохранена, возвращайтесь и доигровайте скорей")
        else:
            print("Ошибка! Пожалуйста, выберите действительный пункт меню.\n")

def start_game():
    global teacher_name
    global player_name
    player_name = input("Введите свое имя, молодой падаван: ")
    print(f"\nПривет, {player_name}! Ты - последняя надежда всей галактики.")
    print("Тебе предстоит обучиться навыкам джедая и сразиться с Лордом ситхов - Дартом Вейдером.")
    print("Да прибудет с тобой сила!\n")
    ychitela = ["Оби-Ван Кеноби", "Магистр Йода", "Квайгон-Джин", "Мейс Винду"]
    print(f"Перед тобой 4 лучших джедая: {ychitela}")
    ispitanie = input("Кого из них ты выберешь, но выбор делай, опираясь на свое чутье: ")
    if ispitanie in ychitela:
        teacher_name = ispitanie
    else:
        print("Неправильный выбор! Попробуй еще раз.\n")
        start_game()
    print(f"Твой учитель: {teacher_name}\n")
def save_game_result(result):
    global saved_data
    saved_data.append({"Результат": result, "Дата": str(datetime.now())})
    save_data()
    save_to_csv()

def save_to_csv(csv_file=None):
    with open(csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Результат", "Дата"])
        for data in saved_data:
            csv_writer.writerow([data["Результат"], data["Дата"]])

def view_saved_data():
    load_data()
    print("Сохраненные данные:")
    for i, data in enumerate(saved_data, 1):
        print(f"{i}. Результат: {data['Результат']}, Дата: {data['Дата']}")

def delete_save():
    global saved_data
    view_saved_data()
    choice = input("Введите номер сохранения для удаления: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(saved_data):
            deleted_data = saved_data.pop(choice - 1)
            print(f"Удалено сохранение: Результат: {deleted_data['Результат']}, Дата: {deleted_data['Дата']}")
            save_data()
            save_to_csv()
        else:
            print("Ошибка! Введите действительный номер сохранения.")
    except ValueError:
        print("Ошибка! Введите номер сохранения.")
    except IndexError:
        print("Ошибка! Введите действительный номер сохранения.")

def exit():
    save_data()
    save_to_csv()
    super().exit()

def kristalnaypeshera(player_name, teacher_name):
    print(f"ТЫ НАХОДИШЬСЯ В КРИСТАЛЬНОЙ ЛЕДЯНОЙ ПЕЩЕРЕ.")
    print(f"Твоя задача - найти именно твой кристалл и выбраться из пещеры")
    while True:
        choicevpeshere = input(
            f"{player_name}: Передо мной 4 дороги, куда мне отправиться: Вниз, Вправо, Влево, Прямо \n")
        if choicevpeshere == "Прямо":
            print(f"{player_name}: Ура, сила привела меня к моему кристаллу\n"
                  f"{player_name}Надо скорее рассказать это учителю")
            print(
                f"{teacher_name}: Я знал, что силы в тебе больше, чем страха, и ты сможешь добыть свой кайбер-кристалл")
            sborkamecha(player_name, teacher_name)
        elif choicevpeshere == "Влево":
            print(
                f"{player_name}: Я нашел выход из пещеры, но если я вернусь без кристалла, {teacher_name} будет разгневан.")
        elif choicevpeshere == "Вправо":
            print(f"{player_name}: Тут кристалла нет, надо вспомнить, что говорил {teacher_name} и следовать за силой")
        elif choicevpeshere == "Вниз":
            print(f"{player_name}: Ура, я нашел кристалл\n"
                  "Кристалл расскалывается в руке\n"
                  f"{player_name}: Но почему он сломался, я же его нашел, придется искать новый\n"
                  "Вы вернулись в начало пещеры, куда зовет сила на этот раз")
            print(
                f"{teacher_name}: Я знал, что силы в тебе больше, чем страха, и ты сможешь добыть свой кайбер-кристалл")

def sborkamecha(player_name, teacher_name):
    print(f"{teacher_name}: {player_name} теперь из кайбер-кристалла тебе необходимо сделать световой меч\n"
          f"{player_name}: Учитель как я должен его сделать только из кибер кристалла?"
          f"{teacher_name}: В этом тебе поможет выскотехнологичный робот Хьюянг")
    print(
        f"Хьюянг: Здравствуй, юный падаван! Я - робот Хуян. За все время на своем корабле я создал более 10,000 световых мечей для падаванов. Давай соберем для тебя блестящий световой меч.")
    tipsvetovogomecha = input(f"Хьюянг: Начнем с простого. Какого типа меч ты хочешь (Обычный / Двусторонний / 2 меча): ")
    cvetlezviya = input(f"Хьюянг: Отличный выбор! Теперь выбери цвет лезвия (Синий / Зелёный / Фиолетовый): ")
    materialrukoitki = input(f"Хьюянг: Хорошо, теперь выбери материал для рукоятки (Металл / Дерево / Пластик): ")
    print(f"Хьюянг: Великолепно, {player_name}! Твой световой меч готов.")
    print(f"Тип меча: {tipsvetovogomecha}")
    print(f"Цвет лезвия: {cvetlezviya}")
    print(f"Материал рукоятки: {materialrukoitki}")
    print(f"Да прибудет с вами сила!")
    piatletspustia(player_name, teacher_name)
    return player_name, teacher_name


def piatletspustia(player_name, teacher_name):
    print(f"Пять лет спустя\n"
          f"{teacher_name}: {player_name}, ты стал опытным дждаем и достойным учеником\n"
          f"{teacher_name}: ты проделал огромный путь и обрел мудрость, теперь настало время новых испытаний\n"
          f"{player_name}: {teacher_name} я готов к новым испытаниям\n"
          f"{teacher_name}: Ты по-прежнему несешь в себе силу и смелость. Но помни, что сила - это не всё. Служи своей миссии и оставайся верным джедайским учениям\n"
          f"{teacher_name}: Да прибудет с тобой сила, {player_name}.\n")
    smertiechitelya(player_name, teacher_name)
    return player_name, teacher_name


def smertiechitelya(player_name, teacher_name):
    print(f"Сражение с Дартом Вейдером началось!\n")
    print(f"{teacher_name} и {player_name} готовы к битве.\n")
    teachersmrt = random.uniform(0, 1)
    if teachersmrt >= 0.5:
        print(f"{teacher_name} сражается с Дартом Вейдером, проявляя выдающиеся навыки.\n"
              f"{teacher_name}: {player_name}, уходи, я позабочусь о том, чтобы ты выжил.\n"
              f"Учитель сражается с героизмом, но в конечном итоге погибает, защищая {player_name}.\n"
              f"{player_name}: {teacher_name} НННННННЕЕЕЕЕЕЕЕТТТТТТ\n"
              f"Дарт Вейдер: Ты следующий, {player_name}.")
    else:
        print(f"{teacher_name} сражается с Дартом Вейдером, но силы ситха слишком велики.\n"
              f"{teacher_name}: {player_name}, уходи, пока не поздно!\n"
              f"Учитель героически сражается, чтобы дать {player_name} шанс на спасение.\n"
              f"{player_name}: {teacher_name} НННННННЕЕЕЕЕЕЕЕТТТТТТ\n"
              f"Дарт Вейдер: Ты следующий, {player_name}.")

    print(f"После тяжелой потери {player_name} возвращаешься в храм джедаев.\n")
    print(f"Пло Кун: Мы слышим твою печаль, {player_name}. Твой учитель был великим джедаем.\n")
    print(f"{player_name}: Да, Пло Кун, и теперь на мне лежит ответственность продолжить его дело.\n"
          f"И стану тренироваться усерднее\n"
    "Выбери тренировку или введи 'завершить тренировки':\n"
    "1. Обучение бою с мечом.\n"
    "2. Медитация и контроль над силой.\n"
    "3. Стратегическое планирование.\n")
    trained_skills = {"1": "технику боя с мечом", "2": "медитацию и контроль над силой", "3": "стратегическок планирование"}

    training_tasks = {
        "1": ["Задание 1: Практика атаки с мечом.", "Задание 2: Тренировка парирования атак.",
              "Задание 3: Симуляция боя с врагом."],
        "2": ["Задание 1: Медитация для укрепления силы.", "Задание 2: Контроль над телом и разумом.",
              "Задание 3: Погружение в силовой поток."],
        "3": ["Задание 1: Стратегический анализ предыдущих сражений.", "Задание 2: Планирование тактики в бою.",
              "Задание 3: Управление ресурсами и поддержка союзников."]
    }

    while True:
        print("")

        choice = input("Введите номер выбранной тренировки или 5 чтобы завершить тренировки: ")

        if choice == "5":
            break
        elif choice in ["1", "2", "3"]:
            print(f"{player_name}: Я начинаю тренирововать {trained_skills[choice]}...")
            for task in training_tasks[choice]:
                print(task)
            print(f"{player_name}: Я усвоил урок {trained_skills[choice]}.")
        else:
            print("Ошибка! Пожалуйста, выберите допустимый вариант тренировки или 'завершить тренировки'.")
    print(f"{player_name}: Я готов к новым вызовам.!\n"
          f"Прошло пару лет с момента гибели учиетля, {player_name}, также является перспективным джедаем,который способен одалеть темную силу\n"
          f"И вот однажды выполяняя задание дждаев Люк встертился с Дартом Вейдером лицом к лицу\n"
          f"{player_name}: Я закончил последнее задание и вернулся на корабль.\n"
          "Внезапно, ты чувствуешь сильное присутствие темной силы.\n"
          "Дарт Вейдер: Ты зашёл слишком далеко, юный джедай.\n"
          f"{player_name}: Дарт Вейдер! Что ты здесь делаешь?\n"
          f"Сражение началось! Дарт Вейдер намного сильнее.\n")
    print(f"Дарт Вейдер атакует {player_name} и наносит решающий удар.\n"
          f"Дарт Вейдер: Ты побежден, {player_name}. Ты носишь в себе силу темной стороны, и ты - мой сын.\n"
          f"{player_name}: Это... Это невозможно!\n"
          f"{player_name}: Ааааааааа!\n"
          f"Вейдер отрубает руку {player_name}.\n"
          f"Дарт Вейдер: Теперь ты знаешь правду, {player_name}. И это только начало твоего обучения.\n"
          f"{player_name}: Неужели это конец...\n"
          f"Дарт Вейдер: Нет, это не конец, {player_name}.\n"
          f"Дарт Вейдер: Я - твой отец, {player_name}. И ты носишь в себе силу темной стороны.\n"
          f"{player_name}: Это... Это невозможно!\n"
          "В этот момент вмешиваются спасательный отряд и Хан Соло.\n"
          f"Хан Соло: Мы не можем дать тебе умереть, {player_name}. Мы знаем, что в тебе есть добро.\n"
          f"{player_name}: Спасибо вам, я готов продолжить свой путь.\n"
          f"Хан Соло: Ты - наш последний надежды, {player_name}. Да прибудет с тобой сила.\n")
    print(f"После битвы с Дарт Вейдером, {player_name} был ранен и потерял свою руку.\n"
          "Джедаи решили сделать протез для тебя, чтобы восстановить потерянные способности.\n"
          "Теперь у тебя есть новая рука, смешанная с механическими компонентами.\n"
          f"{player_name} решил сдаться и попытаться убедить своего отца, Дарта Вейдера, вернуться на светлую сторону.\n"
          "Дарт Вейдер: Ты сделал правильный выбор, сын.\n"
          "Однако, твои слова не убедили его. Внезапно начинается битва между вами двоими.\n"
          f"Битва началась, и вы сражаетесь с Дарт Вейдером.\n")
    player_health = 100
    enemy_health = 100

    while player_health > 0 and enemy_health > 0:
        player_damage = random.randint(10, 20)
        enemy_damage = random.randint(15, 25)

        player_health -= enemy_damage
        enemy_health -= player_damage

        print(f"{player_name}: У меня {player_health} здоровья,\n Дарт Вейдер: У меня {enemy_health} здоровья.")
        print(f"Дарт Вейдер атакует {player_name} и наносит {enemy_damage} урона.")
        print(f"{player_name} контратакует и наносит {player_damage} урона Дарт Вейдеру.")

        if player_health <= 0:
            print(f"{player_name}: Это конец, отец.")
            (print(f"{player_name}: Отец, вернись на светлую сторону \n"
                  "Дарт Вейдер: Никогда!\n"
                  f"Внезапно на сцену выходит Дарт Сидиус, учитель Дарта Вейдера.\n"
                  "Дарт Сидиус: Время окончено, Дарт Вейдер. Твоя слабость лишь удерживает тебя на светлой стороне.\n"
                  "Сидиус вмешивается в битву и атакует Дарта Вейдера.\n"
                  f"Дарт Вейдер: Подожди, учитель! Нет!"
                  f"Дарта Вейдера раняет темная сторона, и он падает на землю.\n"
                  f"Дарт Вейдер: Учитель, не покидайте меня!\n"
                  f"Дарт Сидиус: Ты слишком слаб, Вейдер.\n"
                  f"Не ожиданно Дарт Вейдер встает и убивает Дарта Сидиуса и падает так как он потерял все свои силы\n"
                  f"{player_name} понимает, что его отце вернулся и одален темную сторону силы\n"
                  f"Сразу же {player_name} бежит к своему отцу которого в прошлом звали Энакаеном Скайвокером\n"
                  f"Но {player_name} понимает, что он уже мертв\n"
                  f"После победы над Дартом Вейдером, галактика отмечает победу.\n"
                  f"На праздновании победы {player_name} видит призрак своего отца, Энакакена Скайукера, и {teacher_name}.\n"
                  f"{teacher_name} улыбается тебе и исчезает в силу.\n"
                  f"Энакен: Ты изменил меня, {player_name}. Спасибо."))
    exit()



introduction()
# show_menu()
# handle_menu_choice()

introduction()
