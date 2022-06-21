import database as db

class maneMoney:
    def __init__(self, goal, goalName, startCapital, startDate):
        db.createTables()
        self.GOAL = goal
        self.GOALNAME = goalName
        self.startCapital = startCapital
        self.startDate = startDate
        self.envelope = {self.startDate: self.startCapital}

    def getGoal(self):
        return self.GOAL

    def summarizeSavedCapital(self):
        return round(sum(self.envelope.values()), 2)

    def putMoneyInEnvelope(self, date, amount):
        self.envelope.update({date: amount})

    def removeMoneyFromEnvelope(self, date):
        self.envelope.pop(date)

    def printAbsSavedMoney(self):
        print("Bisher angesparter Betrag: "+str(self.summarizeSavedCapital()))
        print("Noch anzusparender Betrag: "+str(self.GOAL - self.summarizeSavedCapital()))

    def printRelativeSavedMoney(self):
        relOpenCapital = 100*(1 - self.summarizeSavedCapital()/self.GOAL)
        relSavedCapital = 100*(self.summarizeSavedCapital()/self.GOAL)
        print("Angesparter Betrag in Prozent: "+str(round(relSavedCapital))+" %")
        print("Noch anzusparender Betrag: "+str(round(relOpenCapital))+" %")

taigoFund = maneMoney(10000.00, "Taigo", 170.00, "13.06.22")
db.importGoalIntoDB(taigoFund.GOALNAME, taigoFund.GOAL)
db.getDataFromDB()
