import random
from math import sin, cos, radians, pi, sqrt, atan2


class Coord:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def delta_rads(self, lat, lon):
        self.lat += lat
        self.lon += lon

    def distance_to_in_meters(self, coord, planet_radius_km=6371000):
        meters = self.__distance_to(coord, planet_radius_km)
        meters = round(meters, 3)
        return meters

    def distance_to_in_kilometers(self, coord, planet_radius_km=6371000):
        meters = self.__distance_to(coord, planet_radius_km)
        km = round(meters / 1000, 3)
        return km

    def __distance_to(self, coord, planet_radius_km):
        lon1 = self.lon
        lat1 = self.lat
        lon2 = coord.lon
        lat2 = coord.lat
        phi_1 = radians(lat1)
        phi_2 = radians(lat2)
        delta_phi = radians(lat2 - lat1)
        delta_lambda = radians(lon2 - lon1)
        a = sin(delta_phi / 2.0) ** 2 + cos(phi_1) * cos(phi_2) * sin(delta_lambda / 2.0) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        meters = planet_radius_km * c
        return meters

    def __repr__(self):
        return "lat: " + str(self.lat) + " lon: " + str(self.lon)


def add_delta_in_km_to_coord(coord, d_lat_km, d_lon_km, planet_radius_km=6371):
    lat = coord.lat
    lon = coord.lon
    d_lat = (180 / pi) * (d_lat_km / float(planet_radius_km))
    d_lon = (180 / pi) * (d_lon_km / float(planet_radius_km)) / cos(radians(lat))

    return Coord(lat + d_lat, lon + d_lon)


def create_west_random_point(dest, radius):
    degree = random.randint(-90, 90)
    d_lat_km = cos(radians(degree)) * radius
    d_lon_km = sin(radians(degree)) * radius
    origin = Coord(dest.lat, dest.lon)
    origin = add_delta_in_km_to_coord(origin, -d_lat_km, d_lon_km)
    return origin


def create_east_random_point(dest, radius):
    degree = random.randint(-90, 90)
    d_lat_km = cos(radians(degree)) * radius
    d_lon_km = sin(radians(degree)) * radius
    origin = Coord(dest.lat, dest.lon)
    origin = add_delta_in_km_to_coord(origin, +d_lat_km, d_lon_km)
    return origin
