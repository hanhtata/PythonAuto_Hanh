# 1
import time
import datetime
from datetime import datetime as dt
def day_diff(release_date, code_complete_day):
    date_format_1 = "%d/%m/%Y"
    date_format_2 = "%Y-%d-%m"
    d1 = dt.strptime(release_date, date_format_1)
    d2 = dt.strptime(code_complete_day, date_format_2)
    delta=abs(d1 - d2)
    return(delta.days)

# 2
import re
def alpha_num(sentence):
  result = []
  a = sentence.split()
  for i in a :
    if re.match("^\w*$",i) :
      if re.match("^[a-zA-Z]*$",i) or re.match("^\d*$",i) :
        pass
      else :
        result.append(i)
  return(result)