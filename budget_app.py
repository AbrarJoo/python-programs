

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"

        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"

        total = f"Total: {self.get_balance()}"
        return title + items + total


def create_spend_chart(categories):

    # Title
    chart = "Percentage spent by category\n"

    # Calculate spending
    spends = []
    total_spent = 0

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        spends.append(spent)
        total_spent += spent

    # Percentages rounded down to nearest 10
    percentages = []
    for spent in spends:
        percent = int((spent / total_spent) * 100)
        percentages.append(percent - (percent % 10))

    # Bars
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical names
    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i != max_len - 1:
            chart += "\n"

    return chart



