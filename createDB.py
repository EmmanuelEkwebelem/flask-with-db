import sqlite3

connect = sqlite3.connect('patients')

db = connect.cursor()

db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

table = """ CREATE TABLE patient_table (
            ID VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            gender CHAR(25) NOT NULL,
            risk CHAR(25) NOT NULL,
            LOS CHAR(25) NOT NULL,
            insurance CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() 

db.execute("INSERT INTO patient_table(ID, firstname, lastname, dob, gender, risk, LOS, insurance) values('123456789', 'Matthew', 'Crean', '01/01/2000', 'male', 'high', '12', 'Private')")
db.execute("INSERT INTO patient_table(ID, firstname, lastname, dob, gender, risk, LOS, insurance) values('113652748', 'Ruth', 'Beth', '02/02/2001', 'female', 'medium', '38', 'Medicaid')")
db.execute("INSERT INTO patient_table(ID, firstname, lastname, dob, gender, risk, LOS, insurance) values('854289652', 'Luke', 'Skywalker', '03/03/2002', 'male', 'low', '89', 'Medicare')")
db.execute("INSERT INTO patient_table(ID, firstname, lastname, dob, gender, risk, LOS, insurance) values('963845628', 'John', 'Williams', '04/04/2003', 'male', 'severe', '241', 'None')")
db.execute("INSERT INTO patient_table(ID, firstname, lastname, dob, gender, risk, LOS, insurance) values('193027364', 'Janee', 'Baker', '05/05/2004', 'female', 'notapplicable', '2', 'Private')")

connect.commit()
connect.close()