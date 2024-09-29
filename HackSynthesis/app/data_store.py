import json

def save_contribution(account, location, amount):
    data = load_contributions()
    if account not in data:
        data[account] = []
    data[account].append({"location": location, "amount": amount})
    with open('contributions.json', 'w') as f:
        json.dump(data, f)

def load_contributions():
    try:
        with open('contributions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
