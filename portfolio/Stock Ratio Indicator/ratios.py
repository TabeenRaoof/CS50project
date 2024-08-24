import matplotlib.pyplot as plt
import yfinance as yf
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


def pft(stock_1, stock_2):
        # Get stock 1 & 2 and assign them to different variables
        stk_1 = yf.Ticker(stock_1)
        stk_2 = yf.Ticker(stock_2)

        # Change both stock symbols to upper letters
        stock_1 = stock_1.upper()
        stock_2 = stock_2.upper()

        # Plot style - Some styles to use >> default, ggplot, Solarize_Light2, seaborn-v0_8
        plt.style.use('ggplot')

        # Assign income statement for stock 1 to a variable
        income_statement_stk_1 = stk_1.get_income_stmt()
        # Profitability - Net Profit Margin ratio for stock 1 by deviding Net Income by Total Revenu
        profitability_stk_1 = income_statement_stk_1.loc['NetIncome'].values/income_statement_stk_1.loc['TotalRevenue'].values
        ''' Plot Net Profit Margin ratio from above on the y axis and the year on the x axis by useing the index from NetIncome which
            is the the year for all other data as well (NetIncome and TotalRevenu have the same data for year - could use either)'''
        plt.plot(income_statement_stk_1.loc['NetIncome'].index, profitability_stk_1, marker='o')

        ''' Only implement the second plot if stock 1 is different than stock 2 meaning that operation
            type b was selected to compare 2 stocks in function_2 > project.py'''
        if stock_1 != stock_2:
            # same comments from stock 1 above apply ot the stock 2 below 3 lines
            income_statement_stk_2 = stk_2.get_income_stmt()
            profitability_stk_2 = income_statement_stk_2.loc['NetIncome'].values/income_statement_stk_2.loc['TotalRevenue'].values
            plt.plot(income_statement_stk_2.loc['NetIncome'].index, profitability_stk_2, marker='o')

        ''' When stock_1 and stock_2 are the same, it means that operation a has been selected in function_2 >
            project.py to evaluate 1 stock - to select the appropriate plot title below'''
        if stock_1 == stock_2:
            # Create title for the plot with name of stock_1 only
            plt.title(f'Net Profit Margin - {stock_1}')
            # Tilt x axis to avoid the years colliding
            plt.xticks(rotation=30)
            # Save file with name consists of ratio_stock_1
            plt.savefig(f'analysis/NetPftMgn_<{stock_1}>.png')
            return f'NetPftMgn_<{stock_1}>.png'


        ''' Only implement the second plot if stock_1 is different than stock_2 meaning that operation type b was selected to compare
            2 stocks in function_2 > project.py - title to indicate both stocks and graph lines to be identified'''
        if stock_1 != stock_2:
            # Create title for the plot with both stock names
            plt.legend((stock_1, stock_2),
               loc='lower left')
            plt.title(f'Net Profit Margin - {stock_1} vs {stock_2}')
            # Tilt x axis to avoid the years colliding
            plt.xticks(rotation=30)
            # Save file with name consists of ratio_stock1_VS_stock2
            plt.savefig(f'analysis/NetPftMgn_<{stock_1}>vs<{stock_2}>.png')
            return f'NetPftMgn_<{stock_1}>vs<{stock_2}>.png'


