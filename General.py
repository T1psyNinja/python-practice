class Enlistee:
    def __init__(self, enlistee_name, enlistee_number):
        self.__enlistee_name = enlistee_name
        self.__enlistee_number = enlistee_number
        
    def set_enlistee_name(self, enlistee_name):
        self.__enlistee_name = enlistee_name
        
    def set_enlistee_number(self, enlistee_number):
        self.__enlistee_number = enlistee_number
        
    def get_enlistee_name(self):
        return self.__enlistee_name
        
    def get_enlistee_number(self):
        return self.__enlistee_number

class General(Enlistee):
    def __init__(self, enlistee_name, enlistee_number, annual_salary, annual_bonus):
        super().__init__(enlistee_name, enlistee_number)
        self.__annual_salary = annual_salary 
        self.__annual_bonus = annual_bonus 

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary
    def get_annual_bonus(self):
        return self.__annual_bonus

def main():
    print("Provide the following")
    enlistee_name = input("Enter enlistee name: ")
    enlistee_number = int(input("Enter enlistee number: "))

    print("General Pay")
    annual_salary = int(input("What is your annual salary "))
    annual_bonus = int(input("What is your annual bonus "))

    print("General Information")
    current_general = General(
        enlistee_name,
        enlistee_number,
        annual_salary,
        annual_bonus
    )
    print("Enlistee Name:", current_general.get_enlistee_name())
    print("Enlistee Number:", current_general.get_enlistee_number())
    print("Annual Salary:", current_general.get_annual_salary())
    print("Annual Bonus:", current_general.get_annual_bonus())
main()
    
