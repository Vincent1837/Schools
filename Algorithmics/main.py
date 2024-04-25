from sorting_algorothms import*

if __name__ == '__main__':

    # Generate a random permutation of 50 numbers ranging from 1 to 50.
    data = random.sample(range(1, 51), 50)

    # initialize the figure
    fig, axes = plt.subplots(1, 5, figsize=(15, 4))
    bars = []
    algorithms = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort']
    for i, ax in enumerate(axes):
        ax.set_title(algorithms[i])
        ax.set_ylim(top=55)
        ax.set(xticks=[], yticks=[])
        ax.autoscale()
        bars.append(ax.bar(range(len(data)), data, align='edge', color='blue'))
    
    bubble_sort_steps = [list(data)]
    insertion_sort_steps = [list(data)]
    
    for i in bubble_sort(data.copy()):
        bubble_sort_steps += [list(i)]
    for i in insertion_sort(data.copy()):
        insertion_sort_steps += [list(i)]


    max_step = max(len(bubble_sort_steps), len(insertion_sort_steps))

    if len(bubble_sort_steps) < max_step:
        bubble_sort_steps += [bubble_sort_steps[-1] for i in range(max_step - len(bubble_sort_steps))]
    if len(insertion_sort_steps) < max_step:
        insertion_sort_steps += [insertion_sort_steps[-1] for i in range(max_step - len(insertion_sort_steps))]
    
    

    # Bubble sort algorithm
    def update(frame):
        for i, rect in enumerate(bars[1]):
            rect.set_height(frame[i])
        
    ani = FuncAnimation(fig, func=update, frames=insertion_sort_steps, interval=1, repeat=False)
    plt.show()

    



    """ # Insertion sort algorithm
    for step in insertion_sort_steps:
        for i, rect in enumerate(bars[1]):
            rect.set_height(step[i])
            
        plt.pause(0.1) """

