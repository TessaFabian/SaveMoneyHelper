from constant import GOAL


def init_dict(startingFund, emptyDict, startDate):
    emptyDict = {startDate: startingFund}
    return emptyDict

def getRemainingFromGoalAbs(envelope):
    return GOAL - getSumSavedMoney(envelope)

def getSumSavedMoney(envelope):
    return sum(envelope.values())

def addMoneyToEnvelope(date, value, envelope):
    envelope.update({date: value})

def removeMoneyFromEnvelope(date, value, envelope):
    envelope.pop(date)



print("#######Save Money#######")
print("Ziel: "+str(GOAL))
