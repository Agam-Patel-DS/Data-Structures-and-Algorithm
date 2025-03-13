def maximum_profit(days):
    minSoFar=days[0]
    result=0

    for i in range(1,len(days)):
        minSoFar=min(minSoFar,days[i])

        result=max(result,days[i]-minSoFar)

    return result

days=[7,6,5,10,1]
print(f"The maximum profit can be: {maximum_profit(days)} in the given days.")