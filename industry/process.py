import json
import datetime
import dateutil.parser
import pyclowder
import pyclowder.datasets

clowder_url = 'https://pdg.clowderframework.org/'

user_api = 'b81d4590-cd89-416e-8ee4-d0dade8b0c95'

file_id = '6192cf36e4b0e1bb77ac6b7a'

client = pyclowder.datasets.ClowderClient(host=clowder_url, key=user_api)

def post_metadata_file():
    try:
        with open('61775e9cb84813122064b444.json', 'r') as f:
            md = json.load(f)

            result = client.post('/files/'+file_id+'/metadata', content=md, params=md)
            print(result)
    except Exception as e:
        print(e)

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


post_metadata_file()

total_file = get_entire_json_file('61775e9cb84813122064b444.json')

time_stamps = get_timespan_json_file('61775e9cb84813122064b444.json')


# create a datetime for the start of query
start_time_query = datetime.datetime(2021, 11, 3, 15, 45, 50)

# create a datetime for the end of query
end_time_query = datetime.datetime(2021, 11, 3, 15, 46)


## THIS gets the entries that are within the start and end time
entries = get_entries_within_timestamp(start_time_query, end_time_query, '61775e9cb84813122064b444.json')

earlier_date = datetime.datetime(2021, 11, 3, 0, 0, 0)

later_date = datetime.datetime(2021, 11, 3, 20, 0, 0)

# this check if the start or end times are BEFORE this particular json

is_earlier = is_start_before_json(path_to_json='61775e9cb84813122064b444.json', start=earlier_date)

is_later = is_end_after_json('61775e9cb84813122064b444.json', later_date)

print('done')