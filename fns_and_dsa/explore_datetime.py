import datetime


def display_current_datetime():
    # Format and print the current date and time in a readable format,
    # such as “YYYY-MM-DD HH:MM:SS”.

    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time: {current_date}"


print(display_current_datetime())

nb_days = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    # Print the future date in a format like “YYYY-MM-DD”.

    now = datetime.datetime.now()
    future_date = (now + datetime.timedelta(days=nb_days)).strftime("%Y-%m-%d")
    return f"Future date: {future_date}"


print(calculate_future_date())
