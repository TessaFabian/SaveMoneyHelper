import sqlite3


def createMoneyTable():
    connection = sqlite3.connect("money.db")
    cursor = connection.cursor()
    createMoneyTable = """
    CREATE TABLE money (
    id INTEGER PRIMARY KEY,
    date DATE,
    amount DOUBLE,
    goal CHAR(30)
    );
    """
    cursor.execute(createMoneyTable)
    connection.commit()
    connection.close()

def createGoalsTable():
    connection = sqlite3.connect("money.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE goals (
    id INTEGER PRIMARY KEY,
    goalName CHAR(30),
    goalSum DOUBLE
    )
    """)
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
