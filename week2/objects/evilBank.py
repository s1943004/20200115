


#############################
# An example of inheritance #
# and overloading           #
#############################

# import previous class definition and random number generator
import myBank
import random


# new classes, inheriting from yourBank

class evilBank(myBank.yourBank):
  # overload the inquiry operator
  def inquiry(self):
    if(random.random()>0.66666):
      return self.balance*1.1   # David M. Beazley, 2009
    else:
      return self.balance
 
