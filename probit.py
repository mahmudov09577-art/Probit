import random
import time
import os
import string
from colorama import Fore, Style, init

# Инициализация цветов
init(autoreset=True)

# --- ГЕНЕРАТОРЫ ДАННЫХ ---
names_m = ["Иван", "Александр", "Дмитрий", "Максим", "Сергей", "Андрей", "Артем", "Михаил", "Никита", "Егор", "Кирилл", "Даниил", "Роман", "Владислав"]
names_f = ["Анна", "Мария", "Елена", "Ольга", "Наталья", "Виктория", "Алина", "Екатерина", "Полина", "Дарья", "Ксения", "Софья", "Юлия", "Валерия"]
surnames = ["Смирнов", "Иванов", "Кузнецов", "Попов", "Соколов", "Лебедев", "Козлов", "Новиков", "Морозов", "Волков", "Зайцев", "Павлов", "Семенов", "Голубев"]
patr_m = ["Иванович", "Александрович", "Дмитриевич", "Сергеевич", "Андреевич", "Алексеевич", "Михайлович", "Максимович"]
patr_f = ["Ивановна", "Александровна", "Дмитриевна", "Сергеевна", "Андреевна", "Алексеевна", "Михайловна", "Максимовна"]
cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону", "Уфа", "Красноярск"]
streets = ["Ленина", "Пушкина", "Гагарина", "Советская", "Мира", "Главная", "Садовая", "Школьная", "Лесная", "Набережная", "Кирова", "Победы"]
cars = ["BMW M5", "Audi A6", "Mercedes E-Class", "Lada Vesta", "Kia Rio", "Toyota Camry", "Hyundai Solaris", "Skoda Octavia", "Ford Focus", "Renault Logan", "Mazda 6", "Volkswagen Polo"]
operators = ["МТС", "Билайн", "Мегафон", "Tele2", "Yota"]
jobs = ["Менеджер", "Инженер", "Программист", "Водитель", "Врач", "Учитель", "Дизайнер", "Бухгалтер", "Охранник", "Директор", "Курьер", "Бариста"]
companies = ["ООО Ромашка", "АО СтройИнвест", "ИП Иванов", "ООО ТехноСервис", "ПАО Сбербанк", "Яндекс", "VK Group", "Ozon", "Wildberries", "Газпром"]
emails = ["@mail.ru", "@gmail.com", "@yandex.ru", "@bk.ru", "@list.ru", "@inbox.ru"]
browsers = ["Chrome", "Safari", "Firefox", "Edge", "Opera", "Yandex"]
isps = ["Ростелеком", "Дом.ру", "МТС", "Билайн", "ТТК"]
banks = ["Сбербанк", "Тинькофф", "Альфа-Банк", "ВТБ", "Райффайзен", "Газпромбанк"]
subscriptions = ["Netflix", "Spotify", "YouTube Premium", "Яндекс.Плюс", "Telegram Premium", "Discord Nitro"]

