def add_time(start, duration, day=None):
    """
    Adds a duration to a start time in 12-hour format.

    Parameters:
    start (str)    : start time, e.g., '11:43 PM'
    duration (str) : duration to add, e.g., '24:20'
    day (str, optional): starting day of the week, e.g., 'tuesday'

    Returns:
    str : new time in 12-hour format with optional day and days later info
    """

    # List of week days for calculating new day later
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # --- Step 1: Split start into time and period ---
    # Example: '11:43 PM' → start_time='11:43', period='PM'
    start_time, period = start.split()

    # --- Step 2: Split start_time into hours and minutes ---
    # Example: '11:43' → start_hour=11, start_minute=43
    start_hour, start_minute = map(int, start_time.split(':'))

    # --- Step 3: Split duration into hours and minutes ---
    # Example: '24:20' → dur_hour=24, dur_minute=20
    dur_hour, dur_minute = map(int, duration.split(':'))

    # --- Step 4: Convert start time to 24-hour format for easy calculation ---
    # PM times need +12 hours, except 12 PM is already 12
    if period.upper() == "PM":
        start_hour += 12
    if start_hour == 24:  # 12 PM stays 12
        start_hour = 12

    # --- Step 5: Add minutes and handle overflow to hours ---
    # Example: 43 + 20 = 63 → extra_hour = 1, final_minute = 3
    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    # --- Step 6: Add hours and count how many full days passed ---
    # Example: 23 + 24 + 1 = 48 → days_later = 2, final_hour_24 = 0
    total_hours = start_hour + dur_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # --- Step 7: Convert back to 12-hour format and determine AM/PM ---
    if final_hour_24 == 0:
        final_hour = 12
        final_period = "AM"
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = "AM"
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = final_hour_24 - 12
        final_period = "PM"

    # --- Step 8: Format minutes with leading zero ---
    final_minute_str = f"{final_minute:02d}"

    # --- Step 9: Calculate new day if starting day was given ---
    if day:
        # Normalize input day to match our list
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_str = f", {new_day}"  # Example: ", Thursday"
    else:
        day_str = ""

    # --- Step 10: Add next day / n days later info ---
    if days_later == 1:
        later_str = " (next day)"
    elif days_later > 1:
        later_str = f" ({days_later} days later)"
    else:
        later_str = ""

    # --- Step 11: Combine everything into final string ---
    result = f"{final_hour}:{final_minute_str} {final_period}{day_str}{later_str}"

    return result

if __name__=="__main__":
    # --- EXAMPLES OF USING THE FUNCTION ---

    # Example 1: simple addition without day
    print(add_time('3:00 PM', '3:10'))  
    # Output: 6:10 PM
    # Explanation: 3 PM + 3 hours 10 minutes → 6:10 PM same day

    # Example 2: with starting day
    print(add_time('11:30 AM', '2:32', 'Monday'))  
    # Output: 2:02 PM, Monday
    # Explanation: 11:30 AM + 2:32 → 14:02 → 2:02 PM, same day, Monday

    # Example 3: crosses midnight
    print(add_time('10:10 PM', '3:30'))  
    # Output: 1:40 AM (next day)
    # Explanation: 10:10 PM + 3:30 → 1:40 AM next day

    # Example 4: multiple days
    print(add_time('11:43 PM', '24:20', 'tueSday'))  
    # Output: 12:03 AM, Thursday (2 days later)
    # Explanation: 11:43 PM + 24:20 → 12:03 AM, 2 days later, Thursday
