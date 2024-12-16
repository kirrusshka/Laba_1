#класс дом
class House:
    def __init__(self, addres, price_per_night, num_rooms):
        self.addres = addres
        self.price_per_night = price_per_night
        self.num_rooms = num_rooms

    def back_to_file(self):
        return{
            "addres": self.addres,
            "price_per_night": self.price_per_night,
            "num_rooms": self.num_rooms
        }
    
#класс квартира
class Apartment(House):
    def __init__(self, addres, price_per_night, num_rooms, floor):
        super().__init__(addres, price_per_night, num_rooms)
        self.floor = floor

    def back_to_file(self):
        Apartment = super().back_to_file()
        Apartment.update({
            "floor": self.floor
        })
        return Apartment
    
    def get_Apartment(self):
        print("Адрес: ", self.addres, "Цена за ночь: ", self.price_per_night, "Кол-во комнат: ", self.num_rooms, "Этаж: ", self.floor, sep = '\n')
        

#класс бани   
class Baths(House):
    def __init__(self, addres, price_per_night, num_rooms, has_sauna):
        super().__init__(addres, price_per_night, num_rooms)
        self.has_sauna = has_sauna

    def back_to_file(self):
        baths = super().back_to_file()
        baths.update({
            "has_sauna": self.has_sauna
        })
        return baths
    
    def get_Baths(self):
        print("Адрес: ", self.addres, "Цена за ночь: ", self.price_per_night, "Кол-во комнат: ", self.num_rooms, "Наличие сауны: ", self.has_sauna, sep = '\n')

#класс коттедж    
class Cottage(House):
    def __init__(self, addres, price_per_night, num_rooms, garden_area):
        super().__init__(addres, price_per_night, num_rooms)
        self.garden_area = garden_area

    def back_to_file(self):
        cottage = super().back_to_file()
        cottage.update({
            "garden_area": self.garden_area
        })
        return cottage
    def get_Cottage(self):
        print("Адрес: ", self.addres, "Цена за ночь: ", self.price_per_night, "Кол-во комнат: ", self.num_rooms, "Площадь сада (м²): ", self.garden_area, sep = '\n')
    
#класс дачи
class Dacha(House):
    def __init__(self, addres, price_per_night, num_rooms, has_pool):
        super().__init__(addres, price_per_night, num_rooms)
        self.has_pool = has_pool

    def back_to_file(self):
        dacha = super().back_to_file()
        dacha.update({
            "has_pool": self.has_pool
        })
        return dacha
    
    def get_Dacha(self):
        print("Адрес: ", self.addres, "Цена за ночь: ", self.price_per_night, "Кол-во комнат: ", self.num_rooms, "Наличие бассейна: ", self.has_pool, sep = '\n')
    