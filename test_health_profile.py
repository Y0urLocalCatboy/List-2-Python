import unittest
from health_profile import HealthProfile


class TestHealthProfile(unittest.TestCase):
    """
    Unit test class for testing the HealthProfile class.
    Methods:
        setUp(): Initializes test instances of HealthProfile.
        test_get_age(): Tests age calculation.
        test_get_bmi(): Tests BMI calculation with 2 decimal precision.
        test_calculate_age_stats(): Tests calculation of mean and standard deviation of ages.
        test_find_people_at_risk(): Tests identification of people at risk based on BMI thresholds.
    """

    def setUp(self):
        """
        Sets up HealthProfile instances for testing.

        Instances:
            profile1: John, 180 cm, 75 kg, born in 1990.
            profile2: Alice, 160 cm, 60 kg, born in 1985.
            profile3: Bob, 170 cm, 80 kg, born in 2000.
            profiles: List of all test profiles.
        """
        self.profile1 = HealthProfile("John", 1990, 180, 75)
        self.profile2 = HealthProfile("Alice", 1985, 160, 60)
        self.profile3 = HealthProfile("Bob", 2000, 170, 80)
        self.profiles = [self.profile1, self.profile2, self.profile3]

    def test_get_age(self):
        """
        Tests the get_age() method to verify age calculation based on birth year.

        Asserts:
            Correct ages for each profile based on the year 2024.
        """
        self.assertEqual(self.profile1.get_age(), 34)
        self.assertEqual(self.profile2.get_age(), 39)
        self.assertEqual(self.profile3.get_age(), 24)

    def test_get_bmi(self):
        """
        Tests the get_bmi() method for BMI calculation with precision to two decimal places.

        Asserts:
            Calculated BMI for each profile matches expected BMI values.
        """
        self.assertAlmostEqual(self.profile1.get_bmi(), 23.15, places=2)
        self.assertAlmostEqual(self.profile2.get_bmi(), 23.44, places=2)
        self.assertAlmostEqual(self.profile3.get_bmi(), 27.68, places=2)

    def test_calculate_age_stats(self):
        """
        Tests the calculate_age_stats() method to ensure accurate mean age
        and standard deviation calculation for a set of profiles.

        Asserts:
            Mean age and standard deviation are accurate to two decimal places.
        """
        mean_age, std_dev = HealthProfile.calculate_age_stats(self.profiles)
        self.assertAlmostEqual(mean_age, 32.33, places=2)
        self.assertAlmostEqual(std_dev, 6.24, places=2)

    def test_find_people_at_risk(self):
        """
        Tests the find_people_at_risk() method to correctly identify individuals
        outside the healthy BMI range (18.5-24.9).

        Asserts:
            Individuals with BMI outside the healthy range are included in the result.
        """
        people_at_risk = HealthProfile.find_people_at_risk(self.profiles)
        self.assertIn(self.profile3, people_at_risk)
        self.assertNotIn(self.profile1, people_at_risk)
        self.assertNotIn(self.profile2, people_at_risk)


if __name__ == '__main__':
    unittest.main()
