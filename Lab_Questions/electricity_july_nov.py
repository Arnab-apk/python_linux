"""Read customer electricity data and print July and November consumption.

Expected file format (CSV):
customer,july,nov
Anita,120,160
Rahul,95,140
"""

import csv

file_path = input("Enter path of the electricity data file: ").strip()

try:
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            print("File is empty or invalid")
            raise SystemExit(1)

        fields = [name.strip().lower() for name in reader.fieldnames]
        if "july" not in fields or "nov" not in fields:
            print("Required columns 'july' and 'nov' not found")
            raise SystemExit(1)

        # Map lowercase names to original names to safely access row keys.
        key_map = {name.strip().lower(): name for name in reader.fieldnames}
        july_key = key_map["july"]
        nov_key = key_map["nov"]
        customer_key = key_map.get("customer")

        print("\nElectricity consumption for July and November:")
        for idx, row in enumerate(reader, start=1):
            customer = row.get(customer_key, f"Customer{idx}") if customer_key else f"Customer{idx}"
            july_val = row.get(july_key, "")
            nov_val = row.get(nov_key, "")
            print(f"{customer}: July = {july_val}, November = {nov_val}")

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error reading file:", e)
