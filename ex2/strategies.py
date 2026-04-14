# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  strategies.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/09 16:08:53 by klucchin        #+#    #+#               #
#  Updated: 2026/04/14 14:12:12 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from ex1.capabilities import HealCapability, TransformCapability
from .exception import InvalidStrategyError
from ex0.Creature import Creature


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        _ = creature
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy"
            )

        assert isinstance(creature, TransformCapability)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "defensive strategy"
            )

        assert isinstance(creature, HealCapability)
        print(creature.attack())
        print(creature.heal())
