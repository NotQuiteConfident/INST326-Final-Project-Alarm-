import datetime
import time


def dateEntry():
    inDay = input("Enter the desired date for alarm (mm/dd/yyyy): ").split("/")

    try:
        inDay = [int(x) for x in inDay]
        valid = True
    except ValueError:
        valid = False

    while not valid or len(inDay) != 3:

        print("Date is not in correct format.")

        inDay = input("Enter the desired date for alarm (mm/dd/yyyy): ").split("/")

        try:
            inDay = [int(x) for x in inDay]
            valid = True
        except ValueError:
            valid = False

    return inDay

def timeEntry():
    inTime = input("Enter the desired time for alarm (hh:mm:ss): ").split(":")

    try:
        inTime = [int(x) for x in inTime]
        valid = True
    except ValueError:
        valid = False

    while not valid or len(inTime) != 3:

        print("Date is not in correct format.")

        inTime = input("Enter the desired time for alarm (hh:mm:ss): ").split(":")

        try:
            inTime = [int(x) for x in inTime]
            valid = True
        except ValueError:
            valid = False

    return inTime

inDate = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)

nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)

finalDay = dateEntry()
finalTime = timeEntry()

inDate = inDate.replace(year=finalDay[2])
inDate = inDate.replace(month=finalDay[0])
inDate = inDate.replace(day=finalDay[1])
inDate = inDate.replace(hour=finalTime[0])
inDate = inDate.replace(minute=finalTime[1])
inDate = inDate.replace(second=finalTime[2])

while inDate < datetime.datetime.now():
    print("This time is before now, enter another time.")

    finalDay = dateEntry()
    finalTime = timeEntry()

    inDate = inDate.replace(year=finalDay[2])
    inDate = inDate.replace(month=finalDay[0])
    inDate = inDate.replace(day=finalDay[1])
    inDate = inDate.replace(hour=finalTime[0])
    inDate = inDate.replace(minute=finalTime[1])
    inDate = inDate.replace(second=finalTime[2])

nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)

while nowDate != inDate:

    nowDate = datetime.datetime.now()
    nowDate = nowDate.replace(microsecond=0)
    print("Time: " + str(nowDate))
    print("Alarm: " + str(inDate))
    time.sleep(1)

print("-----------------------")
print("Alarm Reached")
print("-----------------------")
