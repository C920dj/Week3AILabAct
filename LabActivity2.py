def check_fast_lane(minutes_left, items, teacher_pass):
    
    if teacher_pass:
        return "Fast lane approved"
    elif minutes_left < 10 and items <= 3:
        return "Fast lane approved"
    else:
        return "Use regular line"


students_in_line = [
    {"name": "Marco", "minutes_left": 8, "items": 2, "teacher_pass": False},
    {"name": "Diane", "minutes_left": 15, "items": 1, "teacher_pass": False},
    {"name": "Kyle", "minutes_left": 5, "items": 6, "teacher_pass": False},
    {"name": "Ella", "minutes_left": 20, "items": 5, "teacher_pass": True},
]

fast_lane_count = 0

for student in students_in_line:
    result = check_fast_lane(student["minutes_left"], student["items"], student["teacher_pass"])
    print(f"{student['name']}: {result}")

    if result == "Fast lane approved":
        fast_lane_count += 1
    else:
        print(f"   -> {student['name']} has {student['minutes_left']} minutes left. Suggest using the regular line.")

print(f"\nTotal students approved for fast lane today: {fast_lane_count}")



# Why rule-based systems need override conditions:

# Basically, some rules should come first before the others, like a teacher's pass.
# If the program checks the normal rules first (time left and number of items),
# then someone like Ella could get rejected even if she already has a teacher's pass.
# Thats why the order is really important. The override rule should be checked first
# so it can allow the student before the other rules says no.
# Its kinda the same as the overdue books activity. The most important rule
# should always be checked first or the program might give the wrong result.

# What if two overrides conflict (teacher's pass vs. cafeteria closed)?

# This one is a little more confusing because now there are two special rules.
# I think if the cafeteria is closed, then nobody should be allowed to use the fast lane,
# even if they have a teacher's pass. It just makes more sense because the fast lane
# cant be used if its closed. So the program should check if the cafeteria is closed
# before checking the teacher's pass.