from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

arch_folder = "archives"
csv_1_dict = dict() # тут по идее строка будет уникальнее чем число
csv_2_dict = dict() # ключем будет значение из object


def parse_xml(file):
    csv_1_list = []
    root = ET.parse(file)
    id_value = '' # запомним его для указанного файла
    name_value_list = [] # список всех значений имен в objects
    
    for elem in root.findall('.//var'):
        level_value = ''
        if elem.attrib.get('name') == 'id':
            id_value = elem.attrib.get('value')

        if elem.attrib.get('name') == 'level':
            level_value = elem.attrib.get('value')

        csv_1_dict[id_value] = level_value


    for elem in root.findall('.//object'):
        name_value = elem.attrib.get('name')
        name_value_list.append(name_value)

    for el in name_value_list:
        csv_2_dict[el] = id_value


for arch in Path(arch_folder).glob("*.zip"):
    zip_file = zipfile.ZipFile(arch)
    zip_file.extractall(Path(arch_folder, arch.stem))

    for file in Path(arch_folder, arch.stem).glob("*.xml"):
        print(file)
        parse_xml(file)
    print(arch)


with open('csv_1.csv', 'w') as f:
    for key, value in csv_1_dict.items():
        # print(key," ", value)
        # print(key, value)
        f.write(key + " " + value + "\n") 


with open('csv_2.csv', 'w') as f:
    for key, value in csv_2_dict.items():
        f.write(key + " " + value + "\n") 
