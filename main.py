class worker:
    def __init__(self, wage, weekend, my_lunch):
        self.wage = wage
        self.weekend = weekend
        self.my_lunch = my_lunch

    def get_wage(self):
        return f'I get a wage in the size of {self.wage} dollars!'

    def brain_recharge(self):
        return f'I will rest for {self.weekend} days!'

programmer = worker(90000, 2, 'banana')
print(programmer.get_wage())

class Builder(worker):

    def __init__(self, wage, weekend, my_lunch, __special_form):
        super().__init__(wage, weekend, my_lunch)
        self.__special_form = "builder's form"
    def brain_recharge(self):
        return f'I will rest for {self.weekend} months!'
