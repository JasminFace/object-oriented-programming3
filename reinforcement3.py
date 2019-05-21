dict = { 'data': { 'rooms': 
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}

data = dict.get("data")
room201 = data.get("rooms")[0]
room201_capacity = room201.get("capacity") #50

def room201_events():
    events = data.get('events')
    for event in events:
        if event.get("room_id") == 1:
            return event

event = room201_events()
room201_attendees = event.get("attendees")
if room201_attendees <= room201_capacity:
    print("It's okay!")
else:
    print("It's NOT okay..")

