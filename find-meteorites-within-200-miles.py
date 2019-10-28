import math

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h)

for item in test:
    try:
        item.get('reclat')
        a = item.get('reclat')
        item.get('reclong')
        b = item.get('reclong')
        dist = calc_dist(float(a), float(b), 52.7941, -6.1649)
        if dist < 200.0:
            print(item.get('name'))
            print(calc_dist(float(a), float(b), 52.7941, -6.1649))
    except:
        pass

)
