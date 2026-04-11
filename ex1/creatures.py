# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  creatures.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/08 13:16:55 by klucchin        #+#    #+#               #
#  Updated: 2026/04/09 16:05:06 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):

    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self, target=None):
        if target:
            return f"Sproutling heals {target.name} for a small amount"
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return "Bloomelle uses Petal Dance!"

    def heal(self, target=None):
        if target:
            return f"Bloomelle heals {target.name} for a large amount"
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):

    def __init__(self):
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self):
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self):
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self):
        self.transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):

    def __init__(self):
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self):
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self):
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self):
        self.transformed = False
        return "Morphagon stabilizes its form."
