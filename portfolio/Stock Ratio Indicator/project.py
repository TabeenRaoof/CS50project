import yfinance as yf
from ratios import pft, lvg, lqd, ROE



def main():
    opt_type = type_of_operation()

    '''
    Call the select_stock(opt_type) function in two different ways based on the operation type that the user selected:
    > if operation type 'a' has been selected, the function will return the same stock symbol twice as stock_1 and stock_2 because all ratio function imported from ratios.py take two parameters
    > if operation type 'b' was selected, the function will return the two stock symbols to the select_stock(opt_type) function
    '''
    if opt_type == 'a':
        selected_stock_1 = select_stock(opt_type)
        select_ratio(selected_stock_1, selected_stock_1)
    if opt_type == 'b':
        selected_stock_1, selected_stock_2 = select_stock(opt_type)
        select_ratio(selected_stock_1, selected_stock_2)

# Prompt User to input a type of operation
def type_of_operation():
    print('\nWelcome to Stock Ratio Indicator!')
    while True:
        # User Input to indicate type of operation (opt) >> Different input stype > opt = int(input('Would you like to a- Evaluate one stock; OR b- Compare two stocks (a/b)? '))
        opt = input('\n\nFirst, start by selecting the Type of operation (a/b): \n\na) Evaluate one stock \nb) Compare two stocks\n').lower()
        if opt == 'a' or opt == 'b':
            return opt

        else:
            print(f'\n{opt} is an invalid operation type')

# Run one of two operations based on input
def select_stock(opt_type):
    # If operation type 1 is selected > evaluate one stock
    if opt_type == 'a':
        while True:
            ticker_1 = input('\nNow, add the ticker of the stock you would like to evaluate: ').lower()
            try:
                validate = yf.Ticker(ticker_1)
                validate_ticker = validate.income_stmt.loc['Net Income']

                # print(f'You selected {ticker_1}')
                return ticker_1
            except:
                print(f'{ticker_1} is not a valid symbul')

    # If operation type 2 is selected > Compare 2 stocks
    if opt_type == 'b':

        while True:
            ticker_a = input('\nNow, add a stock symbul that you would like to compare: ').lower()
            try:
                validate_1 = yf.Ticker(ticker_a)
                validate_ticker = validate_1.income_stmt.loc['Net Income']
                break
            except:
                print(f'{ticker_a} is not a valid symbul')
                # Need to exit here or loop back to enter a valid ticker

    if opt_type == 'b':
        while True:
            ticker_b = input(f'Add a second stock symbul to compare to {ticker_a}: ').lower()

            if ticker_b != ticker_a:
                try:
                    validate_2 = yf.Ticker(ticker_b)
                    validate_ticker = validate_2.income_stmt.loc['Net Income']
                    break
                except:
                    print(f'{ticker_b} is not a valid ticker')
            else:
                print(f'You already added {ticker_a} as your first selection')

    print(f'You selected {ticker_a} and {ticker_b}')
    return ticker_a, ticker_b


# Assign the stock/s added by user to one of the functions from ratios.py
def select_ratio(stock_1, stock_2):
    while True:
        ratio_type = input('\n\nTo evaluate the stock, please select one of the ratios below: \n\na) Profitability - Net Profit Margin \nb) Leverage - Debt-to-Equity \nc) Management Efficiency - ROE \nd) Liquidity - Quick ratio \n').lower()
        if ratio_type == 'a':
            try:
                pft(stock_1, stock_2)
                file_Name = pft(stock_1, stock_2)
                break
            except:
                print('\nERROR: It is not possible to calculate Net Profit Margin at this time because one or more parameter/s for at lease one selected stock are not returned by the server')

        if ratio_type == 'b':
            try:
                lvg(stock_1, stock_2)
                file_Name = lvg(stock_1, stock_2)
                break
            except:
                print('\nERROR: It is not possible to calculate Debt-to-Equity at this time because one or more parameter/s for at lease one selected stock are not returned by the server')

        if ratio_type == 'c':
            try:
                ROE(stock_1, stock_2)
                file_Name = ROE(stock_1, stock_2)
                break
            except:
                print('\nERROR: It is not possible to calculate ROE at this time because one or more parameter/s for at lease one selected stock are not returned by the server')

        if ratio_type == 'd':
            try:
                lqd(stock_1, stock_2)
                file_Name = lqd(stock_1, stock_2)
                break
            except:
                print('\nERROR: It is not possible to calculate the Quick Ratio at this time because one or more parameter/s for at lease one selected stock are not returned by the server')

        elif ratio_type not in ['a', 'b', 'c', 'd']:
            print(f'\n"{ratio_type}" is not a valid selection, please select one of the folloeing: a, b, c or d')

    print(f'\n\nFrom the folder analysis/ open file "{file_Name}" to see the results \n\nImportant Note - Disclaimer: \n\nPlease note that this program is not intended to use for making financial or investment dicisions. This is a prototype and not a final product. If used, this tool should only be complimentary and a small part of extensive analysis an research on any company that you decide to invest in. Even then, this tool must not be used to finalize a financial decision or prefer a company over another in any shape of form. If this tool is used to complement your decisions, you are totally taking responsibility of your decisions.\n')


if __name__ == "__main__":
    main()
