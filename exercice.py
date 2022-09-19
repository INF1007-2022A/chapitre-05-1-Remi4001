#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = -number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []

    for char in prefixes:
        names += [char + suffixe]

    return names


def prime_integer_summation() -> int:
    somme = 0
    nombre = 0

    i = 0
    while i < 100:
        if is_prime(nombre):
            somme += nombre
            i += 1
        nombre += 1

    return somme


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    else:
        i = 2
        sqrt = int(number ** 0.5)

        while i <= sqrt:
            if number % i == 0:
                return False

            i += 1

        return True


def factorial(number: int) -> int:
    facto = 1
    for i in range(number):
        i += 1
        facto *= i
    return facto


def use_continue() -> None:
    i = 0
    while i <= 10:
        i += 1
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    accepted = [bool]

    for i in range(len(groups)):
        groups[i].sort()
        match groups[i]:
            case group if len(group) <= 3 or len(group) > 10:
                accepted.insert(i, False)
            case group if 25 in group:
                accepted.insert(i, True)
            case group if group[0] < 18:
                accepted.insert(i, False)
            case group if group[-1] > 70 and 50 in group:
                accepted.insert(i, False)
            case _:
                accepted.insert(i, True)

    return accepted


def main() -> None:
    number = -4.325
    print(
        f"La valeur absolue du nombre {number} est "
        f"{convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(
        "La somme des 100 premiers nombre premier est : "
        f"{prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print("L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [
            70, 50, 26, 28], [75, 50, 18, 25],
        [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
