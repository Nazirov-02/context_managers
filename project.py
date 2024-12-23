from context_managers import DatabaseConnect

data_base = {
    'host': 'localhost',
    'database': 'month_5',
    'user': 'postgres',
    'password': 'KA1275147',
    'port': 5432
}


class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def save(self):
        with DatabaseConnect(**data_base) as conn:
            with conn.cursor() as cur:
                insert_person_query = '''insert into person(full_name,age)
                values (%s,%s);
                '''
                data = (self.full_name, self.age)

                cur.execute(insert_person_query, data)
                conn.commit()
                print('Person successfully saved')
    @staticmethod
    def get_all():
         with DatabaseConnect(**data_base) as conn:
             with conn.cursor() as cur:
                 cur.execute("""select * from person;""")
                 for i in cur.fetchall():
                     print(i)
                 print('get all function successfully worked')
    @staticmethod
    def get_one(person_id):
       with DatabaseConnect(**data_base) as conn:
           with conn.cursor() as cur:
               query = """select * from person
                              where id = %s;"""
               data = (person_id,)
               cur.execute(query,data)
               print(cur.fetchone())
               print('get one function successfully worked')




# data = Person('sherali olimov', 25)
# data2 = Person('Ali aliyev',20)
# data3 = Person('Vali valiyev',27)
# data.save()
# data2.save()
# data3.save()
# data.get_all()
# data.get_one(1)
