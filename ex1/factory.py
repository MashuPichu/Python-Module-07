# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  factory.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/09 15:55:40 by klucchin        #+#    #+#               #
#  Updated: 2026/04/09 15:55:57 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.factory import CreatureFactory
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):

    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
