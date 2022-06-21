import sqlite3


def createTables():
    connection = sqlite3.connect("money")
    cursor = connection.cursor()

    #Creates the table goals
    cursor.execute(
    """
    CREATE TABLE goals (
    goal CHAR(30) PRIMARY KEY,
    goalSum DOUBLE
    );
    """
    )

    #Creates the table money
    cursor.execute(
    """
    CREATE TABLE money(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sum DOUBLE NOT NULL,
    payingInDate String NOT NULL,
    payingOutDate String,
    goal CHAR(30) NOT NULL,
    FOREIGN KEY (goal) REFERENCES goals(goal)
    );
    """
    )

    #commit and close
    connection.commit()
    connection.close()



def importDataIntoDB(statement):
    connection = sqlite3.connect("money")
    cursor = connection.cursor()
    cursor.execute(statement)
    connection.commit()
    connection.close()

def importGoalIntoDB(goalName, goalSum):
    connection = sqlite3.connect("money")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO goals(goal, goalSum)
    VALUES('"""
    +goalName+
    """ ',"""
    +str(goalSum)+
    """);""")

    connection.commit()
    connection.close()

def deleteDataFromDB():
    pass

def getDataFromDB():
    connection = sqlite3.connect("money")
    cursor = connection.cursor()
    cursor.execute("""
    select * from goals;
    """)
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()
