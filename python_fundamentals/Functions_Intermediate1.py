# 1.please create a function randInt() where 
# randInt() returns a random integer between 0 to 100

def rando_integer():
  import random
  return random.random()*100

# 2.please create a function randInt() where 
# randInt(max=50) returns a random integer between 0 to 50
def rando_integer(max=50):
  import random
  return random.random()*50


rando_integer()

# 3.please create a function randInt() where 
# randInt(min=50) returns a random integer between 50 to 100
def rando_integer():
  import random
  return random.randrange(50,101,1)

rando_integer()

# 4.please create a function randInt() where 
# randInt(min=50, max=500) returns a random integer between 50 and 500
def rando_integer():
  import random
  return random.randrange(50,500,1)
  
rando_integer()