
def main():
    var = raw_input("Please enter something: ")
    file = open(var, 'r')

    numList = []

    file.readline()
    solvedSat = file.readline()
    newLine = 0

    for i in solvedSat.split():
        num = int(i)
        if num > 0:
            newLine+=1
            realNum = num%9
            if realNum == 0:
                realNum = 9
            numList.append(realNum)
            if newLine%9 == 0:
                numList.append('\n')



    path = var.split('/')
    var = path[len(path)-1]
    var = var[:len(var)-4]
    output = open(var+"_solution.txt", 'w')
    for i in numList:
        output.write(str(i))

if __name__ == "__main__":
    main()