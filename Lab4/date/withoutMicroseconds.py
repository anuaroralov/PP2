import datetime
date=datetime.datetime.now()
withoutMicroseconds=date.replace(microsecond=0)
print(withoutMicroseconds)
