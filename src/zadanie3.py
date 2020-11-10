import math
import unittest


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


#
# invoice1 = {
#             "customer": "BigCo",
#             "performances": [
#                 {
#                     "playID": "hamlet",
#                     "audience": 55
#                 }
#             ]
#         }
# plays1 = {
#             "hamlet": {"name": "Hamlet", "type": "tragedy"}
#         }

# print(statement(invoice1, plays1))

class StatementTest(unittest.TestCase):

    def test_hamlet_audience_55(self):
        invoice1 = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                }
            ]
        }
        plays1 = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        }

        result1 = "Statement for BigCo\n Hamlet: $650.00 (55 seats)\nAmount owed is $650.00\nYou earned 25 credits\n"
        self.assertEqual(statement(invoice1, plays1), result1)

    def test_hamlet_audience_20(self):
        invoice2 = {"customer": "BigCo",
                    "performances": [{"playID": "hamlet", "audience": 20}]}
        plays2 = {"hamlet": {"name": "Hamlet", "type": "tragedy"}}

        result2 = "Statement for BigCo\n Hamlet: $400.00 (20 seats)\nAmount owed is $400.00\nYou earned 0 credits\n"

        self.assertEqual(statement(invoice2, plays2), result2)

    def test_as_you_like_it_35(self):
        invoice3 = {"customer": "BigCo",
                    "performances": [{
      "playID": "as-like",
      "audience": 35
    },]}
        plays3 = {"as-like": {"name": "As You Like It", "type": "comedy"}}

        result3 = "Statement for BigCo\n As You Like It: $580.00 (35 seats)\nAmount owed is $580.00\nYou earned 12 credits\n"

        self.assertEqual(statement(invoice3, plays3), result3)



if __name__ == "__main__":
    unittest.main()
