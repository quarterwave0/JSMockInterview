import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
numberIterations = 500

def game(threshold, isPartTwo):
    diceValue = 1 
    remainingRounds = 100
    moneyCollected = 0

    while remainingRounds > 0:
        collection, reroll = play(diceValue, threshold, isPartTwo)
        
        diceValue = reroll
        moneyCollected += collection
        
        remainingRounds-=1
        
    return moneyCollected
    
    
def play(diceValue, threshold, isPartTwo):
        
    if(diceValue>=threshold): #we take
        if isPartTwo:
            return diceValue, 0
        else:
            return diceValue, diceValue
    
    else: #we reroll
        diceValue = reroll()
        return 0, diceValue
            

def reroll():
    return rng.integers(1, 21, 1)[0]

def generatePlotsNStuff(data, isPartTwo):
    fig, ax = plt.subplots(dpi=300)
    ax.bar(np.arange(20), data)
    ax.set_xlabel('Dice Hold Threshold')
    ax.set_ylabel(f"Mean Collection Over {numberIterations} Iterations")
    ax.set_xticks(np.arange(20), np.arange(1, 21))
    
    optimalHold = np.argmax(data)+1
    valueDelivered = data[optimalHold-1]
    if isPartTwo:
        print()
        print(f"Optimal Part 2 Hold: {optimalHold}")
        print(f"With Value: ${valueDelivered}")
    else:
        print(f"Optimal Hold: {optimalHold}")
        print(f"With Value: ${valueDelivered}")

def operateSimulation(isPartTwo):
    returns = np.zeros((20, numberIterations))
    
    for i in range(numberIterations):
        for threshold in range(1, 21):
            returns[threshold-1][i] = game(threshold, isPartTwo)
            
    return np.mean(returns, axis = 1)

if __name__ == "__main__":
    
    part1 = operateSimulation(False)
    part2 = operateSimulation(True)
    
    generatePlotsNStuff(part1, False)
    generatePlotsNStuff(part2, True)
    
    
    