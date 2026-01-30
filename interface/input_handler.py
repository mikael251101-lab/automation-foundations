def load_businesses_from_csv(filename):
    import csv
    businesses = []

    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = {k.strip().lower(): v for k, v in row.items()}
            row["income"] = float(row["income"])
            row["expenses"] = float(row["expenses"])
            row["cash"] = float(row["cash"])
            row["investment"] = float(row["investment"])
            businesses.append(row)

    return businesses