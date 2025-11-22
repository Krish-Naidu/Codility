from datetime import datetime


def calculate_age(dob_str):
    """
    Calculate age from date of birth in ddmmyyyy format.
    
    Args:
        dob_str (str): Date of birth in ddmmyyyy format (e.g., "15031990")
    
    Returns:
        tuple: (years, months, days) representing the age
    """
    # Validate input length
    if len(dob_str) != 8:
        raise ValueError("DOB must be in ddmmyyyy format (8 digits)")
    
    # Parse the date string
    try:
        day = int(dob_str[0:2])
        month = int(dob_str[2:4])
        year = int(dob_str[4:8])
        
        # Create datetime object for DOB
        dob = datetime(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    
    # Get current date
    today = datetime.now()
    
    # Check if DOB is in the future
    if dob > today:
        raise ValueError("Date of birth cannot be in the future")
    
    # Calculate age
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day
    
    # Adjust for negative days
    if days < 0:
        months -= 1
        # Get the last day of the previous month
        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year
        
        # Calculate days in previous month
        last_day_prev_month = datetime(prev_year, prev_month, 1)
        if prev_month == 12:
            next_month_year = prev_year + 1
            next_month = 1
        else:
            next_month_year = prev_year
            next_month = prev_month + 1
        
        days_in_prev_month = (datetime(next_month_year, next_month, 1) - last_day_prev_month).days
        days += days_in_prev_month
    
    # Adjust for negative months
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days


def main():
    """Main function to demonstrate the age calculator."""
    print("Age Calculator")
    print("-" * 40)
    
    # Example usage
    dob = input("Enter your date of birth (ddmmyyyy): ")
    
    try:
        years, months, days = calculate_age(dob)
        print(f"\nYour age is: {years} years, {months} months, and {days} days")
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
