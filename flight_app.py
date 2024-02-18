def create_flight():
    flight_number = input("Введите номер рейса (XXXX): ").upper()
    if len(flight_number) != 4 or not flight_number.isalnum():
        print("Некорректный формат номера рейса.")
        return


    departure_date = input("Введите дату вылета (ДД/ММ/ГГГГ): ")
    if len(departure_date) != 10:
        print("Некорректный формат даты вылета.")
        return

    departure_time = input("Введите время вылета (ЧЧ:ММ): ")
    if len(departure_time) != 5:
        print("Некорректный формат времени вылета.")
        return

    flight_duration = input("Введите время перелета (ЧЧ.ММ): ")
    if not is_valid_flight_duration(flight_duration):
        print("Некорректный формат времени перелета.")
        return

    source_airport = input("Введите код ИАТА аэропорта вылета (XXX): ").upper()
    if len(source_airport) != 3 or not source_airport.isalpha():
        print("Некорректный формат кода ИАТА аэропорта вылета.")
        return

    destination_airport = input("Введите код ИАТА аэропорта прилета (XXX): ").upper()
    if len(destination_airport) != 3 or not destination_airport.isalpha():
        print("Некорректный формат кода ИАТА аэропорта прилета.")
        return

    price = input("Введите стоимость авиабилета: ")
    if not is_valid_price(price):
        print("Некорректный формат стоимости авиабилета.")
        return

    flight_info = {
        "flight_number": flight_number,
        "departure_date": departure_date,
        "departure_time": departure_time,
        "flight_duration": flight_duration,
        "source_airport": source_airport,
        "destination_airport": destination_airport,
        "price": price
    }

    return flight_info


def is_valid_flight_duration(flight_duration):
    try:
        hours, minutes = flight_duration.split(".")
        hours = int(hours)
        minutes = int(minutes)
        return len(flight_duration) == 5 and hours >= 0 and hours < 24 and minutes >= 0 and minutes < 60
    except ValueError:
        return False


def is_valid_price(price):
    try:
        price = float(price)
        return price >= 0
    except ValueError:
        return False

flights = []

while True:
    print("Главное меню:")
    print("1. Создать новый рейс")
    print("2. Вывести информацию обо всех рейсах")
    print("3. Вывести информацию о конкретном рейсе")
    print("4. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        flight_info = create_flight()
        if flight_info:
            flights.append(flight_info)
            print("Информация о рейсе добавлена.")

    elif choice == "2":
        if not flights:
            print("Нет доступных рейсов.")
        else:
            for flight in flights:
                print(f"Номер рейса: {flight['flight_number']}")
                print(f"Дата вылета: {flight['departure_date']}")
                print(f"Время вылета: {flight['departure_time']}")
                print(f"Время перелета: {flight['flight_duration']}")
                print(f"ИАТА аэропорта вылета: {flight['source_airport']}")
                print(f"ИАТА аэропорта прилета: {flight['destination_airport']}")
                print(f"Стоимость авиабилета: {flight['price']}")
                print("-" * 20)

    elif choice == "3":
        if not flights:
            print("Нет доступных рейсов.")
        else:
            flight_number = input("Введите номер рейса: ").upper()
            for flight in flights:
                if flight['flight_number'] == flight_number:
                    print(f"Номер рейса: {flight['flight_number']}")
                    print(f"Дата вылета: {flight['departure_date']}")
                    print(f"Время вылета: {flight['departure_time']}")
                    print(f"Время перелета: {flight['flight_duration']}")
                    print(f"ИАТА аэропорта вылета: {flight['source_airport']}")
                    print(f"ИАТА аэропорта прилета: {flight['destination_airport']}")
                    print(f"Стоимость авиабилета: {flight['price']}")
                    break
            else:
                print("Рейс с указанным номером не найден.")

    elif choice == "4":
        break

    else:
        print("Некорректный номер действия.")
