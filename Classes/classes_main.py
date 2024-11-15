import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from Database import datbase_main as DBm

humans = ["Asher", "Aion", "Tayahar", "Zinner", "Ryuan", "Norne", "Vildian", "Daevar", "Kwa", "Celsus"]
nephilim = ["Sylvian", "Jayan", "DAnjayni", "Ebudan", "Daimah", "Dukzarist"]

def get_race(char=""):
    race = DBm.call_one(char,"Player_information","Race")
    return race

def check_bonus(race=""):
    if race in humans:
        return "you are human, no bonus for you"
    if race in nephilim:
        return "you get a bonus"