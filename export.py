# export

# data = "Phone_base.csv"
# separating = "\n"

def export_contacts(data, sepa):
    with open(f"{data}", "r", encoding="utf-8") as file:
        line_count = sum(1 for line in open(f"{data}"))
        for i in range (line_count):
            a = file.readline().split("; ")
            print(f'{sepa}'.join(a))

export_contacts(data, separating)
