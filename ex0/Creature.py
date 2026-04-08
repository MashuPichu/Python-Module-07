# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Creature.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/22 14:11:56 by klucchin        #+#    #+#               #
#  Updated: 2026/04/08 11:22:13 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, types: str):
        self.name = name
        self.types = types

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.types} type creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire")

    def attack(self):
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self):
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self):
        return f"{self.name} uses Hydro Pump!"
