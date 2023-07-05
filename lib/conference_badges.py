def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    msg_list = []
    for name in names:
        msg_list.append(badge_maker(name))
    return msg_list

def assign_rooms(names):
    room_list = []
    for i in range (len(names)):
        room_list.append(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
    return room_list

def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for message in badge_messages:
        print(message)

    for assignment in room_assignments:
        print(assignment)
    # return None
