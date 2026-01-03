("\n******START******\n")

#for calling candidates in loop
for call in range(1, 6):
    print(f"Calling candidate numer: {call}")

#for checking stocks for the day
for Stocks in range(1, 6):
        print(f"Checking stock price for the day: {Stocks}")

#for printing numbers from 1 to 5
for num in range(1, 6):
        print(num)

#for printin evens numbers
for num in range(1, 6):
    if num % 2 == 0:
        print(num)

#for print odd numbers
for num in range(1, 6):
    if num %2 != 0:
        print(num)

#for printing stocks from the watchlist
Stocks = ["gail", "ongc", "coalinda"]

for stock in Stocks:
     print(f" Analyzing stocks : {stock}") 
      
#counting profit days
prices = [170, 172, 175, 180, 117]
profit_days = 0

for price in prices:
     if price >= 170:
          profit_days += 1 #counter

print(f"Print number of days:", profit_days)