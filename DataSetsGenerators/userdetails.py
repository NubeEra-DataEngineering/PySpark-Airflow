#pip install faker
import csv
from faker import Faker
import random

def generate_random_data(num_rows):
    fake = Faker()
    header = ["user_id", "user_name", "age"]

    with open('userdetails.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)

        for _ in range(num_rows):
            user_id = fake.uuid4()
            name = fake.name()
            age = random.randint(18, 99)

            row = [user_id, name, age]
            csv_writer.writerow(row)

if __name__ == "__main__":
    num_rows_to_generate = 100  # Adjust the number of rows as needed
    generate_random_data(num_rows_to_generate)
