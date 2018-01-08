total_distance_travelled=10
total_time_in_minutes=43 + 30.0/60
miles_per_km=1/1.61

distance_travelled_in_miles=total_distance_travelled*miles_per_km

average_time_per_mile=total_time_in_minutes/distance_travelled_in_miles

average_speed_in_miles_per_hour=distance_travelled_in_miles/(total_time_in_minutes/60)


print "average time per mile",
print average_time_per_mile

print "average speed in miles per hour",
print average_speed_in_miles_per_hour
