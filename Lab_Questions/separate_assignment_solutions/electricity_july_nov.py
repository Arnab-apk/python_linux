"""Print electricity consumption for July and November."""

customers = {
    "Anita": {"july": 120, "nov": 160},
    "Rahul": {"july": 95, "nov": 140},
    "Priya": {"july": 110, "nov": 155},
    "Vikram": {"july": 130, "nov": 145}
}

print("Electricity Consumption (July & November)\n")
for customer, consumption in customers.items():
    print(f"{customer}: July = {consumption['july']} units, November = {consumption['nov']} units")
