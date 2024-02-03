import matplotlib.pyplot as plt

# Read data from file
data = []
with open('score_gameCNT.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        episode, score = map(int, line.strip().split(','))
        data.append((episode, score))

# Separate the data into two lists for plotting
episodes, scores = zip(*data)

# Create scatterplot
plt.scatter(episodes, scores)
plt.xlabel('Episode')
plt.ylabel('Score')
plt.title('Score per Episode')
plt.show()