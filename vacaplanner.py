def hotel_cost(nights):
	return nights*120
def plane_ride_cost(destination):
	if destination=="Hawaii":
		return 500
	elif destination=="toukyou":#romaji
		return 2500
	elif destination=="New York":
		return 50
	else:
		return False
def rental(day):
	if day<3:
		return day*40
	if day>=3 and day<7:
		return day*40-20
	elif day>=7:
		return day*40-50

def overall_cost(city,days,spending_money):
	return hotel_cost(days)	+ rental_car_cost(days)+plane_ride_cost(city)+spending_money

print hotel_cost(9)+plane_ride_cost("toukyou")+rental(7)+350		
		
