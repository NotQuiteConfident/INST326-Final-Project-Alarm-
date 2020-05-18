# Import modules
import datetime
import time

# Get desired day
def dateEntry():
    inDay = str(raw_input("Enter the desired date for alarm (mm/dd/yyyy): ")).split("/")

    try:
        inDay = [int(x) for x in inDay]
        valid = True
    except ValueError:
        valid = False

    while not valid or len(inDay) != 3:

        print("Date is not in correct format.")

        inDay = str(raw_input("Enter the desired date for alarm (mm/dd/yyyy): ")).split("/")

        try:
            inDay = [int(x) for x in inDay]
            valid = True
        except ValueError:
            valid = False

    return inDay

# Get desired time
def timeEntry():
    inTime = str(raw_input("Enter the desired time for alarm (hh:mm:ss): ")).split(":")

    try:
        inTime = [int(x) for x in inTime]
        valid = True
    except ValueError:
        valid = False

    while not valid or len(inTime) != 3:

        print("Date is not in correct format.")

        inTime = str(raw_input("Enter the desired time for alarm (hh:mm:ss): ")).split(":")

        try:
            inTime = [int(x) for x in inTime]
            valid = True
        except ValueError:
            valid = False

    return inTime

inDate = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)

# Get current time and date
nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)

# Date and time entry
finalDay = dateEntry()
finalTime = timeEntry()

inDate = inDate.replace(year=finalDay[2])
inDate = inDate.replace(month=finalDay[0])
inDate = inDate.replace(day=finalDay[1])
inDate = inDate.replace(hour=finalTime[0])
inDate = inDate.replace(minute=finalTime[1])
inDate = inDate.replace(second=finalTime[2])

# Check for valid date and time
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

# Remove microseconds from current time
nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)

# Check date and time
while nowDate != inDate:

    nowDate = datetime.datetime.now()
    nowDate = nowDate.replace(microsecond=0)
    print("Time: " + str(nowDate))
    print("Alarm: " + str(inDate))
    time.sleep(1)

print("-----------------------")
print("Alarm Reached")
print("-----------------------")
