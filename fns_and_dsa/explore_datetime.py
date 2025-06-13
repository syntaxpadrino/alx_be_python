from datetime import datetime, timedelta
def display_current_datetime():
    """
    Display the current date and time in a formatted string.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return formatted_date

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {days_to_add} days: {formatted_future_date}")
    return future_date

def main():
    current_date = display_current_datetime()
    days_to_add = int(input("Enter the number of days to add to the current date:"))
    future_date = calculate_future_date(current_date, days_to_add)
    print(f"Future date after adding {days_to_add} days: {future_date.strftime('%Y-%m-%d')}")
if __name__ == "__main__":
    main()