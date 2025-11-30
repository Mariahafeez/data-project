import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(url):                            # url is the path of sales_csv file
    # First Read  csv file
    data = pd.read_csv(url)
    return data
    # print(data)


def main(url):
    data = read_data(url)

    # Collect all sales across each month in a list
    monthly_sales = list(data['sales'])
    print('The sales across each month are:{}'.format(monthly_sales))

    # Total Sales across all months
    total = sum(monthly_sales)
    print('Total Sales:{}'.format(total))

    # Average=Total sale/Total no of months
    average_sale = round(total/12, 2)
    print('Average sale in a year:{}'.format(average_sale))

    # To delete those column which are not required drop() method is used
    new_data = data.drop(['year', 'expenditure'], axis=1)  # drop() is used to delete column
    print(new_data)
    # sort_values()method is used to arrange sales column in ascending order
    sorted_data = new_data.sort_values('sales', ascending=True)
    # print(sorted_data)

    # Lowest sale Month
    lowest_sale_month = sorted_data.head(1)
    print('The lowest sales month is :\n{}'.format(lowest_sale_month))

    # Highest Sale Month
    highest_sale_month = sorted_data.tail(1)
    print('The highest sales month is:\n{}'.format(highest_sale_month))

    # Annual Expenditure
    total_expenditure = sum(data['expenditure'])
    print('Total Expenditure is:{}'.format(total_expenditure))

    # x axis values
    x = data['month']

    # y axis values
    y = data['sales']
    # plotting strip plot with seaborn
    ax = sns.stripplot(x=data['month'],y=data['sales']);

    # giving labels to x-axis and y-axis
    ax.set(xlabel='Months', ylabel='Sales')
    # giving title to the plot
    plt.title('Sales graph');

    # function to show plot
    plt.show()

main('/Users/mariahafeez/Downloads/Student Guides/sales.csv')
# read_data('/Users/mariahafeez/Downloads/Student Guides/sales.csv')




