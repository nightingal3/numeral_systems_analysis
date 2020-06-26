def convert_to_minutes(num_hours: int) -> int:
    minutes = num_hours * 60
    return minutes

def convert_to_seconds(num_hours: int) -> int:
    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds

seconds = convert_to_seconds(2)
seconds = convert_to_seconds(3)
print(seconds)