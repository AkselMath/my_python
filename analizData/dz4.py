from datetime import datetime, timedelta
import pandas as pd
import time

# date_string = 'May 9 2017 9:00AM'
# date_datetime = datetime.strptime(date_string, '%b %d %Y %H:%M%p')
# print(date_datetime)
#
# date_datetime += timedelta(hours=1)
# print(date_datetime)
#
# print(date_datetime.strftime( '%Y-%m-%d'))
#

# startDate = '2017-01-01 00:00:00'
# endDate = '2017-01-07 23:59:59'
#
# startDate_datetime = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S')
# endDate_datetime = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')
# current_day = startDate_datetime
#
# while current_day < endDate_datetime:
#     current_day += timedelta(hours=1)
#
# current_day -= timedelta(hours=1)
# print(current_day.strftime('%Y-%m-%d %H:%M:%S'))



def date_range(start_date, end_date):
    date_range_list = []
    current_date = start_date
    current_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')

    while current_date_dt <= end_date_dt:
        date_range_list.append(current_date)
        current_date_dt += timedelta(days=1)
        current_date = current_date_dt.strftime('%Y-%m-%d')
    return date_range_list

def convert_to_datetime(row):
    return datetime.strptime(row['date'], '%d.%m.%Y %H:%M')


def make_unix_time(row):
    return time.mktime(row['datetime'].timetuple())

data = pd.read_csv('https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data.tsv', sep='\t')
data['datetime'] = data.apply(convert_to_datetime, axis=1)
data['unixtime'] = data.apply(make_unix_time, axis=1)
user_id = data["user_id"].value_counts()
a = []
for i in range(len(user_id.index)):
    if (data[data.user_id == user_id.index[i]].unixtime.max() - data[data.user_id == user_id.index[i]].unixtime.min()) > 0:
        ka = data[data.user_id == user_id.index[i]].unixtime.max() - data[data.user_id == user_id.index[i]].unixtime.min()
        a.append(ka)

print(round(sum(a)/len(a)/60/24,1))