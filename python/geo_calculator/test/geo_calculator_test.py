import unittest

from geo_calculator import add_delta_in_km_to_coord, Coord


class CoordTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_delta_in_km_to_coord(self):
        coord = Coord(53.32055555555556, -1.7297222222222221)

        new_coord = add_delta_in_km_to_coord(coord, 0, 10)

        self.assertEqual(53.32055555555556, new_coord.lat)
        self.assertEqual(-1.579167190360281, new_coord.lon)

    def test_distance_to_in_meters_one_place(self):
        coord1 = Coord(52.0673599, 5.1102121)
        coord2 = Coord(52.08608282419939, 5.109284354540611)

        self.assertEqual(2082.859, coord1.distance_to_in_meters(coord2))
        self.assertEqual(2.083, coord1.distance_to_in_kilometers(coord2))

    def test_distance_to_in_meters_two_place(self):
        coord1 = Coord(52.0673599, 5.1102121)
        coord3 = Coord(52.366336822509766, 4.903250694274902)

        self.assertEqual(36111.006, coord1.distance_to_in_meters(coord3))
        self.assertEqual(36.111, coord1.distance_to_in_kilometers(coord3))

    def test_distance_to_in_meters_three_place(self):
        coord1 = Coord(52.0673599, 5.1102121)
        coord4 = Coord(52.0309339, 5.1385769)

        self.assertEqual(4490.877, coord1.distance_to_in_meters(coord4))
        self.assertEqual(4.491, coord1.distance_to_in_kilometers(coord4))


if __name__ == '__main__':
    unittest.main()
