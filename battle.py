# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  battle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/08 11:02:55 by klucchin        #+#    #+#               #
#  Updated: 2026/04/08 11:44:11 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import FlameFactory as Flame, AquaFactory as Aqua


def test_factory(factory) -> None:
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(factory1, factory2) -> None:
    print("Testing battle")

    print(factory1.create_base().describe())
    print(" vs.")
    print(factory2.create_base().describe())
    print(" fight!")

    print(factory1.create_base().attack())
    print(factory2.create_base().attack())


if __name__ == "__main__":
    flame = Flame()
    aqua = Aqua()

    test_factory(flame)
    test_factory(aqua)

    battle(flame, aqua)
