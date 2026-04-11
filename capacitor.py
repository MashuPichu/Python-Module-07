# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capacitor.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/09 15:57:06 by klucchin        #+#    #+#               #
#  Updated: 2026/04/09 16:07:13 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory):
    print("Testing Creature with healing capability")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal(evolved))

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory):
    print("Testing Creature with transform capability")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(heal_factory)
    test_transform(transform_factory)
