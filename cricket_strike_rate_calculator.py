#title
print("Strike_rate calculator")

#main_code
def strike_rate(runs, balls):
    return (runs / balls) * 100
  
r = int(input("Enter runs:"))
b = int(input("Enter balls played:"))
strike__rate = round(strike_rate(r, b),2)
print("SR is",strike__rate)

if strike__rate > 600:
    print(" POSSIBLE CHEATING DETECTED OR THE BOWLER IS PLAYING WIDEBALL CRICKET")
elif strike__rate >= 150:
    print("BATTER ATE 500 EGGS FOR BREAKFAST")
elif strike__rate >= 120:
    print("BATTER IS A FAN OF KL RAHUL")
else:
    print("BATTER IS A HUGE FAN OF RAHUL DRAVID!!!")