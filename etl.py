import json

def extract():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def transform(data):
    cleaned = []

    for d in data:
        if d["amount"] is None:
            continue

        amount = int(d["amount"])

        if amount < 0:
            continue

        cleaned.append({
            "id": int(d["id"]),
            "amount": amount,
            "status": d["status"].upper()
        })

    return cleaned

def run():
    data = extract()
    result = transform(data)
    print(result)

if __name__ == "__main__":
    run()