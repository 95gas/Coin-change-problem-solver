import timeit

#****************************************
#*********** BACKTRACKING ***************
#****************************************

# Function to find the minimum list of coins to get a change of `N` from an
# limited supply of coins in set `list_coins`
def bk(change, return_coins):

    global best_return_coins
    global size
    global list_coins
    global N
    global N_combination

    for i in range(len(list_coins)):

        curr_coin = list_coins[i]
        return_coins.append(curr_coin)
        change = change - curr_coin

        #Consider only the elements that can lead to a best solution
        if change >= 0 :

            #candidate solution found
            if change == 0:

                #print all the possible combinations
                N_combination = N_combination + 1
                print("Combination #", N_combination," ", return_coins)

                #update best solutions
                if len(return_coins) <= size:
                    best_return_coins = return_coins[:]
                    size = len(best_return_coins)

            else:
                bk(change, return_coins)

        #backtrack step
        return_coins.pop()
        change = change + curr_coin


# Optimized backtracking function
def bkOpt(change, return_coins):

    global best_return_coins
    global size
    global list_coins
    global N
    global N_combination

    for i in range(len(list_coins)):

        curr_coin = list_coins[i]
        return_coins.append(curr_coin)
        change = change - curr_coin

        #Consider only the elements that can lead to a best solution
        if change >= 0 and len(return_coins) <= size:

            #candidate solution found
            if change == 0:

                #print all the possible combinations
                N_combination = N_combination + 1
                print("Combination #", N_combination," ", return_coins)

                #update best solutions
                best_return_coins = return_coins[:]
                size = len(best_return_coins)

            else:
                bkOpt(change, return_coins)

        #backtrack step
        return_coins.pop()
        change = change + curr_coin



#********************************************
#********** DYNAMIC PROGRAMMING *************
#********************************************

def NBP(S,N):
# initialization of the array
  store = [0]*(N+1)

# start dynamic programming algorithm
  return RLMMO_dyn(S, N, store)

def RLMMO_dyn(S, N, storeMin):

# If change = 0
  if N==0:
    # No coins to give back
    return 0

# if the last item in the array is positive
  elif storeMin[N]>0:
    # return it
    return storeMin[N]

# else search for the miminum coins
  else:
	# init minimum
    minimum = 9000

    for i in range(len(S)):

    # if a new ways is found
      if S[i]<=N:
        #increment number of ways (combinations)
        nbWays= 1 + RLMMO_dyn(S, N-S[i], storeMin)

        # if it is the best one
        if nbWays<minimum:
        # update minimum
          minimum = nbWays
          storeMin[N] = minimum

  return minimum



#****************************************
#**************** GREEDY ****************
#****************************************

# Function to find the the best way to get a change of N
def greedy(change, start, return_coins):

    global list_coins

    #clean-up phase: find the next candidates for the next choice
    while (change < list_coins[start]): #find the next coin
      start = start + 1

    coin = list_coins[start] #greedy choice
    return_coins.append(coin)
    change = change - coin

    if change == 0:
        return #stop recursion

    greedy(change, start, return_coins)




#main function
if __name__ == '__main__':
    print("*******************************************************************************")
    print("************************* COING CHANGE PROBLEM SOLVER *************************")
    print("*******************************************************************************")

    print("") #newline
    #global variable to count the number of combinations
    N_combination=0


    #select the list of coin to use
    print("SELECT THE SET OF COINS:")
    print("a : [200, 100, 50, 20, 10, 5, 2, 1]")
    print("b : [50, 30, 10, 5, 3, 1]")
    print("c : [9, 6, 5, 1]")
    print("d : [6, 4, 1]")
    print("Set: ", end='')
    choice = str(input())

    list_coins = []

    if choice == 'a':
        print("--> Set chosen : [200, 100, 50, 20, 10, 5, 2, 1]")
        list_coins = [200, 100, 50, 20, 10, 5, 2, 1]
    elif choice == 'b':
        print("--> Set chosen : [50, 30, 10, 5, 3, 1]")
        list_coins = [50, 30, 10, 5, 3, 1]
    elif choice == 'c':
        print("--> Set chosen : [9, 6, 5, 1]")
        list_coins = [9, 6, 5, 1]
    elif choice == 'd':
        print("--> Set chosen : [6, 4, 1]")
        list_coins = [6, 4, 1]


    # total change required
    print("\nINSERT THE VALUE OF THE CHANGE (ex. 100 for 1€): ", end='')
    N = int(input())

    #select problem solver

    print("\nSELECT THE PROBLEM SOLVER TO USE:")
    print("a : Backtracking")
    print("b : Dynamic programming (return only the number of coins)")
    print("c : Greedy")
    print("\nChoice: ", end='')
    choice = str(input())

    #BACKTRACKING
    if choice == 'a':
        print("\n--> Problem solver chosen : Backtracking")
        print("START BACKTRACKING PROGRAM\n")


        # These variables are going to be used by the backtracking function to compute the solution
        return_coins = []
        best_return_coins = []
        size = 100000000


        start = timeit.default_timer() #start timer

        bkOpt(N, return_coins)

        #bk(N, return_coins)

        stop = timeit.default_timer() #stop timer
        #Print results
        print("\nThe best way to give back the change: ", N, " is: ", best_return_coins)
        print('Time (in seconds): ', stop - start)
        print("END program")

    #DYNAMIC PROGRAMMING
    elif choice == 'b':
        print("--> Problem solver chosen : Dynamic programming")
        print("\nSTART DYNAMIC PROGRAMMING PROGRAM")


        start = timeit.default_timer() #start timer

        result = NBP(list_coins, N)

        stop = timeit.default_timer() #stop timer

        #Print results
        print("\nThe minimum number of coins to give back for the change", N, "is: ", result)
        print('Time (in seconds): ', stop - start)
        print("END program")


    #GREEDY
    elif choice == 'c':

        print("--> Problem solver chosen : Greedy")
        print("\nSTART GREEDY PROGRAM")



            #declare variables for the function
        return_coins = []
        indexStart = 0

        start = timeit.default_timer() #start timer

        greedy(N, indexStart, return_coins)

        stop = timeit.default_timer() #stop timer

        #Print results
        print("\nThe best way to give back change", N,  "is: ", return_coins)
        print('Time (in seconds): ', stop - start)
        print("End program")
