import math
events=input().split('|')
energy=100
coins=100
interupted=False
for i in range(len(events)):
    event=events[i].split('-')
    event_type=event[0]
    event_value=int(event[1])

    if (event_type=='rest'):
        energy_before=energy
        new_energy=energy+event_value
        energy=min(100, new_energy)
        print(f"You gained {energy-energy_before} energy.")
        print(f"Current energy: {energy}.")
    elif event_type=='order':
        if energy>=30:
            coins+=event_value
            energy-=30
            print(f"You earned {event_value} coins.")

        else:
            energy_before=energy
            new_energy=energy+50
            energy=min(100, new_energy)
            print("You had to rest!")
    else:
        if(coins>=event_value):
            coins-=event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            interupted=True
            break


if (interupted==False):
    print("Day completed!" )
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")