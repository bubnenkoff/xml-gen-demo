import random
import string
import zipfile
import glob
from pathlib import Path

number_of_archives = 51

class GenXML:
    def __init__(self):
        self.ob_list = []
        self.gen_obj()

    def gen_obj(self):
        self.ob_list.append("<objects>")
        for i in range(random.randrange(10)):
            random_value_str = ''.join(random.choice(string.ascii_letters) for i in range(6))
            my_str = " <object name='{0}'/>".format(random_value_str)
            self.ob_list.append(my_str)
        self.ob_list.append("</objects>")

    def __repr__(self):
        random_id_value_str = ''.join(random.choice(string.ascii_letters) for i in range(6))
        random_level_value = random.randrange(100)
        result = "<root>" + '\n' + \
                 " <var name='id' value='{0}'/>".format(random_id_value_str) + '\n' + \
                 " <var name='level' value='{0}'/> ".format(random_level_value) + '\n'

        for el in self.ob_list:
            result += el + '\n' 

        result += '</root>'
        return result

def start():
    for i in range(1, number_of_archives):
        zip_name = "archives/" + str(i) + ".zip"
        print(zip_name, " created")
        with zipfile.ZipFile(zip_name, "w") as myzip: 
            for i in range(1,101):
                myxml = GenXML()
                single_xml_file_content = repr(myxml)
                fname = "out/" + str(i) + '.xml'
                f = open(fname, "w")
                f.write(single_xml_file_content)

            for f in Path("out/").glob("*.xml"):
                myzip.write(f, f.name)
                f.unlink()           


def prepare():
    if not Path("out").exists():
        Path("out").mkdir()

    if not Path("archives").exists():
        Path("archives").mkdir() 


prepare()    
start()    


