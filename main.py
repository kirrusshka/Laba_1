from classes import Apartment, Baths, Cottage, Dacha
import json_job


def price_try(price):
    try:
        if (int(price) < 1000):
            print("Нету такой цены :(")
        else:
            flag = True
            return flag
    except Exception as e:
            print(f"Ошибка: {e}")


def main():
    choice = ''

    list_Apartment = []
    count_Apartment = -1
    list_Baths = []
    count_Baths = -1
    list_Cottage = []
    count_Cottage = -1
    list_Dacha = []
    count_Dacha = -1

    while (choice != '13'):
        print("\n--- Выберите что хотите забронировать ---")
        print("1. Квартиру")
        print("2. Баню")
        print("3. Коттедж")
        print("4. Дача")
        print("5. Добавить квартиру в json")
        print("6. Удалить квартиру в json")
        print("7. Добавить баню в json")
        print("8. Удалить баню в json")
        print("9. Добавить коттедж в json")
        print("10. Удалить коттедж в json")
        print("11. Добавить дачу в json")
        print("12. Удалить дачу в json")
        print("13. Выход")

        choice = input().strip()

        if choice == '1':
            addres = input("Введите адрес квартиры: ")
            flag = False

            while (flag != True):
                price_per_night = input("Введите цену за ночь: ")
                flag = price_try(price_per_night)
            num_rooms = input("Введите кол-во комнат: ")
            floor = input("Введите этаж: ")
            list_Apartment.append(Apartment(addres, price_per_night, num_rooms, floor))
            count_Apartment += 1
            print('Введенные данные:')
            list_Apartment[count_Apartment].get_Apartment()
            print(f"Вы успешно забронировали квартиру под номером {count_Apartment}")
            

        elif choice == '2':
            addres = input("Введите адрес бани: ")
            flag = False

            while (flag != True):
                price_per_night = input("Введите цену за ночь: ")
                flag = price_try(price_per_night)
            num_rooms = input("Введите кол-во комнат: ")
            has_sauna = input("Есть ли сауна? (да/нет): ")
            list_Baths.append(Baths(addres, price_per_night, num_rooms, has_sauna))
            print('Введенные данные:')
            list_Baths[count_Baths].get_Baths()
            print("Вы успешно забронировали баню")

        elif choice == '3':
            addres = input("Введите адрес коттеджа : ")
            flag = False

            while (flag != True):
                price_per_night = input("Введите цену за ночь: ")
                flag = price_try(price_per_night)
            num_rooms = input("Введите кол-во комнат: ")
            garden_area = input("Введите площадь сада (м²): ")
            list_Cottage.append(Cottage(addres, price_per_night, num_rooms, garden_area))
            print('Введенные данные:')
            list_Cottage[count_Cottage].get_Cottage()
            print("Вы успешно забронировали коттедж")

        elif choice == '4':
            addres = input("Введите адрес дачи : ")
            flag = False

            while (flag != True):
                price_per_night = input("Введите цену за ночь: ")
                flag = price_try(price_per_night)
            num_rooms = input("Введите кол-во комнат: ")
            has_pool = input("Есть ли бассейн? (да/нет): ")
            list_Dacha.append(Dacha(addres, price_per_night, num_rooms, has_pool))
            print('Введенные данные:')
            list_Dacha[count_Dacha].get_Dacha()
            print("Вы успешно забронировали дачу")

        elif choice == '5':
            if len(list_Apartment) > 0:
                print("Доступные номера квартир:")

                for i in range(len(list_Apartment)):
                    print(i)
                number = -1

                while(number < 0 or number >= len(list_Apartment)):
                    number = int(input(print("Введите номер квартиры:")))
                
                print(f"Номер вашей квартиры {number}")
                file_name = 'data.json'
                data = json_job.start_json(file_name)
                handler = json_job
                handler.add_Apartment(data, list_Apartment[number])
                handler.save_json(data, file_name)

            else:
                print("Квартир пока нет в брони.")

        elif choice == '6':
            addres = input('Введите, какую квартиру по адресу вы хотите удалить: ')
            file_name = 'data.json'
            data = json_job.start_json(file_name)
            handler = json_job
            handler.delete_Apartment(data, addres)
            handler.save_json(data, file_name)
        
        elif choice == '7':
            if len(list_Baths) > 0:
                print("Доступные номера бань:")

                for i in range(len(list_Baths)):
                    print(i)
                number = -1

                while(number < 0 or number >= len(list_Baths)):
                    number = int(input(print("Введите номер дачи:")))
                
                print(f"Номер вашей бани {number}")
                file_name = 'data.json'
                data = json_job.start_json(file_name)
                handler = json_job
                handler.add_Baths(data, list_Baths[number])
                handler.save_json(data, file_name)

            else:
                print("Дач пока нет в брони.")

        elif choice == '8':
            addres = input('Введите, какую баню по адресу вы хотите удалить: ')
            file_name = 'data.json'
            data = json_job.start_json(file_name)
            handler = json_job
            handler.delete_Baths(data, addres)
            handler.save_json(data, file_name)

        elif choice == '9':
            if len(list_Cottage) > 0:
                print("Доступные номера коттедж:")

                for i in range(len(list_Cottage)):
                    print(i)
                number = -1

                while(number < 0 or number >= len(list_Cottage)):
                    number = int(input(print("Введите номер коттедж:")))
                
                print(f"Номер вашей коттедж {number}")
                file_name = 'data.json'
                data = json_job.start_json(file_name)
                handler = json_job
                handler.add_Cottage(data, list_Cottage[number])
                handler.save_json(data, file_name)

            else:
                print("Коттеджей пока нет в брони.")

        elif choice == '10':
            addres = input('Введите, какой коттедж по адресу вы хотите удалить: ')
            file_name = 'data.json'
            data = json_job.start_json(file_name)
            handler = json_job
            handler.delete_Cottage(data, addres)
            handler.save_json(data, file_name)
        
        elif choice == '11':
            if len(list_Dacha) > 0:
                print("Доступные номера дач:")

                for i in range(len(list_Dacha)):
                    print(i)
                number = -1

                while(number < 0 or number >= len(list_Dacha)):
                    number = int(input(print("Введите номер дач:")))
                
                print(f"Номер вашей дачи {number}")
                file_name = 'data.json'
                data = json_job.start_json(file_name)
                handler = json_job
                handler.add_Dacha(data, list_Dacha[number])
                handler.save_json(data, file_name)

            else:
                print("Дач пока нет в брони.")

        elif choice == '12':
            addres = input('Введите, какую дачу по адресу вы хотите удалить: ')
            file_name = 'data.json'
            data = json_job.start_json(file_name)
            handler = json_job
            handler.delete_Dacha(data, addres)
            handler.save_json(data, file_name)

        elif choice == '13':
            return ''
        
        else:
            print("Такого номера не существует")



main()