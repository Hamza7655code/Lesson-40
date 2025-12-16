from datetime import date, datetime
b1 = input("Input your date of birth (YYYY-MM-DD): ")
current_year = date.today().year
b2 = datetime.strptime(b1, "%Y-%m-%d").date().year
age = current_year - b2
print(f"Your age is: {age}")
