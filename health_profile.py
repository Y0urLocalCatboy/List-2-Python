class HealthProfile:
    Healthy_BMI = (18.5, 24.9)
    def __init__(self, first_name, dob, height, weight):
        self.first_name = first_name
        self.dob = dob # Year of birth
        self.height = height
        self.weight = weight
    def get_age(self):
        return 2024 - self.dob
    def get_bmi(self):
        return self.weight / (self.height * self.height) * 10000
    @staticmethod
    def calculate_age_stats(profiles):
        ages = [profile.get_age() for profile in profiles]
        mean_age = sum(ages)/len(profiles)
        standard_dev = (sum((age - mean_age) ** 2 for age in ages) / len(ages)) ** 0.5
        return mean_age, standard_dev
    @staticmethod
    def find_people_at_risk(profiles):
        return [profile for profile in profiles if profile.get_bmi() >= 24.9 or profile.get_bmi() <= 18.5]
    