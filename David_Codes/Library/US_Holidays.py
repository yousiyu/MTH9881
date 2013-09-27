"""
Synopsis: This class creates a list of the US holiday dates for
the following US holidays
    New Year Day
    Martin Luther King Jr. Day
    Presidents Day (Washingtons Birthday)
    Memorial Day
    Independence Day
    Labor Day
    Columbus Day
    Veterans Day
    Thanksgiving Day
    Christmas Day
    
Author: David Herssein
Created: September 30, 2013
Dependencies: dateutil
"""


from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *



def generate_holiday_dates(start_date, end_date):
    """
    Synopsis: This function creates a list of the US holiday dates for
    the following US holidays between the given start and end dates
        New Year Day
        Martin Luther King Jr. Day
        Presidents Day (Washingtons Birthday)
        Memorial Day
        Independence Day
        Labor Day
        Columbus Day
        Veterans Day
        Thanksgiving Day
        Christmas Day
        
    start_date, end_date = datetime(year,month, day)
    """

    #New Years (Jan 1)
    NewYears = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 1, byyearday = 1)

    #Martin Luthor King Jr. (Third Monday in January)
    MLKs = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 1, byweekday = MO(3))

    #Generate Presidents Day (Third Monday in February)
    PresidentsDays = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 2, byweekday = MO(3))

    #Memorial Day (Last Monday in May)
    MemorialDays = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 5, byweekday = MO(-1))

    #Independence Day (July 4)
    July4s = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 7, bymonthday = 4)

    #Labor Day (First Monday in September)
    LaborDays = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 9, byweekday = MO(1))

    #Columbus Day (Second Monday in October)
    ColumbusDays = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 10, byweekday = MO(2))

    #Veterans Day (November 11, or first Monday after November 11)
    TempVeteransDays = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 11, bymonthday = 11)
    VeteransDays = []
    for i in range(end_date.year - start_date.year + 1):
        if((TempVeteransDays[i]).weekday() == 5):
            VeteransDays.append(TempVeteransDays[i] + relativedelta(days=-1))
        elif((TempVeteransDays[i]).weekday() == 6):
            VeteransDays.append(TempVeteransDays[i] + relativedelta(days=+1))
        else:
            VeteransDays.append(TempVeteransDays[i])
    
    #Thanksgiving Day (Fourth Thursday of November)
    Thanksgivings = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 11, byweekday = TH(4))

    #Christmas Day (Dec 25)
    Christmas = rrule(freq = YEARLY, dtstart = start_date, until = end_date, bymonth = 12, bymonthday = 25)


    holidays = []

    for i in range(end_date.year - start_date.year + 1):
        holidays.append(NewYears[i])
        holidays.append(MLKs[i])
        holidays.append(PresidentsDays[i])
        holidays.append(MemorialDays[i])
        holidays.append(July4s[i])
        holidays.append(LaborDays[i])
        holidays.append(ColumbusDays[i])
        holidays.append(VeteransDays[i])
        holidays.append(Thanksgivings[i])
        holidays.append(Christmas[i])

    holidays.sort()
            
    return holidays