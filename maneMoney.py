import database as db

class maneMoney:
    def __init__(self, goal, startCapital, startDate):
        db.createTables()
        self.GOAL = goal
        self.startCapital = startCapital
        self.startDate = startDate
        self.envelope = {self.startDate: self.startCapital}

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

taigoFund = maneMoney(10000.00, 170.00, "13.06.22")
print(taigoFund.GOAL)
print(taigoFund.startCapital)
print(taigoFund.startDate)
print(taigoFund.envelope)
taigoFund.putMoneyInEnvelope("14.05.23", 123.45)
print(taigoFund.summarizeSavedCapital())
taigoFund.printAbsSavedMoney()
taigoFund.printRelativeSavedMoney()
