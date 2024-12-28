import math

class ZeroCouponBonds:
  def __init__(self, principal, maturity, interest_rate):
    self.principal = principal
    self.maturity = maturity
    self.interest_rate = interest_rate / 100

  def present_value_discrete(self, x ,n):
    return x / (1 + self.interest_rate) ** n

  def present_value_continous(self, x ,n):
    return x * math.exp(-self.interest_rate*n)
  
  def calculate_price(self):
    return self.present_value_continous(self.principal, self.maturity)


if __name__ == '__main__':
  principal = 1000
  maturity = 2
  interest_rate = 4

  zero_coupon_bond = ZeroCouponBonds(principal, maturity, interest_rate)
  print(zero_coupon_bond.calculate_price())
