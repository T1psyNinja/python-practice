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


class Private(Enlistee):
    def __init__(self, enlistee_name, enlistee_number, plantoon_number, years_of_service):
        super().__init__(enlistee_name, enlistee_number)
        self.__platoon_number = plantoon_number
        self.__years_of_service = years_of_service

    def set_platoon_number(self, platoon_number):
        self.__platoon_number = platoon_number

    def set_years_of_service(self, years_of_service):
        self.__years_of_service = years_of_service  
    
    def get_platoon_number(self):
        return self.__platoon_number

    def get_years_of_service(self):
        return self.__years_of_service



def main():
    print("Provide the following")
    enlistee_name = input("Enter enlistee name: ")
    enlistee_number = int(input("Enter enlistee number: "))
    platoon_number = int(input("Enter platoon number: "))
    years_of_service = int(input("Enter years of service: "))

    print("Enlisted Information")
    current_private = Private(
        enlistee_name,
        enlistee_number,
        platoon_number,
        years_of_service
    )
    print("Enlistee Name:", current_private.get_enlistee_name())
    print("Enlistee Number:", current_private.get_enlistee_number())
    print("Platoon Number:", current_private.get_platoon_number())
    print("Years of Service:", current_private.get_years_of_service())

main()
