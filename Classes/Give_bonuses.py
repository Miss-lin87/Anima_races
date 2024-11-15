import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from Database import datbase_main as DBm
from main import Character

def Sylvian(char=Character):
    DBm.add_to_data(char,"Resistances","Magic",10)
    DBm.add_to_data(char,"Resistances","Psychic",10)
    DBm.add_to_data(char,"Resistances","Disease",20)
    DBm.add_to_data(char,"Resistances","Physical",5)
    DBm.add_to_data(char,"Resistances","Poison",5)
    DBm.add_to_data(char,"Combat_stats", "Regeneration",1)
    return
    
def Jayan(char=Character):
    DBm.add_to_data(char,"Player_information","Size",2)
    DBm.add_to_data(char,"Player_information","Fatigue",1)
    DBm.add_to_data(char,"Resistances","Physical",15)
    DBm.add_to_data(char,"Physical_Abilities","Strength",1)
    DBm.add_to_data(char,"Resistances","Magic",-10)
    return

def DAnjayni():
    print("Undetectebale")
    print("Ki + 30")
    return

def Ebudan():
    print("Angel packt")
    return

def Daimah(char=Character):
    print("Regeneration 3 in woods")
    DBm.add_to_data(char,"Player_information","Size",-1)
    return

def Dukzarist(char=Character):
    gender = DBm.call_one(char, "Player_information", "Gender")
    if gender == "Male":
        DBm.add_to_data(char,"Resistances","Magic",15)
        DBm.add_to_data(char,"Resistances","Psychic",15)
        DBm.add_to_data(char,"Resistances","Disease",15)
        DBm.add_to_data(char,"Resistances","Physical",20)
        DBm.add_to_data(char,"Resistances","Poison",15)
    elif gender == "Female":
        DBm.add_to_data(char,"Resistances","Magic",20)
        DBm.add_to_data(char,"Resistances","Psychic",15)
        DBm.add_to_data(char,"Resistances","Disease",15)
        DBm.add_to_data(char,"Resistances","Physical",15)
        DBm.add_to_data(char,"Resistances","Poison",15)
    DBm.add_to_data(char,"Combat_stats","Regeneration",1)
    return

def get_bonuses(input=""):
    bonuses = {"DAnjayni":DAnjayni, "Sylvian":Sylvian, "Jayan":Jayan, "Ebudan":Ebudan, "Daimah":Daimah, "Dukzarist":Dukzarist}
    x = bonuses[input]
    return x()