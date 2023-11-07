import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta

a = input("Dogum gununuzu bu sekilde (GG.AA.IIII) daxil edin: ")

def Birthday(a):
  b = datetime.strptime(a,"%d.%m.%Y")
  c= b.year
  d = b.month
  age= datetime.now().year -c
  difference = datetime.now() - b
  month = (age * 12)+(datetime.now().month - d)
  days = difference.days
  hours= days * 24
  minutes= hours * 60
  seconds = minutes * 60
  return print(f"Siz heyatda {seconds} saniye {minutes} deqiqe {hours} saat {days} gun {month} aydir ki movcudsunuz ve sizin {age} yashiniz var")


Birthday(a)
