from datetime import datetime

class FoodDiary:

    def  __intit__(self):
        self._json = {}

    def _get_date(self):
        today = datetime.now()
        return "{}.{}.{}".format (today.day,today.month, today.year)

    def add_meal(self, meal):
        date = self._get_date
        if date in self._json:
            self._json[date].append(mean)
        else:
            self._json[date] = [meal]

        return "Ok. it is done"
        

    def list_meal(self,date):
        if date in self._json:
            return "\n".join(self._json[date])
        
        return "No meals for that day"
        

diary = FoodDiary()
diary.add_meal("pizza")
print(diary.list_meal("30.11.2015"))


class CLI:
    def  __init__(self):
        pass

    def create_hello_message(self):
        return "hello"

    def create_menu_message(self):
        return "help text"

    def start(self):
        print(self.create_hello_message)

        while True:
            console_input = input("Enter command: ")

            try:
                "meal pizza" 




