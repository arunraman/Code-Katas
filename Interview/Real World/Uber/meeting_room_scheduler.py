# Meeting:(name, start, end)   -- start / end are unix timestamps
# Room: (id) -- room ID: 1, 2, 3, 4, 5, ...
# input: collection of meetings
# output: mapping of meeting name -> room ID
# constarints: use as few rooms as possible
# example: (foo, 3, 4), (bar, 3.5, 4.5) => foo->1, bar->2 => 2
# example: (foo, 3, 4), (bar, 4, 5) => foo->1, bar->1 => 1
# example: (foo, 3, 4) = > 1, (bar, 3.5, 6) = > 2, (zoo, 5.5, 6) => 1, (bar, 5.5, 6)  => 2

# function getNextRoom() => 1,2,3,4,5,... # yield
from collections import defaultdict, OrderedDict
class meetingInterval(object):
    def __init__(self, meeting_name, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_name = meeting_name


class meetingroomScheduler(object):
    def __init__(self):
        self.meeting_room_number = 0

    def minimumMeetingRoom(self, intervals):
        starts, ends = [], []
        reusable_meeting_rooms = []
        start_time_interval_meeting_map = defaultdict(list)
        end_time_interval_meeting_map = defaultdict(list)
        meeting_room_map = OrderedDict()
        count_rooms = 0
        minimum_room = 0
        for i in intervals:
            starts.append(i.start_time)
            ends.append(i.end_time)
            start_time_interval_meeting_map[i.start_time].append(i.meeting_name)
            end_time_interval_meeting_map[i.end_time].append(i.meeting_name)
        starts.sort()
        ends.sort()
        i, j = 0, 0
        while i < len(starts):
            if starts[i] < ends[j]:
                if len(reusable_meeting_rooms) == 0:
                    meeting_room_map[start_time_interval_meeting_map[starts[i]].pop()] = self.getNextRoom()
                else:
                    meeting_room_map[start_time_interval_meeting_map[starts[i]].pop()] = reusable_meeting_rooms.pop(0)
                count_rooms += 1
                minimum_room = max(minimum_room, count_rooms)
                i += 1
            else:
                count_rooms -= 1
                reusable_meeting_rooms.append(meeting_room_map[end_time_interval_meeting_map[ends[j]].pop()])
                j += 1

        return meeting_room_map, minimum_room

    def getNextRoom(self):
        self.meeting_room_number += 1
        return self.meeting_room_number

M = meetingroomScheduler()
print M.minimumMeetingRoom([meetingInterval('foo', 3, 4),
                            meetingInterval('boo', 3.5, 6)])
M = meetingroomScheduler()
print M.minimumMeetingRoom([meetingInterval('foo', 3, 4),
                            meetingInterval('boo', 3.5, 6),
                            meetingInterval('goo', 5.5, 6),
                            meetingInterval('bar', 5.5, 6)])
M = meetingroomScheduler()
print M.minimumMeetingRoom([meetingInterval('foo', 3, 4),
                            meetingInterval('boo', 4, 5)])


