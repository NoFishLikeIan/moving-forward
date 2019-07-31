import random
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import sys

def show_up(prob_show):
    return random.random() < prob_show

def simulate_flight(nb_tickets_sold, prob_show):
    n = 0
    for i in range(nb_tickets_sold):
        if show_up(prob_show):
            n += 1
    
    return n

def simulate_revenue(nb_tickets_sold, nb_seats, prob_show, rev_per_seat, voucher_cost):
    nb_shows = simulate_flight(nb_tickets_sold, prob_show)

    if nb_shows <= nb_seats:
        return rev_per_seat * nb_shows
    else:
        voucher_out = nb_shows-nb_seats
        return nb_seats * rev_per_seat - voucher_cost * voucher_out

prob_show = .95
nb_seats = 100
rev_per_seat = 350.
voucher_cost = rev_per_seat * 2

nb_flights = 100000
max_overbooking = 15
revenue = np.zeros((nb_flights,max_overbooking+1))
for tix_overbooked in range(1,max_overbooking):

    nb_tickets_sold = nb_seats + tix_overbooked
    for flight in range(nb_flights):
        pct = flight/nb_flights*max_overbooking
        str = f'{np.round(pct, decimals = 3)*100} percentage complete'
        print(str, end='\r')
        sys.stdout.flush()
        revenue[flight, tix_overbooked] = simulate_revenue(nb_tickets_sold, nb_seats, prob_show, rev_per_seat, voucher_cost)

plt.figure(figsize=(15,10))
plt.boxplot(revenue)
plt.ylim(20000,40000)
plt.show()
