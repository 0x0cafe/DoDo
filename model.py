class Alogrithm:
    id = 0
    algorithm_name = ''
    algorithm_type = ''
    location = ''
    file_type=''
    description=''
    def __init__(self, id, algorithm_name, algorithm_type, file_type):
        self.id = id
        self.algorithm_name = algorithm_name
        self.algorithm_type = algorithm_type
        self.file_type = file_type
    def to_json(self):
        return {"id":self.id,
                "algorithm_name":self.algorithm_name,
                "algorithm_type":self.algorithm_type,
                "location":self.location,
                "file_type":self.file_type,
                "description":self.description}

def getAlogrithms():
    res = []
    import pymysql
    db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    cursor = db.cursor()
    sql = "SELECT * FROM EMPLOYEE \
           WHERE INCOME > %s" % (1000)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                  (fname, lname, age, sex, income))
    except:
        print("Error: unable to fetch data")

    db.close()
    a = Alogrithm(1, 'xxx')
    b = Alogrithm(2, 'yyy')
    return [a,b]