# STUDENT name: Toan Le
#   CSC 1301 – CRN 84165 Section 036
#   Python Lab 5
#   References: no one
#   No resources were used
#   Approximate time taken: 10 minutes

def main():
    # prompt user for the hour of the day that Road Runner needs to get out of bed.
    hours = int(input("HOURS:"))
    hours1 = hours
    # prompt user for the minute of the day that Road Runner needs to get out of bed
    minutes = int(input("MINUTES:"))
    minutes1 = minutes
    # prompt user for the minutes that Road Runner wants to stay in bed awake
    time_in_bed = int(input("TIME:"))

    # if time in bed is greater than minutes, subtract one from the hour then calculate for minutes left
    # calculate minutes by taking 60 and subtract it by time in bed, then add minutes
    if time_in_bed > minutes:
        hours -= 1
        minutes = 60 - time_in_bed + minutes

    # if minutes is greater or equals to time in bed, then subtract time in bed from minutes
    else:
        minutes = minutes - time_in_bed

    #print out alarm time with hours and minutes, format to have a leading zero
    print(f"ALARM TIME: {hours:02}:{minutes:02}")


main()
