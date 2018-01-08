import math

radius=5
pi = math.pi
print "Volume of sphere",
print 4/3.0*pi*radius**3

total_book_quantity=60
price_of_book=24.95
discount=40/100.0*24.95
shipping_cost=3
actual_price=price_of_book-discount

print "Total wholesale cost",
print actual_price + shipping_cost + (total_book_quantity-1)*(actual_price + .75)

time=6 + 52/60.0
easy_pace_time_per_mile=8 + 15/60.0
tempo_pace_time_per_mile=7 + 12/60.0

total_time=2*(1*easy_pace_time_per_mile + 3 * tempo_pace_time_per_mile + 1*easy_pace_time_per_mile)/60.0
time_when_reached=total_time+time;

print "Time when reached home in hours",
print time_when_reached
