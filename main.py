import datetime

from user import User
from plan import basic_plan, standar_plan, premium_plan


shandy = User("Shandy", basic_plan, datetime.date(2022,6,19))
shandy.current_plan.check_plan()