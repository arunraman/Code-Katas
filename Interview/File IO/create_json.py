import json


def createJson():
    data = {}
    topics_list = ['__consumer_offsets',
                   'change-stream',
                   'change-stream-gc-errors',
                    'container-hints',
                    'container-stats',
                    'health-check-topic',
                    'ome-publisher-gen1',
                    'purger-partitions',
                    'reaper-stream',
                    'reaper-stream-reaper-errors',
                    'telemetry']
    for topics in topics_list:
        data['versions'] = 1
        data['partitions'] = [
            {"topic":topics,"partition":0,"replicas":[0,1,2]},
            {"topic":topics,"partition":1,"replicas":[0,1,2]},
            {"topic":topics,"partition":2,"replicas":[0,1,2]},
            {"topic":topics,"partition":3,"replicas":[0,1,2]},
            {"topic":topics,"partition":4,"replicas":[0,1,2]},
            {"topic":topics,"partition":5,"replicas":[0,1,2]},
            {"topic":topics,"partition":6,"replicas":[0,1,2]},
            {"topic":topics,"partition":7,"replicas":[0,1,2]},
            {"topic":topics,"partition":8,"replicas":[0,1,2]},
            {"topic":topics,"partition":9,"replicas":[0,1,2]}
        ]
        jsonData = json.dumps(data, indent=4, skipkeys=True, sort_keys=True)
        print jsonData


createJson()
