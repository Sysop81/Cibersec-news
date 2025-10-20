import argparse
from datetime import datetime
import re

class Parameters:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Parameters handler")
        self.add_params()
        self.args = self.parser.parse_args()

    def add_params(self):
        self.parser.add_argument("--dateStart", help="Set the initial date to start the search. [dd/mm/yyyy]")

    def get_date(self):
        return datetime.strptime(self.args.dateStart, "%d/%m/%Y").date() if self.check_date() else datetime.now().date() #self.args.dateStart

    def validate_date(self):
        er = r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})"
        return bool(re.fullmatch(er, self.args.dateStart)) and not self.is_future_date()

    def is_future_date(self):
        param_date = datetime.strptime(self.args.dateStart, "%d/%m/%Y")
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        return param_date > today    

    def check_date(self):
        return self.args.dateStart is not None and self.validate_date()
            

