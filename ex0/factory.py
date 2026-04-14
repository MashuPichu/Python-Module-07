# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  factory.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/08 11:11:35 by klucchin        #+#    #+#               #
#  Updated: 2026/04/14 13:46:14 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from .Creature import Flameling, Pyrodon, Aquabub, Torragon, Creature


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):

    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
