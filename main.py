import csv
import re


contact_list = []
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    for i in rows:
        contact = ", ".join(i)
        # Регулярка для разбивки ФИО
        pattern_name_1 = r'^([а-яёА-ЯЁ]+)\s([а-яёА-ЯЁ]+)\s([а-яёА-ЯЁ]+)(,\s){2}'
        result_name_1 = re.sub(pattern_name_1, r"\1, \2, \3", contact)
        # Регулярка для разбивки ФИ
        pattern_name_2 = r'^([а-яёА-ЯЁ]+)\s([а-яёА-ЯЁ]+)(,\s)'
        result_name_2 = re.sub(pattern_name_2, r"\1, \2", result_name_1)
        # Регулярка для разбивки Ф+ИО
        pattern_name_3 = r'^([а-яёА-ЯЁ]+)[,]\s([а-яёА-ЯЁ]+)\s([а-яёА-ЯЁ]+)(,\s)'
        result_name_3 = re.sub(pattern_name_3, r"\1, \2, \3", result_name_2)
        # Регулярка для форматирования телефонов
        pattern_phone = r"(\+7|8)\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*)\(*(\w+.)*\s*(\d+)*"
        result_phone = re.sub(pattern_phone, r"+7(\2)\3-\4-\5\6\7\8", result_name_3)

        contact_list.append(result_phone.split(', '))

dict_contacts = {}
for item in contact_list:
    unique = f"{item[0]} {item[1]} {item[2]}"
    if unique in dict_contacts:
        for ids, value in enumerate(dict_contacts.get(unique)):
            if not value:
                dict_contacts.get(unique)[ids] = item[ids]
    else:
        dict_contacts.update({unique: [item[0], item[1], item[2], item[3], item[4], item[5], item[6]]})


with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator="\r")
    datawriter.writerows([value for value in dict_contacts.values()])
