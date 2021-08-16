# Database Lab Report 2 Question #3

import random

courses = [["1012","Discrete Math"], ["1013","Logic"], ["1014","Calculus"], ["1015","Java"], ["1016","Python"]]

departments = [["4456","SITE"], ["4457","SECE"], ["4458","SCEE"], ["4459","SBME"], ["4460","SMIE"], ["4461","ABCD"],
               ["4462","EFGH"], ["4463","HIJK"], ["4464","LMNO"], ["4465","PQRS"], ["4466","TUVW"], ["4467","XYZZ"],
               ["4467","AABB"], ["4468","BBCC"], ["4469","BBCC"]]

names = ["Jamauri","Asha","Kit","Briel","Joell","Lucio","Domingo","Finnick","Elder","Alaina","Bryceson","Isabela",
         "Allanah","Raylynn","Braelyn","Tamiyah","Gema","Rachel","Cypress","Olympia","Genevie","Christan","Austyn",
         "Eryn","Coralie","Hanson","Reet","Wylder","Mikaella","Amariah","Freeman","Jakiya","Namir","Maryan","Estefania",
         "Trevor","Kinzley","Evey","Mark","Kepler","Jazariah","Hesston","Richie","Ayesha","Moussa","Lizbeth","Braelyn",
         "Caelyn","Aubrielle","Jemma","Varun","Dia","Oaklie","Khaliyah","Emmelia","Tommie","Ivette","Jayliana","Tiberius",
         "Marlon","Celina","Howard","Price","Tycen","Auriel","Ameen","Karmin","Akari","Faiga","Rayna","Mariajose","Heidy",
         "Karl","Roxana","Esha","Shaina","Benyamin","Emitt","Gordon","Maylynn","Kree","Chyanne","Klay","Cori","Brandon",
         "Adan","Marielle","Cavan","Keisy","Donavon","Dottie","Akira","Guillermo","Aashna","Daila","Ayonna","Ritchie",
         "Alister","Arianny","Blakelynn","Alaura","Brynna","Journey","Kadyn","Reyes","Aranza","Collier","Yeshua","Ari",
         "Keondre","Jaymee","Pyper","Alaysia","Jamar","Gautham","Leena","Karley","Sebastien","Kiya","Daquan","Ameliah",
         "Aysha","Alvaro","Ananya","Saw","Jaden","Dwayne","Kimi","Erin","Yassine","Audie","Fox","Hiram","Aviana","Ethaniel",
         "Layna","Cassius","Lesly","Mariela","Ayrton","Malachai","Krystina","Amarion","Halen","Karter","Kennady","Jaxton",
         "Paizlee","Lillyana","Zenaida","Avni","Khaleel","Ford","Kanye","Jaliyah","Milan","Acelyn","Kavin","Wyatt","Jamilah",
         "Madden","Aalia","Ricki","Bashir","Uriah","Kylar","Harley","Kree","Annistyn","Frieda","Keylin","Finnley","Casen",
         "Carli","Clifton","Noella","Khai","Simeon","Shreyan","Brantley","Shyanne","Gian","Arhaan","Alannah","Isha","Alizay",
         "Corinna","Sofiya","Chantal","Irma","Naveah","Conor","Arial","Macoy","Jovani","Elexis","Nila","Hareem","Saleh",
         "Caison"]

def NAME():
    index = random.randint(0, len(names)-1)
    return names.pop(index)

def ID(first):
    return first+i

def CGPA():
    cgpa = "3."
    for c in range(2):
        digit = random.randint(0, 9)
        cgpa += str(digit)
    return cgpa

def AGE(a,b):
    return random.randint(a, b)

def COURSE(x):
    if x==1:
        return courses[i % 5][1]
    elif x==0:
        return courses[i % 5][0]

def EMAIL(name):
    return name[-1::-1] + '@gmail.com'

def DPT(x, rand):
    if rand==False:
        if x==1:
            return departments[i][1]
        elif x==0:
            return departments[i][0]
    else:
        if x==1:
            return departments[random.randint(0, 4)][1]
        elif x==0:
            return departments[random.randint(0, 4)][0]

def PHONE():
    phone = "+2519"
    for j in range(8):
        phone += str(random.randint(0, 9))
    return phone

def PRODUCT():
    name = 'Product '
    letter = chr(i + 65)
    name += letter
    return name

