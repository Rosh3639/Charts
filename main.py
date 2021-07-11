import matplotlib.pyplot as plt


def charts():
    x = [25, 30, 35, 40, 45, 50, 55, 60]
    y = [10000, 20000, 30000, 40000, 50000, 55000, 60000, 70000]
    while True:
        print("\nChoose a type of chart you want!",
              '\n1.Pie chart\n2.Bar chart\n3.Line chart\n4.Trend chart\n0.To exit')
        User_input = int(input("\nEnter a number: "))

        if User_input == 1:
            Labels = list('Age Group')
            plt.pie(y, labels=x, shadow=True, startangle=90)
            plt.legend(y, loc="best")
            plt.title('Pie chart')
            plt.show()
        elif User_input == 2:
            plt.bar(x, y)
            plt.xlabel('Age Group')
            plt.ylabel('Salary')
            plt.title('Bar chart')
            plt.show()
        elif User_input == 3:
            plt.plot(x, y)
            plt.xlabel('Age')
            plt.ylabel('Salary')
            plt.title('Line chart')
            plt.show()
        elif User_input == 4:
            plt.plot(x, y, marker='o')
            plt.xlabel('Age')
            plt.ylabel('Salary')
            plt.title('Trend chart')
            plt.show()
        elif User_input > 4:
            print("Invalid!")
            break
        elif User_input == 0:
            break


if __name__ == '__main__':
    charts()
