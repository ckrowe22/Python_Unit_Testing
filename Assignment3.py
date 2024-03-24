
class Employee:
    HRS_IN_YR = 2080

    # Cat = Full or Part Time
    def __init__(self, first, last, category, hourlySal):
        if not isinstance(first, str) or not isinstance(last, str) or not isinstance(category, str):
            raise TypeError("First name, last name, and category must be strings")
        self.first = first
        self.last = last
        self.category = category
        self.hourlySal = hourlySal

    def empyName(self):
        return '{} {} is a {}-time employee.'.format(self.first, self.last, self.category)

    def yearSalary(self):
        if self.hourlySal < 0:
            raise ValueError("Salary cannot be a negative number.")
        if self.category.lower() not in ['full', 'half']:
            raise ValueError("Please specify if employee is full or half time.")
        if self.category.lower() == "full":
            salary = Employee.HRS_IN_YR * self.hourlySal
        elif self.category.lower() == "half":
            salary = Employee.HRS_IN_YR/2 * self.hourlySal
        return salary