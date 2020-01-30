# https://www.interviewbit.com/problems/hotel-bookings-possible/

# Hotel Booking Possible

# Input : 
#         Arrivals :   [1 3 5]
#         Departures : [2 6 8]
#         K : 1

# Return : False / 0 

# At day = 5, there are 2 guests in the hotel. But I have only one room. 

class Solution:
    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)
        
        # print(events)

        guests = 0

        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1

            if guests > K:
                return 0

        return 1