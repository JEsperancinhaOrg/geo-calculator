import math
import random


class Coord:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def delta(self, lat, lon):
        self.lat += lat
        self.lon += lon

    def distanceTo(self, coord, planet_radius_km=6371000):
        lon1 = self.lon
        lat1 = self.lat
        lon2 = coord.lon
        lat2 = coord.lat
        phi_1 = math.radians(lat1)
        phi_2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        meters = planet_radius_km * c
        km = meters / 1000.0

        meters = round(meters, 3)
        km = round(km, 3)

        print(f"Distance: {meters} m")
        print(f"Distance: {km} km")

    def __repr__(self):
        return "lat: " + str(self.lat) + " lon: " + str(self.lon)


def add_delta_in_km_to_coord(coord, d_lat_km, d_lon_km, planet_radius_km=6371):
    lat = coord.lat
    lon = coord.lon
    d_lat = (180 / math.pi) * (d_lat_km / float(planet_radius_km))
    d_lon = (180 / math.pi) * (d_lon_km / float(planet_radius_km)) / math.cos(math.radians(lat))

    return Coord(lat + d_lat, lon + d_lon)


def create_west_random_point(dest, radius):
    degree = random.randint(-90, 90)
    d_lat_km = math.cos(math.radians(degree)) * radius
    d_lon_km = math.sin(math.radians(degree)) * radius
    origin = Coord(dest.lat, dest.lon)
    origin = add_delta_in_km_to_coord(origin, -d_lat_km, d_lon_km)
    return origin


def create_east_random_point(dest, radius):
    degree = random.randint(-90, 90)
    d_lat_km = math.cos(math.radians(degree)) * radius
    d_lon_km = math.sin(math.radians(degree)) * radius
    origin = Coord(dest.lat, dest.lon)
    origin = add_delta_in_km_to_coord(origin, +d_lat_km, d_lon_km)
    return origin


if __name__ == '__main__':
    coord1 = Coord(52.0865204, 5.0378913)
    coord2 = Coord(52.0688916, 5.1120921)

    coord1.distanceTo(coord2)
