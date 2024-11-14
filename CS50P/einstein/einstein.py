def main():
    # Asking for mass
    mass = int(input("m: "))

    # Calling function calculating energy
    joule = energy(mass)

    print("E: ", joule)


def energy(mass):
    # Calculating energy
    return mass * 300000000 * 300000000


main()
