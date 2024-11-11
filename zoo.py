# Lab 15
# Sukollapat Pisuchpen
# 6687052
# Sec 2
class Zoo:
    def get_ticket_price(self, age):
        if age < 0: # Path
            return "error, Please enter the correct age"
        elif age >= 0 and age <= 12:
            return 50
        elif age >= 13 and age <= 20:
            return 100
        elif age >= 21 and age <= 60:
            return 150
        else:
            return 100
