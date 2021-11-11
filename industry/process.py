import json
import datetime
import dateutil.parser

def is_start_before_json(path_to_json, start):
    span = get_timespan_json_file(path_to_json)
    start_of_file = span[0]
    if start < start_of_file:
        return True
    else:
        return False

def is_end_after_json(path_to_json, end):
    span = get_timespan_json_file(path_to_json)
    end_of_file = span[1]
    if end > end_of_file:
        return True
    else:
        return False

def get_entire_json_file(path_to_json):
    with open(path_to_json) as f:
        entries = json.load(f)
    return entries

def get_timespan_json_file(path_to_json):
    with open(path_to_json) as f:
        entries = json.load(f)
        start_timestamp = entries[0]['timestamp']

        end_timestamp = entries[-1]['timestamp']
        print(start_timestamp)
        print(end_timestamp)
        start = dateutil.parser.isoparse(start_timestamp)
        end = dateutil.parser.isoparse(end_timestamp)
        return [start, end]

def get_entries_within_timestamp(start_time, end_time, path_to_json):
    results = []
    with open(path_to_json) as f:
        entries = json.load(f)
        for each in entries:
            timestamp = each['timestamp']
            dt = dateutil.parser.isoparse(timestamp)
            if dt >= start_time and dt <= end_time:
                results.append(each)
    return results

time_stamps = get_timespan_json_file('61775e9cb84813122064b444.json')

# 2021-11-03T15:45:44.419000

# create a datetime for the day at 3:15 AM
start_time_query = datetime.datetime(2021, 11, 3, 15, 45, 50)

# create a datetime for 30 seconds  later
end_time_query = datetime.datetime(2021, 11, 3, 15, 46)

total_file = get_entire_json_file('61775e9cb84813122064b444.json')

entries = get_entries_within_timestamp(start_time_query, end_time_query, '61775e9cb84813122064b444.json')

earlier_date = datetime.datetime(2021, 11, 3, 0, 0, 0)

later_date = datetime.datetime(2021, 11, 3, 20, 0, 0)

is_earlier = is_start_before_json('61775e9cb84813122064b444.json', earlier_date)

is_later = is_end_after_json('61775e9cb84813122064b444.json', later_date)

print('done')