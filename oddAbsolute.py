def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    iTarget = 21
    # print("target :", iTarget)
    iNumber = int(in_num)
    # print("iNumber raw :", iNumber)
    bBigNumber = iNumber > iTarget
    # if bBigNumber:
    #     print("iNumber is greather than 21")
    # else:
    #     print("iNumber is less than 21")
    absNumber = abs(iNumber)
    # print("absolute iNumber :", absNumber)
    test = iTarget - iNumber
    # print("test :", test)
    absTest = abs(test)
    # print("absTest :", absTest)
    if bBigNumber:
        absTest += absTest
    print("Result:", absTest)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateAbsolute()