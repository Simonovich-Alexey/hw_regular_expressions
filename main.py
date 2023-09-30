from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contact_list = list(rows)

# pprint(contact_list)

for i in contact_list:
    test = ", ".join(i)
    # print(test)
    name = r'^([а-яёА-ЯЁ]+)(\s|[,])?\s*([а-яёА-ЯЁ]+)(\s|[,])?\s*([а-яёА-ЯЁ]+)?'
    result_name = re.sub(name, r"\1, \3, \5", test)
    phone = r"(\+7|8)\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*)\(*(\w+.)*\s*(\d+)*"
    result_phone = re.sub(phone, r"+7(\2)\3-\4-\5\6\7\8", result_name)
    print(result_phone)


# print(result)
# new_contact_list = []
# for i in contact_list:
#     for id, j in enumerate(i):
#         print(id, j)



# with open("phonebook.csv", "w", encoding='utf-8') as f:
#     datawriter = csv.writer(f, delimiter=',')
#     datawriter.writerows(contact_list)