def get_random_string(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    banner = f"""
{Fore.CYAN}  ____  ____   ___  ____ ___ _____ 
 |  _ \\|  _ \\ / _ \\| __ )_ _|_   _|
 | |_) | |_) | | | |  _ \\| |  | |  
 |  __/|  _ <| |_| | |_) | |  | |  
 |_|   |_| \\_\\\\___/|____/___| |_|  
{Style.RESET_ALL}
{Fore.RED}   [ ФЕЙКОВЫЙ ПРОБИВ-БОТ v3.0 MEGA ]{Style.RESET_ALL}
{Fore.YELLOW}   (База: 1.4 млрд записей. Демо-режим){Style.RESET_ALL}
"""
    print(banner)

def loading_bar(text):
    print(f"{Fore.YELLOW}[*] {text}")
    for i in range(101):
        time.sleep(0.005)
        bar = '█' * (i // 2) + '-' * (50 - i // 2)
        print(f"\r{Fore.CYAN}    |{bar}| {i}%", end="")
    print("\n")

def fake_search(target):
    loading_bar(f"Глубокий поиск по всем базам для: {target}")
    for _ in range(6):
        time.sleep(0.2)
        print(f"{Fore.CYAN}    [+] Дешифровка: {random.choice(['ГИБДД', 'ФНС', 'Сбер', 'Тинькофф', 'Почта', 'ТГ', 'ВК', 'Госуслуги', 'Ozon', 'WB', 'МВидео'])}... OK")
    
    time.sleep(0.5)
    print(f"{Fore.GREEN}[+] Найдено 12 совпадений! Выгрузка данных:\n")
    time.sleep(0.3)

    # Переменные для генерации
    gender = random.choice(["М", "Ж"])
    name = random.choice(names_m) if gender == "М" else random.choice(names_f)
    surname = random.choice(surnames) + ("а" if gender == "Ж" else "")
    patr = random.choice(patr_m) if gender == "М" else random.choice(patr_f)
    city = random.choice(cities)
    
    # 1. ПАСПОРТ
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}[ БАЗА: ПАСПОРТА РФ / ФМС ]")
    print(f"║ {Fore.WHITE}ФИО:        {Fore.CYAN}{surname} {name} {patr}")
    print(f"║ {Fore.WHITE}Дата рожд.: {Fore.CYAN}{random.randint(1, 28):02d}.{random.randint(1, 12):02d}.{random.randint(1970, 2006)}")
    print(f"║ {Fore.WHITE}Место рожд.:{Fore.CYAN} г. {city}")
    print(f"║ {Fore.WHITE}Паспорт:    {Fore.CYAN}{random.randint(40, 49)}{random.randint(10, 99)} {random.randint(100000, 999999)}")
    print(f"║ {Fore.WHITE}Прописка:   {Fore.CYAN}г. {city}, ул. {random.choice(streets)}, д. {random.randint(1, 150)}, кв. {random.randint(1, 300)}")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝\n")

    # 2. ТЕЛЕФОН
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}[ БАЗА: ОПЕРАТОРЫ СВЯЗИ ]")
    print(f"║ {Fore.WHITE}Телефон:    {Fore.CYAN}+7 ({random.randint(900, 999)}) {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}")
    print(f"║ {Fore.WHITE}Оператор:   {Fore.CYAN}{random.choice(operators)}")
    print(f"║ {Fore.WHITE}Регион:     {Fore.CYAN}{city}")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝\n")

    # 3. АВТО
    if gender == "М":
        car = random.choice(cars)
        plate = f"{random.choice('АВЕКМНОРСТУХ')}{random.randint(100, 999)}{random.choice('АВЕКМНОРСТУХ')}{random.choice('АВЕКМНОРСТУХ')} {random.choice([77, 99, 177, 199, 50, 150, 750])}"
        print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════╗")
        print(f"║ {Fore.WHITE}[ БАЗА: ГИБДД / АВТО ]")
        print(f"║ {Fore.WHITE}Марка/Модель: {Fore.CYAN}{car}")
        print(f"║ {Fore.WHITE}Гос. номер:   {Fore.CYAN}{plate}")
        print(f"║ {Fore.WHITE}Цвет:         {Fore.CYAN}{random.choice(['Черный', 'Белый', 'Серебристый', 'Синий', 'Красный', 'Серый'])}")
        print(f"║ {Fore.WHITE}Штрафы:       {Fore.RED}{random.randint(0, 45)} шт. (на сумму {random.randint(500, 35000)} руб.)")
        print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝\n")

    # 4. РАБОТА И КОНТАКТЫ
    email_name = get_random_string(8)
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}[ БАЗА: РАБОТА / СОЦСЕТИ ]")
    print(f"║ {Fore.WHITE}Место работы:{Fore.CYAN} {random.choice(companies)}")
    print(f"║ {Fore.WHITE}Должность:   {Fore.CYAN}{random.choice(jobs)}")
    print(f"║ {Fore.WHITE}Зарплата:    {Fore.CYAN}~ {random.randint(30, 250)} 000 руб/мес")
    print(f"║ {Fore.WHITE}E-mail:      {Fore.CYAN}{email_name}{random.choice(emails)}")
    print(f"║ {Fore.WHITE}Telegram:    {Fore.CYAN}@{target.replace('+', '').replace('@', '')[:12]}_anviz")
    print(f"║ {Fore.WHITE}VK:          {Fore.CYAN}id{random.randint(10000000, 99999999)}")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝\n")

    # 5. БАНКИ
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}[ БАЗА: БАНКИ / КАРТЫ ]")
    print(f"║ {Fore.WHITE}Банк:        {Fore.CYAN}{random.choice(banks)}")
    print(f"║ {Fore.WHITE}Карта:       {Fore.CYAN}{random.randint(4000, 4999)} **** **** {random.randint(1000, 9999)}")
    print(f"║ {Fore.WHITE}Баланс:      {Fore.GREEN}{random.randint(100, 950000)} руб.")
    print(f"║ {Fore.WHITE}Кредиты:     {Fore.RED}{random.choice(['Нет', 'Есть (1)', 'Есть (2)', 'Просрочка'])}")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝\n")

    # 6. ПАРОЛИ / СЛИВЫ
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}[ БАЗА: СЛИВЫ ПАРОЛЕЙ (COMBOLIST) ]")
    print(f"║ {Fore.WHITE}{email_name}@mail.ru : {Fore.RED}{get_random_string(10)}")
    print(f"║ {Fore.WHITE}{email_name}@gmail.com : {Fore.RED}{get_random_string(8)}!")
    print(f"║ {Fore.WHITE}vk.com/id{random.randint(10000000, 99999999)} : {Fore.RED}{get_random_string(12)}")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝\n")

    # 7. ПОДПИСКИ И УСТРОЙСТВА
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}[ БАЗА: ЦИФРОВОЙ СЛЕД ]")
    print(f"║ {Fore.WHITE}Устройство:  {Fore.CYAN}{random.choice(['iPhone 13', 'iPhone 14 Pro', 'Samsung S22', 'Xiaomi Redmi', 'PC (Windows 11)'])}")
    print(f"║ {Fore.WHITE}Браузер:     {Fore.CYAN}{random.choice(browsers)}")
    print(f"║ {Fore.WHITE}IP-Адрес:    {Fore.CYAN}{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)} ({random.choice(isps)})")
    print(f"║ {Fore.WHITE}Подписки:    {Fore.CYAN}{random.choice(subscriptions)} (Активна)")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝\n")
    
    print(f"{Fore.RED}[!] Внимание: Это фейковые данные для игры! Не является реальным пробивом.\n")

if __name__ == "__main__":
    print_banner()
    while True:
        target = input(f"\n{Fore.GREEN}Введи номер телефона, ник или e-mail цели: {Style.RESET_ALL}")
        
        if target.lower() == '/exit':
            print(f"{Fore.RED}Выход...")
            break
            
        if target.strip() == "":
            print(f"{Fore.RED}Ошибка: пустой запрос.")
        else:
            fake_search(target)
