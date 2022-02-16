class LogicRequests:

    def __init__(self):
        self.user = None

    @staticmethod
    def valid_id(id):
        if len(id) != 9:
            return False
        return sum((int(digit) * (idx % 2 + 1)) % 10 + (int(digit) * (idx % 2 + 1)) / 10 for idx, digit in
                   enumerate(id)) % 10 == 0