def TIME():
    time = ""
    hour = str(random.randint(0, 24))
    if len(hour) == 1:
        time += "0" + hour + ":"
    else:
        time += hour + ":"
    minute = str(random.randint(0, 60))
    if len(minute) == 1:
        time += "0" + minute
    else:
        time += minute
    return time

def WRITE(sql):
    f.write(sql)
    f.write("\n")

def USE(num):
    use = "USE Labex_"
    use+=str(num)+";"
    f.write(use)
    f.write("\n")

with open('sql.txt', 'w+') as f:

    USE(1)

    for i in range(15):
        sql = "INSERT INTO Student(Name, ID, CGPA, Age) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(1209)
        sql += 'UGR/' + str(id) + '/12\', '

        cgpa = CGPA()
        sql += cgpa + ', '

        age = AGE(19,23)
        sql += str(age) + ');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Faculty(Name, ID, Course_Code, Email) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(2207)
        sql += 'FAC/' + str(id) + '\', \''

        course_code = COURSE(0)
        sql += "C-" + course_code + '\', \''

        email = EMAIL(name)
        sql += email+'\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Course(Name, ID, Course_Code, Course_Title) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(3357)
        sql += 'FAC/' + str(id) + '\', \''

        course_code = COURSE(0)
        sql += "C-" + course_code + '\', \''

        course = COURSE(1)
        sql += course + '\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Department(Name, ID) VALUES ('"

        dpt = DPT(1,False)
        sql += dpt + '\', \''

        dpt = DPT(0,False)
        sql += 'DPT/' + dpt + '\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Chair(Name, ID, Chair_of, Email) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(4082)
        sql += 'CHR/' + str(id) + '\', \''

        dpt = DPT(1,True)
        sql += dpt + '\', \''

        email = EMAIL(name)
        sql += email+'\');'

        WRITE(sql)

    USE(2)

    for i in range(15):
        sql = "INSERT INTO Employee(Name, ID, Department, Age) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(5526)
        sql += 'EMP/' + str(id) + '\', \''

        dpt = DPT(1,True)
        sql += dpt + '\', '

        age = AGE(26,59)
        sql += str(age) + ');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO HR(Name, ID, Department, Email) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(6009)
        sql += 'HR/' + str(id) + '\', \''

        dpt = DPT(1,True)
        sql += dpt + '\', '

        email = EMAIL(name)
        sql += email+'\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Customer(Name, ID, Phone_Number) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(7446)
        sql += 'CST/' + str(id) + '\', \''

        phone = PHONE()
        sql += phone + '\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Board(Name, ID, Phone_Number) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(8132)
        sql += 'BRD/' + str(id) + '\', \''

        phone = PHONE()
        sql += phone + '\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Management(Name, ID, Department, Email) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(9293)
        sql += 'MNG/' + str(id) + '\', \''

        dpt = DPT(1,True)
        sql += dpt + '\', '

        email = EMAIL(name)
        sql += email+'\');'

        WRITE(sql)

    USE(3)

    for i in range(15):
        sql = "INSERT INTO Product(Product_Name, Product_ID, Shipper_ID, Deliver_ID) VALUES ('"

        name = PRODUCT()
        sql += name + '\', \''

        id = ID(1944)
        sql += 'PRD/' + str(id) + '\', \''

        id = ID(2233)
        sql += 'SHI/' + str(id) + '\', \''

        id = ID(3765)
        sql += 'DLV/' + str(id) + '\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Customer(Name, ID, Phone_Number) VALUES ('"

        name = NAME()
        sql += name + '\', \''

        id = ID(7461)
        sql += 'CST/' + str(id) + '\', \''

        phone = PHONE()
        sql += phone + '\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Shipper(Shipper_ID, Product_Name) VALUES ('"

        id = ID(2233)
        sql += 'SHI/' + str(id) + '\', \''

        name = PRODUCT()
        sql += name + '\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Deliver(Deliver_ID, Name, Deliver_time) VALUES ('"

        id = ID(3765)
        sql += 'DLV/' + str(id) + '\', \''

        name = NAME()
        sql += name + '\', \''

        time = TIME()
        sql += time + '\');'

        WRITE(sql)

    for i in range(15):
        sql = "INSERT INTO Admin(Admin_ID, Admin_Name, Email) VALUES ('"

        id = ID(5379)
        sql += 'DLV/' + str(id) + '\', \''

        name = NAME()
        sql += name + '\', \''

        email = EMAIL(name)
        sql += email+'\');'

        WRITE(sql)
