#This program asks the user for a product, its initial sales, expected growth rate,
#and the number of years of expected growth. It gives an output restating the input inserted by the user, an output in a table format
#that includes the sales growth for each year, and a final output with a summary description of the previous table
#that includes the total sales growth, total percentage growth, and total sales for the number of years that the user inserted. 

import sys

def main():
    
    #Declare and initialize variables
    product = ""
    flag = "N" #This is our input validation condition loop control variable
    initialSales = 0.00
    expectedGrowthRate = 0.00
    yearsGrowth = 0 #This will be our count loop control variable
    beginningSales = 0.00 #This variable will hold the data of initialSales variable(user input for initial sales)
    endingSales = 0.00
    growth = 0.00
    totalGrowth = 0.00
    totalSales = 0.00
    pause = ""
    
    #Get the Input
    print("\n\t\t\t---------------------------------------------")
    print("\t\t\t****Miller Company Sales Forecast Product****")
    print("\t\t\t---------------------------------------------")
    
    #This is the string input validation loop
    while (flag.upper() == "N"):
        product = str(input("\nWhat is the name of the product: "))
        print("\n\tYou have entered the product {0:s}".format(product))
        flag = str(input("\n\tIf this is not correct, please type n/N. Otherwise, hit any other key: "))
        
    #This is the exception handling loop for numeric inputs
    print("\n\t\t***ENTER ONLY NUMERIC INFORMATION IN ALL THE FOLLOWING PROMPTS***")
    while True:
        try:
            initialSales = float(input("\nEnter current annual sales for the product {0:s}: $".format(product)))
        except ValueError:
            print("\n\tYou have not entered a numeric value! Please, try again.")
            continue
        else:
            break
        
    while True:
        try:
            expectedGrowthRate = float(input("Enter expected annual growth rate (in decimal format such as 7% is .07): "))
        except ValueError:
            print("\n\tYou have not entered a numeric value! Please, try again.")
            continue
        else:
            break
        
    while True:
        try:
            yearsGrowth = int(input("Enter the number of years you want to project sales growth: "))
        except ValueError:
            print("\n\tYou have not entered a numeric value! Please, try again.")
            continue
        else:
            break
    if ((initialSales <= 0) or (expectedGrowthRate <= 0) or (yearsGrowth <= 0)):
        print("\n\tDATA ENTERED IS NOT CORRECT BECAUSE IT EITHER IS ZERO OR CONTAINS A NEGATIVE NUMBER!")
        print("\n\tPlease, try again.")
        main()
    else:
        #Processing and Output
        print("\n\n\n\t\t\t******{0:s} SALES INFORMATION******".format(product.upper()))
        
        #The below lines of code restate the input
        print("\n\tInitial sales: ${0:,.2f}".format(initialSales))
        print("\tNumber of years of expected growth: {0:d} years".format(yearsGrowth))
        print("\tInterest rate to calculate sales growth: {0:.1%}".format(expectedGrowthRate))
        
        #The following two lines of code are the headings of the sales table 
        print("\n\n\t{0:>5s}{1:>15s}{2:>18s}{3:>20s}".format("Year  ", "Beginning", "Growth","Ending  "))
        print("\t{0:>5s}{1:>15s}{2:>18s}{3:>20s}".format("", "Sales ", "","Sales  "))
        print("\t------------------------------------------------------------")

        #This line of code sets in the beginningSales variable the data stored in initialSales (user input).
        #This is needed because the initialSales variable gets changed in the loop, and its data gets lost.
        #In that way, the program can calculate the growth and ending sales for the first year, while also store the initial sales data(user input).
        
        beginningSales = initialSales
        
        #This for loop will display a table based on the years requested by the user
        for i in range (1, yearsGrowth + 1): #It means that starts with year 1 and finishes including the year inserted by the user
            
            growth = expectedGrowthRate * initialSales #This calculates the growth based on the beggining sales of each year
            totalGrowth += growth #This variable stores the total growth for all years and it will be used for the sales summary
            endingSales = initialSales + growth #This calculates the ending sales of each year
            totalSales += endingSales #This variable stores the total sales for all years and it will be used for the sales summary
             
            #The below line of code displays the content of the sales table
            print("\t{0:1s}{1:<5d}{2:15,.2f}{3:18,.2f}{4:20,.2f}".format("", i, initialSales, growth, endingSales))
            initialSales = endingSales #This line of code sets the ending sales as the initial sales,
                                       #so the program can loop and acurately calculate the next year of growth and ending sales
            
        #The below lines of code give the SALES SUMMARY for the total years that the user requested. 
        print("\n\n\tTotal sales growth for {0:d} years is: ${1:,.2f}".format(yearsGrowth, totalGrowth))
        #The below line of code displays the total percent growth of the initial sales in the years requested,
        #and it is calculated diving the total growth by initial sales. 
        print("\tPercent growth of initial ${0:,.2f} sales is: {1:.1%}".format(beginningSales, (totalGrowth/beginningSales))) 
        print("\tThe total amount of sales for the {0:d} years period is: ${1:,.2f}".format(yearsGrowth, totalSales)) 
        pause = str(input("\n\nHit enter to terminate the program: "))
        sys.exit()
        
main() 