def ROE(stock_1, stock_2):
     # Get stock 1 & 2 and assign them to different variables
        stk_1 = yf.Ticker(stock_1)
        stk_2 = yf.Ticker(stock_2)

        # Change both stock symbols to upper letters
        stock_1 = stock_1.upper()
        stock_2 = stock_2.upper()

        # Plot style - Some styles to use >> default, ggplot, Solarize_Light2, seaborn-v0_8
        plt.style.use('ggplot')

        # Assign income statement and balance sheet for stock 1 to 2 variables
        income_statement_stk_1 = stk_1.get_income_stmt()
        balance_sheet_stk_1 = stk_1.get_balance_sheet()
        # Profitability - Net Profit Margin ratio for stock 1 by deviding Net Income by Total Revenu
        profitability_stk_1 = income_statement_stk_1.loc['NetIncome'].values/balance_sheet_stk_1.loc['StockholdersEquity'].values
        ''' Plot Net Profit Margin ratio from above on the y axis and the year on the x axis by useing the index from NetIncome which
            is the the year for all other data as well (NetIncome and TotalRevenu have the same data for year - could use either)'''
        plt.plot(income_statement_stk_1.loc['NetIncome'].index, profitability_stk_1, marker='o')

        ''' Only implement the second plot if stock 1 is different than stock 2 meaning that operation
            type b was selected to compare 2 stocks in function_2 > project.py'''
        if stock_1 != stock_2:
            # same comments from stock 1 above apply ot the stock 2 below 3 lines
            income_statement_stk_2 = stk_2.get_income_stmt()
            balance_sheet_stk_2 = stk_2.get_balance_sheet()
            profitability_stk_2 = income_statement_stk_2.loc['NetIncome'].values/balance_sheet_stk_2.loc['StockholdersEquity'].values
            plt.plot(income_statement_stk_2.loc['NetIncome'].index, profitability_stk_2, marker='o')

        ''' When stock_1 and stock_2 are the same, it means that operation a has been selected in function_2 >
            project.py to evaluate 1 stock - to select the appropriate plot title below'''
        if stock_1 == stock_2:
            # Create title for the plot with name of stock_1 only
            plt.title(f'Return on Equity - {stock_1}')
            # Tilt x axis to avoid the years colliding
            plt.xticks(rotation=30)
            # Save file with name consists of ratio_stock_1
            plt.savefig(f'analysis/ROE_<{stock_1}>.png')
            return f'ROE_<{stock_1}>.png'

        ''' Only implement the second plot if stock_1 is different than stock_2 meaning that operation type b was selected to compare
            2 stocks in function_2 > project.py - title to indicate both stocks and graph lines to be identified'''
        if stock_1 != stock_2:
            # Create title for the plot with both stock names
            plt.legend((stock_1, stock_2),
               loc='lower left')
            plt.title(f'Return on Equity - {stock_1} vs {stock_2}')
            # Tilt x axis to avoid the years colliding
            plt.xticks(rotation=30)
            # Save file with name consists of ratio_stock1_VS_stock2
            plt.savefig(f'analysis/ROE_<{stock_1}>vs<{stock_2}>.png')
            return f'ROE_<{stock_1}>vs<{stock_2}>.png'


# Liquidity - Quick Ratio - (current asset - inventory) / current liability
def lqd(stock_1, stock_2):
        # Get stock 1 & 2 and assign them to different variables
        stk_1 = yf.Ticker(stock_1)
        stk_2 = yf.Ticker(stock_2)

        # Change both stock symbols to upper letters
        stock_1 = stock_1.upper()
        stock_2 = stock_2.upper()

        # Plot style - Some styles to use >> default, ggplot, Solarize_Light2, seaborn-v0_8
        plt.style.use('ggplot')

        # Assign income statement for stock 1 to a variable
        balance_sheet_stk_1 = stk_1.get_balance_sheet()
        # Profitability - Net Profit Margin ratio for stock 1 by deviding Net Income by Total Revenu
        # liquidity_stk_1 = (balance_sheet_stk_1.loc['CurrentAssets'].values - balance_sheet_stk_1.loc['Inventory'].values) / balance_sheet_stk_1.loc['CurrentLiabilities'].values
        liquidity_stk_1 = balance_sheet_stk_1.loc['Inventory'].values / balance_sheet_stk_1.loc['CurrentLiabilities'].values

        ''' Plot Net Profit Margin ratio from above on the y axis and the year on the x axis by useing the index from NetIncome which
            is the the year for all other data as well (NetIncome and TotalRevenu have the same data for year - could use either)'''
        plt.plot(balance_sheet_stk_1.loc['CurrentAssets'].index, liquidity_stk_1, marker='o')

        ''' Only implement the second plot if stock 1 is different than stock 2 meaning that operation
            type b was selected to compare 2 stocks in function_2 > project.py'''
        if stock_1 != stock_2:
            # same comments from stock 1 above apply ot the stock 2 below 3 lines
            balance_sheet_stk_2 = stk_2.get_balance_sheet()
            liquidity_stk_2 = (balance_sheet_stk_2.loc['CurrentAssets'].values - balance_sheet_stk_2.loc['Inventory'].values) / balance_sheet_stk_2.loc['CurrentLiabilities'].values

            plt.plot(balance_sheet_stk_2.loc['CurrentAssets'].index, liquidity_stk_2, marker='o')

        '''
        When stock_1 and stock_2 are the same, it means that operation a has been selected in function_2 >
        project.py to evaluate 1 stock - to select the appropriate plot title below
        '''
        if stock_1 == stock_2:
            # Create title for the plot with name of stock_1 only
            plt.title(f'Quick Ratio - {stock_1}')
            # Tilt x axis to avoid the years colliding
            plt.xticks(rotation=30)
            # Save file with name consists of ratio_stock_1
            plt.savefig(f'analysis/QuickRatio_<{stock_1}>.png')
            return f'QuickRatio_<{stock_1}>.png'

        '''
        Only implement the second plot if stock_1 is different than stock_2 meaning that operation type b was selected to compare
        2 stocks in function_2 > project.py - title to indicate both stocks and graph lines to be identified
        '''
        if stock_1 != stock_2:
            # Create title for the plot with both stock names
            plt.legend((stock_1, stock_2),
               loc='lower left')
            plt.title(f'Quick Ratio - {stock_1} vs {stock_2}')
            # Tilt x axis to avoid the years colliding
            plt.xticks(rotation=30)
            # Save file with name consists of ratio_stock1_VS_stock2
            plt.savefig(f'analysis/QuickRatio_<{stock_1}>vs<{stock_2}>.png')
            return f'QuickRatio_<{stock_1}>vs<{stock_2}>.png'


