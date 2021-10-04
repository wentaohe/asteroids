import json
import math, datetime, calendar
from .utils import feed, browse, lookup

def month_cloest_approaches(start_month):
    
    #get the year, month, and day data
    date = start_month.split('-')
    year = int(date[0])
    month = int(date[1])
    num_of_days = calendar.monthrange(year, month)[1]
    num_of_weeks = math.ceil(num_of_days/7)
    
    #creating week intervals
    week_intervals = []
    for week in range(0, num_of_weeks):
        start = week * 7 + 1
        end = start + 6
        if end > num_of_days:
            end = num_of_days
        #for dates/months with single digits, ie 01-01
        start_day = f'{start_month}-{str(start).zfill(2)}'
        end_day = f'{start_month}-{str(end).zfill(2)}'
        week_intervals.append([start_day, end_day])
    
    results = {'month': start_month, 'element_count': 0, 'near_earth_objects': {}}
    for week in week_intervals:
        data = feed(week[0], week[1])
        results['element_count'] += data['element_count']
        for key, value in data['near_earth_objects'].items():
            results['near_earth_objects'][key] = value
    return json.dumps(results)

