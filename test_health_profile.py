import unittest
from health_profile import HealthProfile

class TestHealthProfile(unittest.TestCase):

    def setUp(self):
        self.profile1 = HealthProfile("John", 1990, 180, 75)  # Waga w kg, wzrost w cm
        self.profile2 = HealthProfile("Alice", 1985, 160, 60)
        self.profile3 = HealthProfile("Bob", 2000, 170, 80)
        self.profiles = [self.profile1, self.profile2, self.profile3]

    def test_get_age(self):
        self.assertEqual(self.profile1.get_age(), 34)
        self.assertEqual(self.profile2.get_age(), 39)
        self.assertEqual(self.profile3.get_age(), 24)

    def test_get_bmi(self):
        self.assertAlmostEqual(self.profile1.get_bmi(), 23.15, places=2)
        self.assertAlmostEqual(self.profile2.get_bmi(), 23.44, places=2)
        self.assertAlmostEqual(self.profile3.get_bmi(), 27.68, places=2)

    def test_calculate_age_stats(self):
        mean_age, std_dev = HealthProfile.calculate_age_stats(self.profiles)
        self.assertAlmostEqual(mean_age, 32.33, places=2)
        self.assertAlmostEqual(std_dev, 6.24, places=2)

    def test_find_people_at_risk(self):
        people_at_risk = HealthProfile.find_people_at_risk(self.profiles)
        self.assertIn(self.profile3, people_at_risk)
        self.assertNotIn(self.profile1, people_at_risk)
        self.assertNotIn(self.profile2, people_at_risk)

if __name__ == '__main__':
    unittest.main()
