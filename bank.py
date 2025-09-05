# bank.py
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} 元已存入帳戶。")
        else:
            print("存款金額必須大於 0。")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} 元已從帳戶中提領。")
        else:
            print("笑死，餘額不足。")

    def show_balance(self):
        print(f"帳戶：{self.owner} 餘額：{self.balance} 元")


# ------------------------------
# 主程式
# ------------------------------

def main():
    name = input("請輸入帳戶名稱：")
    account = BankAccount(name)

    while True:
        action = input("你想做什麼？[存款 / 提款 / 查詢 / 離開]：")

        if action == "存款":
            try:
                amount = int(input("請輸入存款金額："))
                account.deposit(amount)
            except ValueError:
                print("請輸入有效數字。")

        elif action == "提款":
            try:
                amount = int(input("請輸入提款金額："))
                account.withdraw(amount)
            except ValueError:
                print("請輸入有效數字。")

        elif action == "查詢":
            account.show_balance()

        elif action == "離開":
            print("謝謝使用，再見！")
            break

        else:
            print("無效的操作，請重新輸入。")


if __name__ == "__main__":
    main()
