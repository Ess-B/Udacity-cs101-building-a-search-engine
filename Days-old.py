# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
   
  days_of_months = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31,30, 31]
  days = 0
  
  def is_leap(year):
    if year % 4 != 0:
      return "is_not"
    elif year % 100 != 0:
      return "is_leap"
    elif year % 400 != 0:
      return "is_not"
    else:
      return "is_leap"
    
  year = year1 + 1
  while year < year2:
    a = 1

    if is_leap(year) == "is_leap":
      days_in_year = 366
    else:
      days_in_year = 365

    year = year + a
    days = days_in_year + days #days between years

  a = 0
  m = 0

  if year2 > year1:
    while m < 11:
      m = month1 + a
      a = a + 1

      if m == 1 :
        if is_leap(year1) == "is_leap":
          days_of_months[1] = 29
        else:
          days_of_months[1] = 28
              
      days_in_month = days_of_months[m]
      days = days_in_month + days #days in year 1 minus month1
  
    m = 0
    a = 1
    while m < month2 - 1:
      
      #a = a + 1

      if m == 1 :
        if is_leap(year2) == "is_leap":
          days_of_months[1] = 29
        else:
          days_of_months[1] = 28

      days_in_month = days_of_months[m]
      m = m + a

      days = days_in_month + days #days in year2 minus month 2
  
  else: #year 1 = year2
    m = month1
    a = 1

    #days between months(same year) minus days in months 1 and 2
    while m < month2 - 1: 
      
      if m == 1 :
        if is_leap(year2) == "is_leap":
          days_of_months[1] = 29
        else:
          days_of_months[1] = 28

      days_after_month1 = days_of_months[m]
      m = m + a
      days = days_after_month1 + days  
  
  days_in_month1 = days_of_months[month1-1] - day1 #days in month1
  days_in_month2 = day2  #days in month2

  days = days + days_in_month1 + days_in_month2

  return days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

