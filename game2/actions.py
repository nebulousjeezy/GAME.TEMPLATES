
from player import *
from items import *
from map import *


def biscuits_tutor():
    print("The tutor is pleased that you brought him another pack of biscuits so that he can feed his bad habit.")
    inventory.remove(item_biscuits)
    rooms["Tutor"]["changed"] = True
    global biscuits_given


def money_office():
    print("The cashier's prayers have been answered! You buy yourself a sandwich with the money.")
    inventory.remove(item_money)
    inventory.append(item_sandwich)
    rooms["Office"]["changed"] = True


def drop_laptop():
    print("You dropped your laptop! Why would you do that? It's broken now!")
    inventory.remove(item_laptop)


actions = {
    "biscuits tutor": biscuits_tutor,

    "money office": money_office,

    "drop laptop": drop_laptop
}