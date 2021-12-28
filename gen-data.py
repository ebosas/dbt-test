from mimesis import Person
from mimesis import Address
from mimesis.enums import Gender
from mimesis import Datetime
person = Person('en')
import pandas as pd
import random
person = Person()
addess = Address()
datetime = Datetime()

def create_rows_mimesis(num=1):
    output = [{"name":person.full_name(gender=Gender.FEMALE),
                "address":addess.address(),
                "name":person.name(),
                "email":person.email(),
                #"bs":person.bs(),
                "city":addess.city(),
                "state":addess.state(),
                "date_time":datetime.datetime(),
                #"paragraph":person.paragraph(),
                #"Conrad":person.catch_phrase(),
                "randomdata":random.randint(1000,2000)} for x in range(num)]
    return output

df_mimesis = pd.DataFrame(create_rows_mimesis(5000))
print(df_mimesis)