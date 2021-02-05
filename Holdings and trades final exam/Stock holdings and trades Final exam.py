####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
###
###
### Type your name here: Erik Stroud
###
##
## Look at the function main below to see how these functions are used
##
##
## Complete the functions below as directed in the docstring comments
##
##
## I will test your code by running the main function defined below.
##
##Obviously, as you write each function, you can test it individually
##using the Python shell
##
##
def initialize_portfolio(filename): #8 points
    """
    read the data contained in the named file
    and return a *list of tuples* representing the data
    For example: [('DD', 1085),('DIS', 1213), ('GE', 1781), ('GS',1913),......]
    """
    #Open the file that will be used to create list
    file = open(filename, 'r')
    newList = []

    #iterate over each line of the file
    for eachLine in file:

        #strip and split the file into values needed
        eachLine.strip()
        symbol, stocks = eachLine.split(',')

        #create the tuple with values and append it to the list
        newTuple = (symbol,int(stocks))
        newList.append(newTuple)
        
    return newList

def print_portfolio(portfolio):  #8 points
    """
    Print the contents of the portfolio in a two-column format as shown below
    The first line is a header
    All the other lines show a stock symbol, and the number of shares
    held of that stock, with a tab "\t" character separating the two,
    like this:
    Symbol    Amount
    DIS       1213
    GE        1781
    GS        1913
    .....
    This function does not return anything
    """

    #print the beginning of the table
    print("Symbol\tAmount")

    #iterates over the list provided and prints the data in the format needed
    for i in portfolio:
        print(i[0],'\t'+str(i[1]))
        
    pass

def total_shares(portfolio): #8 points
    """
    return the total number of shares owned (across all stocks) in the portfolio
    """
    #initialize total to 0
    total = 0

    #iterate over portfolio and add the value in the location to total
    for i in portfolio:
        total += i[1]
    return total


def find_amount(portfolio, stock_symbol): #8 points
    """
    return the number of shares of the specified stock in the portfolio
    for example, find_amount(portfolio, "DIS") returns 1213
    """
    
    #iterate over the portfolio and finds the symbol
    for i in portfolio:

        #Once the symbol is found, return the value held within the same tuple
        if i[0] == stock_symbol:
            return i[1]
    return 0


def update_portfolio(portfolio, filename): # 8 points
    """
    Open the specified file, read the transactions in it,
    and update the portfolio accordingly
    Return the updated portfolio
    """

    #open the file and create empty list
    file = open(filename,'r')
    actionList = []

    #iterate over each line in the file
    for line in file:

        #strip, split, and append the data to previously created list
        line.strip()
        action, symbol, amount = line.split(',')
        actionList.append([action, symbol, int(amount)])

    #create 2 more empty list for use
    editPort = []
    updatePort = []

    #convert and add the data from portfolio to the editList in order to change values
    for tup in portfolio:
        editPort.append(list(tup))

    #iterate over actionlist to determine what will be added/subtracted
    for i in actionList:
        if i[0] == "Buy":

            #iterate over editPort and add amount that was bought
            for share in editPort:
                if share[0] == i[1]:
                    share[1] += i[2]
        if i[0] == "Sell":

            #iterate over editPort and subtract amount that was sold
            for share in editPort:
                if share[0] == i[1]:
                    share[1] -= i[2]

    #set iterate over editPort and add each list within to updatePort as a tuple
    #done to return a matching data structure 
    for shareList in editPort:
        updatePort.append(tuple(shareList))
    
                
                    
    return updatePort
    

#DO NOT MAKE ANY CHANGES TO THE main FUNCTION BELOW
#DO NOT MAKE ANY CHANGES TO THE main FUNCTION BELOW
def main():
    try:
        portfolio = initialize_portfolio("holdings.txt")
    except:
        print(">>>>>>>> initialize_portfolio has errors")

    print("\nHere is your portfolio before any trades\n")
    
    try:
        print_portfolio(portfolio)
    except:
        print(">>>>>>>> print_portfolio has errors")
        
    try:
        print("\nThe total number of shares in the portfolio is ", total_shares(portfolio))
    except:
        print(">>>>>>>> total_shares has errors")
        
    symbol = input("\nEnter a stock symbol(like IBM): ")

    try:
        print("\nBefore any trades, you hold ", find_amount(portfolio, symbol)," shares of ", symbol)
    except:
        print(">>>>>>>> find_amount has errors")

    try:
        portfolio = update_portfolio(portfolio, "trades.txt")
    except:
        print(">>>>>>>> update_portfolio has errors")
        
    print("\nHere is your portfolio after trades\n")
    
    try:
        print_portfolio(portfolio)
    except:
        print(">>>>>>>> print_portfolio has errors")
    
    symbol = input("\nEnter a stock symbol(like IBM): ")
    
    try:
        print("\nAfter trades, you hold ", find_amount(portfolio, symbol)," shares of ", symbol)
    except:
        print(">>>>>>>>> find_amount has errors")


#Run the main function     
main()
