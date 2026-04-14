# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capabilities.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/08 12:54:17 by klucchin        #+#    #+#               #
#  Updated: 2026/04/14 14:01:45 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Creature import Creature
from abc import ABC, abstractmethod


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        pass


class TransformCapability(ABC):

    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
