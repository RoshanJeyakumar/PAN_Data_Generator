import csv
from faker import Faker
import datetime

def datagenerate(records, headers):
    fake = Faker('en_IN')
    with open("PAN_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):            
            writer.writerow({
                    "Name": fake.name(),
                    "Date of Birth" : fake.date(pattern="%d/%m/%Y", end_datetime=datetime.date(2000, 1,1)),
                    })
    
if __name__ == '__main__':
    records = 10
    headers = [ "Name", "Date of Birth"]
    datagenerate(records, headers)
    print("CSV generation complete!")