# Leverage - Debt-to-Equity (Total Liabilities / Stockholder Equity)
def lvg(stock_1, stock_2):
        # Get stock 1 & 2 and assign them to different variables
        stk_1 = yf.Ticker(stock_1)
        stk_2 = yf.Ticker(stock_2)

        # Change both stock symbols to upper letters
        stock_1 = stock_1.upper()
        stock_2 = stock_2.upper()

        # Plot style - Some styles to use >> default, ggplot, Solarize_Light2, seaborn-v0_8
        plt.style.use('ggplot')

        # Assign income statement for stock 1 to a variable
        balance_sheet_stk_1 = stk_1.get_balance_sheet()
        # Profitability - Net Profit Margin ratio for stock 1 by deviding Net Income by Total Revenu
        leverage_stk_1 = balance_sheet_stk_1.loc['TotalLiabilitiesNetMinorityInterest'].values/balance_sheet_stk_1.loc['StockholdersEquity'].values

        ''' Plot Net Profit Margin ratio from above on the y axis and the year on the x axis by useing the index from NetIncome which
            is the the year for all other data as well (NetIncome and TotalRevenu have the same data for year - could use either)'''
        plt.plot(balance_sheet_stk_1.loc['StockholdersEquity'].index, leverage_stk_1, marker='o')

        ''' Only implement the second plot if stock 1 is different than stock 2 meaning that operation
            type b was selected to compare 2 stocks in function_2 > project.py'''
        if stock_1 != stock_2:
            # same comments from stock 1 above apply ot the stock 2 below 3 lines
            balance_sheet_stk_2 = stk_2.get_balance_sheet()
            leverage_stk_2 = balance_sheet_stk_2.loc['TotalLiabilitiesNetMinorityInterest'].values/balance_sheet_stk_2.loc['StockholdersEquity'].values
            plt.plot(balance_sheet_stk_2.loc['StockholdersEquity'].index, leverage_stk_2, marker='o')

        '''
        When stock_1 and stock_2 are the same, it means that operation a has been selected in function_2 >
        project.py to evaluate 1 stock - to select the appropriate plot title below
        '''
        if stock_1 == stock_2:
            # Create title for the plot with name of stock_1 only
            plt.title(f'Debt-to-Equity - {stock_1}')
            # Tilt x axis to avoid the years colliding
            plt.xticks(rotation=30)
            # Save file with name consists of ratio_stock_1
            plt.savefig(f'analysis/DbtToEqty_<{stock_1}>.png')
            return f'DbtToEqty_<{stock_1}>.png'

        '''
        Only implement the second plot if stock_1 is different than stock_2 meaning that operation type b was selected to compare
        2 stocks in function_2 > project.py - title to indicate both stocks and graph lines to be identified
        '''
        if stock_1 != stock_2:
            # Create title for the plot with both stock names
            plt.legend((stock_1, stock_2),
               loc='lower left')
            plt.title(f'Debt-to-Equity - {stock_1} vs {stock_2}')
            # Tilt x axis to avoid the years colliding
            plt.xticks(rotation=30)
            # Save file with name consists of ratio_stock1_VS_stock2
            plt.savefig(f'analysis/DbtToEqty_<{stock_1}>vs<{stock_2}>.png')
            return f'DbtToEqty_<{stock_1}>vs<{stock_2}>.png'
