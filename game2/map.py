from items import *

room_reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "changed": False,

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},

    "items": [item_biscuits, item_handbook],

    "actions": {
        ("drop", "laptop"): "drop laptop"
    }
}

room_admins = {
    "name": "MJ and Simon's room",

    "description":
    """You are leaning against the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "changed": False,

    "exits":  {"north": "Reception"},

    "items": [],

    "actions": {
        ("drop", "laptop"): "drop laptop"
    }
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "changed": False,

    "alt description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and your pack
of biscuits. He seems to be enjoying them!
The reception is to the west.""",

    "exits": {"west": "Reception"},

    "items": [],

    "actions": {
        ("drop", "biscuits"): "biscuits tutor",

        ("drop", "laptop"): "drop laptop"
    }
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "changed": False,

    "exits": {"east": "Office", "south": "Reception"},

    "items": [],

    "actions": {
        ("drop", "laptop"): "drop laptop"
    }
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "changed": False,

    "alt description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier seems to be tidying up now.
If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "Parking"},

    "items": [item_pen],

    "actions": {
        ("drop", "money"): "money office",

        ("drop", "laptop"): "drop laptop"
    }
}


rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}