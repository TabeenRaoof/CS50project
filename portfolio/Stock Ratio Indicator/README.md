# Stock Ratio Indicator
#### Video Demo:  <https://youtu.be/DNMXujgOBfs>
---
#### Description: This program will evaluate four fundamental stock ratios. It will allow the user to select between two types of operations: evaluate one stock or compare two different stocks. The user will then be prompted to select the stock ticker/s. Once the stocks are selected, the program will prompt the user to also select one of the four different ratios available. The the output is four years of data fro the selected ratio presented on a graph.

### The program uses Yahoo Finance API (yfinance) to get the stock company information. The project is devided into two main files:


### 1)  project.py: contains the main functions that prompts the user for the inputs and checks for the correctness of the input. This file imports the ratios from the ratios.py

### Functions

Main():

Main primarily starts the program by calling type_of_operation() function
One important factor to point out is that this function will call the select_stock(opt_type) function in two different ways based on the operation type that the user selected:
- If operation type 'a' has been selected, the function will return the same stock symbol twice as stock_1 and stock_2 because all ratio function imported from ratios.py take two parameters
- If operation type 'b' was selected, the function will return the two stock symbols to the select_stock(opt_type) function


type_of_operation():
- Prompt User to input a type of operation
- The function will prompt the user until a valid selection has been made
- Does not take any parameters


select_stock(opt_type):
- Run one of two operations from input of the first function type_of_operation() > based on the operation type, the function will either require the user to input 1 or 2 stock symbols
- This function checks if the stock symbol is correct by runnign the Net Income through the API - any other financial info should work so long as it's a valid operation.
- This function takes one parameter > type_of_operation


select_ratio(stock_1, stock_2):
- Assign the stock/s added by user to one of the functions from ratios.py
- The function will prompt the user until a valid selection has been made
- The ratio inputscheck the validity of the output before running the function because some stocks may not have a cetrain parameter of the ratio in certain times and the function will run into an error



### 2) ratios.py: contains the four different ratio functions that utilized by project.py. The functions will create a png file that plots the ratio on a graph. All functions take two parameters (2 stocks).


### Functions and Design Choices

The functions in ratios.py are similar in design. They all take two stocks in parameters and plot either one or two stocks on the graph
- The functions distinguish between an input of one stock or two stocks by comparing the two stock inputs > if they are the same stocks symbols, this means that operation 'a' has been selected, otherwise two stocks have been selected and operation 'b' was selected. This design choice was because this method does not require too many checking and just by comparing the two symbols, we can distinguish which operation type was selected. Refer to the explanation of Main() function above for the detials on how the symbols are returned to the ratio functions
- Based on the distinction made by the above, if one stock is selected, the stock will be plotted on the graph once and the second operation for stock_2 will be inactivated with an if conditional. Otherwise, if there are two distinct stocks, the conditional finction will make the second plot active and stock_2 will be plotted on the graph.


Other Files:
- test_project.py is a file to test the three functions in the project.py file.
- requirements.py contains required pip install files

## Executing program

Run the program with 'python project.py'


### Step One)

The user will be asked to select one of the operations below:

    'a' To evaluate one stock
---
    'b' To compare two stocks

If any input is added other than 'a' or 'b', the program will keep promting the user


### Step Two)

    If operation type 'a' is selected, the user will be requested to add one stock symbol. Example input = 'cost'
---
    If operation type 'b' is selected, the user will be requested to add two stock symbols. Example input = 'cost' and then 'wmt'

If the user adds an incorrect stock symbol (i.e. any symbol that is not recognized by Yahoo Finance), the user will be informed that the stock is incorrect and reprompted to add a correct stock symbol


### Step Three)

The user will be prompted to select one of the ratios below to evaluate the stock:

    a) Profitability - Net Profit Margin
---
    b) Leverage - Debt-to-Equity
---
    c) Return on Equity
---
    d) Liquidity - Quick ratio


in case of any input other than the above letters, the user will be informed that the input is incorrect and prompted again to select one of the above

### Step Four)

The output will be saved as a png file named 'stk_ratio.png'

    In case of operation type 'a', the one stock ratio will be presented on the graph to evaluate
---
    In case of operation type 'b', both stock ratios will be presented on the same graph to compare



# Collaborators

### Tabeen Raoof

---
---

## Important Note - Disclaimer

Please note that this program is not intended to use for making financial or investment dicisions. This is a prototype and not a final product.
If used, this  should only be complimentary and a small part of extensive analysis an research on any company that you decide to invest in. Even then, this tool must not be used to finalize a financial decision or prefer a company over another in any shape of form. If this tool is used to complement your decisions, you are totally taking responsibility of your decisions.
---
