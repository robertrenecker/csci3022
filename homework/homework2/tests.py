import numpy as np;
import random;
import matplotlib.pylab as plt
def miniopoly_turn(location, cash):
    #roll two dice

    diceRolls = [np.random.randint(1,6) for i in range(2)];
    rollSum = sum(diceRolls);
    if location == 30:
            if diceRolls[0] != diceRolls[1]:
                print("You ain't out of jail yet!");
            else:
                print("You are out of jail!, moving %d squares from square 10." % rollSum);
                location = 10+rollSum;
    else:
        location += rollSum;
        if location > 40:
            location = location%40;
        if location == 30:
            #print("go to jail");
            return(location,cash);
        elif location in [2,7,17,22,33,36]:
            #Draw a card
            cardResult = np.random.choice([-100,-50,50,100,200]);
            #print("You landed on square %d" % location);
            #print("you chose card %d , meaning your cash went from %d to %d"% (cardResult, cash, cash+cardResult));
            cash += cardResult;
        elif location == 40:
            #print("You got GO! take $200!");
            cash += 200;
            location = 0;
        else:
            cash -= location;

    if cash <= 0:
        print("You went bankrupt! You LOSE! buhbye.");
        #print("Game ended, please stop calling this function");
        return (-1, cash)



    # your code goes here!

    return location, cash


frequency_cash = [];
for i in range(5000):
    location = 0;
    turn = 0;
    cash = 200;
    while turn<30 and cash >0:
        location, cash = miniopoly_turn(location,cash);
        turn+= 1;
    frequency_cash.append(cash);
n, bins, patches = plt.hist(frequency_cash, bins=18, facecolor='green', range=[min(frequency_cash),max(frequency_cash)]);

plt.xlabel('Remaining Cash');
plt.ylabel('Frequency');
plt.title("Frequency of remaining cash via 5000 iterations of Miniopoly");
plt.grid(True);
plt.show();
