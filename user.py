from tabulate import tabulate
from dataclasses import dataclass
from dateutil.relativedelta import relativedelta
import random
import datetime

from plan import basic_plan, standar_plan, premium_plan

list_plan = [basic_plan, standar_plan, premium_plan]
class User:
    __secret_code = ('abcd', 'gh56', 'kmzw', '8awaa')
    __list_refcode_user = {}
    
       
    def __init__(self, username, choose_plan, register_date):
        self.username = username
        self.current_plan = choose_plan
        self.register_date = register_date
        self.bill = choose_plan.price
        
        self.referral_code = self.username + "-" + self.__secret_code[random.randint(0,len(self.__secret_code)-1)]
        self.__list_refcode_user[self.username] = self.referral_code
    def upgrade_plan(self, new_plan):
        if new_plan.price <= self.current_plan.price:
            print("Anda tidak bisa downgrade, pilih plan lebih tinggi")
            return
        
        difference_in_years = relativedelta(datetime.date.today(), self.register_date).years
        pay = 1
        if difference_in_years >=1:
            pay = 0.95
        
        self.bill = pay * new_plan.price
        self.current_plan = new_plan
        return self.bill
    
    def check_secret(self):
        print(self.__secret_code)
        
    def check_list(self):
        print(self.__list_refcode_user)
        
    def redeem_code(self, code):
        if code in self.__list_refcode_user.values():
            self.bill = 0.96 * self.current_plan.price
            return True, self.bill
        else:
            return False, "Code Referal tidak valid"
        #
    def check_all_plan(self):
        for plan in list_plan:
            plan.check_plan()