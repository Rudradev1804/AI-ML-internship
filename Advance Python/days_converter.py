
# Python program to convert number of days into years, months and days.

# Ask the user to enter the number of days
numberOfDays = int(input("Enter number of days: "))

# Define the number of days in a year and a month
year = 365
month = 30

# Convert days to years
years = numberOfDays // year

# Get the remaining days
remaining_days_after_years = numberOfDays % year

# Convert remaining days to months
months = remaining_days_after_years // month

# Get the final remaining days
days = remaining_days_after_years % month

# Display the result
print(f"Years = {years}")
print(f"Months = {months}")
print(f"Days = {days}")
