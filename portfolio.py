
import pandas as pd     # Seems an obvious choice for easier .csv work

def load_investments(fname):

    # Take in .csv file: Pandas will handle the "quotes problem" by default with read_csv()
    options = pd.read_csv(fname, usecols=['RegionName', 'Zhvi', '10Year'], skiprows=[1])
    options['ROI'] = options['Zhvi'] * options['10Year']    # Create 'ROI' column from calculation provided
    options = options.drop(columns=['10Year'])              # Drop the "no-longer-necessary" column

    # List comprehension of the dataframe for an aggregated, iterable return
    # Pandas' itertuples() will organize rows of dataframe neatly for us
    processed_options = [i for i in options.itertuples(index=False, name=None)]

    return processed_options


def optimize_investments(options_in, budget_in):

    num_options = len(options_in)

    # We create a value table initialized with ROI values of 0. From here we reference the ultimate "optimal" ROI after processing
    values = [[0 for i in range(budget_in + 1)] for i in range(num_options + 1)]

    # We create a traceback table of empty lists in which to store our "successive" additions of investment names
    traceback = [[[] for i in range(budget_in + 1)] for i in range(num_options + 1)]

    for i in range(num_options):          # For each investment option
        name, cost, roi = options_in[i]   # Extract data of that option

        for test_val in range(budget_in + 1):  # For all possible budget values

            if cost <= test_val:    # If the cost of this option is less than the budget being tested

                if roi + values[i][test_val - cost] > values[i][test_val]:  # If the 'ROI' is improved

                    values[i+1][test_val] = roi + values[i][test_val - cost]    # Update value table with improved 'ROI'

                    traceback[i+1][test_val] = traceback[i][test_val - cost] + [name]   # Update traceback table with 'name' of option

                else:   # If the 'ROI' is NOT improved
                    # "ignore" the new info and "bring forward" the previous-best info in both 'values' and 'traceback' table
                    values[i+1][test_val] = values[i][test_val]
                    traceback[i+1][test_val] = traceback[i][test_val]

            else:   # If the cost of this option is too high for the 'test_val' of our 'budget_in'
                # "ignore" the new info and "bring forward" the previous-best info in both 'values' and 'traceback' table
                values[i+1][test_val] = values[i][test_val]
                traceback[i+1][test_val] = traceback[i][test_val]

    # After we've iterated through the tables using our 'budget_in' and investment 'options', we can extract the optimal
    # 'ROI' value and the 'names' of our investments from the tables as follows
    # These will be stored at the "final" position of the tables, the maximum indices in both dimensions
    # These indices would be equivalent to the values of 'num_options' and 'budget_in',
    # which we used to construct the tables in the first place

    optimal_roi = values[num_options][budget_in]
    options_names = traceback[num_options][budget_in]

    return optimal_roi, options_names



# Testing

file_full = 'state_zhvi_summary_allhomes.csv'
budget_full = 1000000
full_options = load_investments(file_full)
print(optimize_investments(full_options, budget_full))
