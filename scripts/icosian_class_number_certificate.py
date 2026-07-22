#!/usr/bin/env python3
"""Exact Eichler-mass certificate for class number one of the icosian order."""
from fractions import Fraction


def bernoulli2(x: Fraction) -> Fraction:
    return x*x - x + Fraction(1, 6)


def chi5(a: int) -> int:
    r = a % 5
    if r == 0:
        return 0
    return 1 if r in (1, 4) else -1


def main() -> None:
    # Generalized Bernoulli number B_{2,chi} = f * sum chi(a) B_2(a/f).
    f = 5
    b2chi = f * sum((chi5(a) * bernoulli2(Fraction(a, f)) for a in range(1, f + 1)), Fraction(0))
    l_minus_1 = -b2chi / 2
    zeta_minus_1 = Fraction(-1, 12)
    zeta_f_minus_1 = zeta_minus_1 * l_minus_1

    # For degree 2 and no finite ramification, Eichler mass is
    # 2^(1-n) * h_F * |zeta_F(-1)|.
    degree = 2
    class_number_f = 1
    mass = Fraction(1, 2 ** (degree - 1)) * class_number_f * abs(zeta_f_minus_1)

    norm_one_units = 120
    central_norm_one_units = 2  # {+1,-1}
    projective_unit_group = norm_one_units // central_norm_one_units
    represented_class_weight = Fraction(1, projective_unit_group)

    print("B2_chi5", b2chi)
    print("L_minus_1_chi5", l_minus_1)
    print("zeta_F_minus_1", zeta_f_minus_1)
    print("field_class_number", class_number_f)
    print("eichler_mass", mass)
    print("norm_one_units", norm_one_units)
    print("projective_unit_group_order", projective_unit_group)
    print("represented_class_weight", represented_class_weight)
    print("mass_equals_represented_weight", mass == represented_class_weight)

    if zeta_f_minus_1 != Fraction(1, 30):
        raise SystemExit("unexpected Dedekind zeta value")
    if mass != Fraction(1, 60):
        raise SystemExit("unexpected Eichler mass")
    if represented_class_weight != mass:
        raise SystemExit("represented class does not exhaust the mass")

    print("maximal_order_right_class_number=1")


if __name__ == "__main__":
    main()