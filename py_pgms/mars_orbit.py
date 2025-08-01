s = int(input("Enter speed (km/hr): "))


def mars_orbit(s):
    hours = 225000000/s
    days = hours/24
    return days


print(mars_orbit(s))
