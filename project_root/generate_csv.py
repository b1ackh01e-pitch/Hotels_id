import csv
from datetime import datetime, timedelta
import os

# List of hotel IDs
hotel_ids = [18482, 18483, 18484, 18485, 18486]

# Generate 25 different check-in and check-out date combinations
date_format = "%Y-%m-%d"
start_date = datetime.strptime("2023-10-30", date_format)

# Function to generate date ranges
def generate_dates(start_date, num_days):
    return [(start_date + timedelta(days=i), start_date + timedelta(days=i+1)) for i in range(num_days)]

date_combinations = generate_dates(start_date, 25)

# Prepare CSV data
csv_data = []
for hotel_id in hotel_ids:
    for check_in, check_out in date_combinations:
        csv_data.append([hotel_id, check_in.strftime(date_format), check_out.strftime(date_format)])

# Create the directory if it doesn't exist
os.makedirs('CheckinCheckout', exist_ok=True)

# Write CSV file
csv_file_path = 'CheckinCheckout/hotels_data.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Hotel_id", "Checkin", "Checkout"])
    writer.writerows(csv_data)

print(f"CSV file has been created at: {csv_file_path}")
