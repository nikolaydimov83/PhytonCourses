total_snow_balls=int(input())
best_ball={"snowball_value":0}
for i in range(total_snow_balls):
    snowball_weight=int(input())
    snowball_time=int(input())
    snowball_quality=int(input())
    snowball_value =int((snowball_weight / snowball_time) ** snowball_quality)
    if (best_ball["snowball_value"]<snowball_value):
        best_ball={'snowball_weight':snowball_weight,'snowball_time':snowball_time,'snowball_quality':snowball_quality,'snowball_value':snowball_value}
print(f"{best_ball['snowball_weight']} : {best_ball['snowball_time']} = {best_ball['snowball_value']} ({best_ball['snowball_quality']})")
