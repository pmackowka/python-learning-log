# Jak 062-nested-loops/main-3.py, ale generatorem zamiast listy - trasy lotnicze.
ports = [
    "WAW",
    "KRK",
    "GDN",
    "KTW",
    "WMI",
    "WRO",
    "POZ",
    "RZE",
    "SZZ",
    "LUZ",
    "BZG",
    "LCJ",
    "SZY",
    "IEG",
    "RDO",
]

routes = ((start, stop) for start in ports for stop in ports)

counter = 0
for start, stop in routes:
    print(f"{start} - {stop}")
    counter += 1

print(counter)

##########

routes = ((start, stop) for start in ports for stop in ports if start != stop)

counter = 0
for start, stop in routes:
    print(f"{start} - {stop}")
    counter += 1

print(counter)

##########

routes = ((start, stop) for start in ports for stop in ports if start < stop)

counter = 0
for start, stop in routes:
    print(f"{start} - {stop}")
    counter += 1

print(counter)
