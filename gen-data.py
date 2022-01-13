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

# def create_rows_mimesis(num=1):
#     output = [{"name":person.full_name(gender=Gender.FEMALE),
#                "address":addess.address(),
#                "name":person.name(),
#                "email":person.email(),
#                #"bs":person.bs(),
#                "city":addess.city(),
#                "state":addess.state(),
#                "date_time":datetime.datetime(),
#                #"paragraph":person.paragraph(),
#                #"Conrad":person.catch_phrase(),
#                "randomdata":random.randint(1000,2000)} for x in range(num)]
#     return output

def gen_customers(num=1):
    output = [{"first_name":person.first_name(),
               "last_name":person.last_name()} for x in range(num)]
    return output

def gen_orders(num=1):
    status = ["returned", "completed", "return_pending", "shipped", "placed"]
    output = [{"user_id":random.randint(1,num),
               "order_date":datetime.date(start=2019, end=2020),
               "status":random.choice(status)} for x in range(num)]
    return output

def gen_payments(num=1):
    payment_method = ["credit_card", "coupon", "bank_transfer", "gift_card"]
    output = [{"order_id":random.randint(1,num),
               "payment_method":random.choice(payment_method),
               "amount":random.randint(1,50)*100} for x in range(num)]
    return output

df_customers = pd.DataFrame(gen_customers(15000))
df_customers = df_customers.rename_axis("id")
df_customers.index = df_customers.index + 1
df_customers.to_csv("data2/raw_customers.csv")
print(df_customers)

df_orders = pd.DataFrame(gen_orders(15000*2))
df_orders = df_orders.rename_axis("id")
df_orders.index = df_orders.index + 1
df_orders.to_csv("data2/raw_orders.csv")
print(df_orders)

df_payments = pd.DataFrame(gen_payments(15000*2))
df_payments = df_payments.rename_axis("id")
df_payments.index = df_payments.index + 1
df_payments.to_csv("data2/raw_payments.csv")
print(df_payments)
