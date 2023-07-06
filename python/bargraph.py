import matplotlib.pyplot as plt

def plot_bar_graph(students, marks):
    colors = ['red', 'blue', 'green', 'yellow', 'orange']
    
    plt.bar(students, marks, color=colors)
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.title('Student Marks')
    plt.show()

if __name__ == '__main__':
    students = ['Arceus', 'Bobby', 'Sagarika', 'David', 'Eve']
    marks = ['50','40','80','20']
    
    for student in students:
        mark = int(input(f"Enter the marks for {student}: "))
        marks.append(mark)
    
    plot_bar_graph(students, marks)
