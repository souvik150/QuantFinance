import math

class CouponBond:

  def __init__(self, principal, rate, maturity, interest_rate):
    self.principal = principal
    # rate = coupoun rate
    self.rate = rate / 100
    self.maturity = maturity
    self.interest_rate = interest_rate / 100

  def present_value_discrete(self, x, n):
    return x / (1 + self.interest_rate) ** n

  def present_value_continuous(self, x, n):
    return x * math.exp(-self.interest_rate*n)
  
  def calculate_price(self):
    price = 0

    # discount the coupon payments
    for t in range(1, self.maturity+1):
      coupon_price = self.principal * self.rate
      price += self.present_value_continuous(coupon_price, t)

    # discount principle amout
    price += self.present_value_continuous(self.principal, self.maturity)

    return price

if __name__ == '__main__':
  bond = CouponBond(1000, 10, 3, 4)
  print(bond.calculate_price())



'''
The term "discount the payments" refers to the process of calculating the present value of future cash flows. This involves adjusting the value of future payments to reflect their value in today's terms, which accounts for the time value of money.

Why is it called "discounting"?
The value of money decreases over time due to factors like inflation, risk, and opportunity cost. A dollar today is worth more than a dollar in the future because you can invest the dollar today and earn interest. The process of discounting adjusts future payments (e.g., coupon payments or the principal) to reflect their reduced value in today's terms.
'''

