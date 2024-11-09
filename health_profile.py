class HealthProfile:
    """
    A class representing a health profile with attributes and methods for calculating age,
    BMI, and assessing health risk based on BMI.

    Attributes:
        Healthy_BMI (tuple): A tuple representing the healthy BMI range (18.5, 24.9).

    Methods:
        get_age(): Calculates and returns age based on the year of birth.
        get_bmi(): Calculates and returns BMI.
        calculate_age_stats(profiles): Calculates the mean age and standard deviation
            for a list of HealthProfile instances.
        find_people_at_risk(profiles): Identifies and returns profiles that are at risk
            due to BMI outside the healthy range.
    """
    Healthy_BMI = (18.5, 24.9)

    def __init__(self, first_name, dob, height, weight):
        """
        Initializes a HealthProfile instance with basic health details.

        Parameters:
            first_name (str): First name.
            dob (int): Year of birth.
            height (float): Height in centimeters.
            weight (float): Weight in kilograms.
        """
        self.first_name = first_name
        self.dob = dob  # Year of birth
        self.height = height
        self.weight = weight

    def get_age(self):
        """
        Calculates age based on the current year (2024) and year of birth.

        Returns:
            int: The calculated age.
        """
        return 2024 - self.dob

    def get_bmi(self):
        """
        Calculates Body Mass Index (BMI).

        Returns:
            float: The calculated BMI, based on weight (kg) / height (m^2).
        """
        return self.weight / (self.height * self.height) * 10000

    @staticmethod
    def calculate_age_stats(profiles):
        """
        Calculates the mean age and standard deviation of age for a list of HealthProfile instances.

        Parameters:
            profiles (list): A list of HealthProfile instances.

        Returns:
            tuple: A tuple containing the mean age and standard deviation of the ages in the list.
        """
        ages = [profile.get_age() for profile in profiles]
        mean_age = sum(ages) / len(profiles)
        standard_dev = (sum((age - mean_age) ** 2 for age in ages) / len(ages)) ** 0.5
        return mean_age, standard_dev

    @staticmethod
    def find_people_at_risk(profiles):
        """
        Identifies profiles with BMI outside the healthy range.

        Parameters:
            profiles (list): A list of HealthProfile instances.

        Returns:
            list: A list of HealthProfile instances where BMI is below 18.5 or above 24.9.
        """
        return [profile for profile in profiles if profile.get_bmi() >= 24.9 or profile.get_bmi() <= 18.5]
