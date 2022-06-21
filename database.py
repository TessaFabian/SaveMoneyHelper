import sqlite3


def createTables():
    connection = sqlite3.connect("money.db")
    cursor = connection.cursor()
    cursor.execute(
    """
    CREATE TABLE goals (
    goal CHAR(30) PRIMARY KEY,
    goalSum DOUBLE
    );

    CREATE TABLE money (
    id INTEGER PRIMARY KEY,
    amount DOUBLE NOT NULL,
    payingIn DATE NOT NULL,
    payingOut DATE,
    goal CHAR(30) NOT NULL,
    FOREIGN KEY(goal) REFERENCES goals.goal
    );
    """
    )

    connection.commit()

    connection.close()



def importDataIntoDB():
    connection = sqlite3.connect("money.db")
    cursor = connection.cursor()
    connection.commit()
    connection.close()

def deleteDataFromDB():
    pass

def getDataFromDB(statement):
    connection = sqlite3.connect("money.db")
    cursor = connection.cursor()

    cursor.execute(statement)

    connection.commit()
    connection.close()
