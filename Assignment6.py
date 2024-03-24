class Creditcard:

    def __init__(self, card_num):
        self.digits = [int(d) for d in str(card_num)]

    def luhn_check(self):
        odd_digits = self.digits[-1::-2]
        even_digits = self.digits[-2::-2]
        double_even_digits = [2 * d - 9 if d > 4 else 2 * d for d in even_digits]
        num_check = sum(odd_digits) + sum(double_even_digits)
        mod_check = num_check % 10
        if mod_check == 0:
            return "Valid Credit Card"
        else:
            return "The credit card number you entered is invalid."

    def bank_check(self):
        bank_dict = {1: "Airlines", 2: "Airlines or Financial", 3: "American Express", 4: "Visa", 5: "Mastercard",
                     6: "Discover"}
        return bank_dict[self.digits[0]]

    def bank_id(self):
        id = self.digits[1:6]
        str_id = ''.join([str(d) for d in id])
        return str_id

    def acct_num(self):
        acct_id = self.digits[7:]
        acc_num = ''.join([str(d) for d in acct_id])
        return acc_num

    def get_bank_info(self, database):
        bank = database.info(self.bank_id())
        if bank:
            return bank
        else:
            return False