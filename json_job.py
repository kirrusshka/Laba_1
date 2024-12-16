import json


def save_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

#создаёт ячейки по кодовым словам
def start_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_Apartment(data, Apartment):
    data['Apartments'].append(Apartment.back_to_file())

def delete_Apartment(data, addres):
    data["Apartments"] = [Apartment for Apartment in data["Apartments"] if Apartment['addres'] != addres]  

def add_Baths(data, Baths):
    data['Bathss'].append(Baths.back_to_file())

def delete_Baths(data, addres):
    data["Bathss"] = [Baths for Baths in data["Bathss"] if Baths['addres'] != addres]  

def add_Cottage(data, Cottage):
    data['Cottages'].append(Cottage.back_to_file())

def delete_Cottage(data, addres):
    data["Cottages"] = [Cottage for Cottage in data["Cottages"] if Cottage['addres'] != addres]  

def add_Dacha(data, Dacha):
    data['Dachas'].append(Dacha.back_to_file())

def delete_Dacha(data, addres):
    data["Dachas"] = [Dacha for Dacha in data["Dachas"] if Dacha['addres'] != addres]  