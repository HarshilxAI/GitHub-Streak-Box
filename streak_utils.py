from datetime import datetime, timedelta

def calculate_streaks(contributions):
    contributions = sorted([(datetime.strptime(date, "%Y-%m-%d"), count) for date, count in contributions])

    current_streak = 0
    longest_streak = 0
    temp_streak = 0
    temp_start = None
    longest_start = None    
    longest_end = None

    today = datetime.utcnow().date()
    streak_continues = True

    total_contributions = 0

    for i in range(len(contributions)-1, -1, -1):
        date, count = contributions[i]
        date = date.date()
        
        if count > 0:
            total_contributions += count
            if streak_continues:
                current_streak += 1

            if temp_streak == 0:
                temp_end = date
            temp_streak += 1
            temp_start = date

            if temp_streak >= longest_streak:
                longest_streak = temp_streak
                longest_start = temp_start
                longest_end = temp_end
        else:
            if date < today:
                streak_continues = False
            temp_streak = 0

    return {
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "longest_start": longest_start,
        "longest_end": longest_end,
        "total_contributions": total_contributions
    }
