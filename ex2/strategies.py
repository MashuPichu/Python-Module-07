# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  strategies.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/09 16:08:53 by klucchin        #+#    #+#               #
#  Updated: 2026/04/09 16:20:15 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from ex1.capabilities import HealCapability, TransformCapability
from .exception import InvalidStrategyError


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature):
        pass

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        _ = creature
        return True

    def act(self, creature):
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "defensive strategy"
            )

        print(creature.attack())
        print(creature.heal())
