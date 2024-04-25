from sorting_algorothms import *

data = random.sample(range(1, 51), 50)

# initialize the figure
fig, axes = plt.subplots(1, 5, figsize=(15, 4))
bars = []
algorithms = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort']
for i in range(len(axes)):
    axes[i].set_title(algorithms[i])
    bars.append(axes[i].bar(range(0, len(data)) , data, align='edge', color='blue'))

steps = [list(data)]
for step in bubble_sort(data):
    steps[0] += [list(step)]
    
# Bubble sort algorithm
def update(frame):
    for i, rect in enumerate(bars[2]):
        rect.set_height(frame[i])
        
ani = FuncAnimation(fig, func=update, frames=steps, interval=10, repeat=False)
plt.show()
