def cel_to_fahr(cel):
    return 1.8 * cel + 32


def fahr_to_cel(fahr):
    return 5/9 * (fahr - 32)


def kelvin_to_rank(kel):
    return 1.8 * kel + 0.6


def fahr_to_rank(fahr):
    return fahr + 460


def rank_to_kelvin(rank):
    return 5/9 * (rank - 0.6)


def cel_to_kelvin(cel):
    return cel + 273


def kelvin_to_cel(kel):
    return kel - 273


def kelvin_to_fahr(kel):
    return 1.8 * (kel - 273) + 32


def fahr_to_kelvin(fahr):
    return 5/9 * (fahr - 32) + 273

