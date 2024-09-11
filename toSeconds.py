def getSecond(hour, minute, second):
    hour *= 3600
    minute *= 60
    return hour + minute + second
