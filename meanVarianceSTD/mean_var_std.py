import numpy as np

# DATA IS A LIST OF WITH 9 ELEMENTS = {LIST = [1,2,3,4,5,6,7,8,9]}
def calculate(list):
    numpyListArray = np.array(list)
    try:
        numpyListArray = numpyListArray.reshape((3,3))

        calculatorDict = {}
        dictionaryKeys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']

        dataMean = meanCalculator(numpyListArray)
        dataVariance= varianceCalculator(numpyListArray)
        
        dataStd =stdCalculator(numpyListArray)
        dataMax = maxCalculator(numpyListArray)
        
        dataMin = minCalculator(numpyListArray)
        dataSum = sumCalculator(numpyListArray)

        values = [dataMean, dataVariance,dataStd,dataMax,dataMin,dataSum]

        for i in range(len(dictionaryKeys)):
            calculatorDict[dictionaryKeys[i]] = values[i]
   
        print(calculatorDict)
        # calculations = list
    except ValueError:
        print("List must contain nine numbers.")
    return calculatorDict

# a numpy array 
def meanCalculator(numpyListArray):

    meanFlatten = np.mean(numpyListArray).flatten()
    meanAxis0 = np.mean(numpyListArray, axis = 0)
    meanAxis1 = np.mean(numpyListArray, axis = 1)
    meanList = [meanAxis0, meanAxis1, meanFlatten]
    return meanList 

def varianceCalculator(numpyListArray):

    varianceFlatten = np.var(numpyListArray).flatten()
    varianceAxis0 = np.var(numpyListArray, axis=0)
    varianceAxis1 = np.var(numpyListArray, axis=1)

    
    varianceList = [varianceAxis0, varianceAxis1, varianceFlatten]
    return varianceList
def stdCalculator(numpyListArray):

    stdFlatten =  np.std(numpyListArray).flatten  
    stdAxis0 =  np.std(numpyListArray, axis=0)
    stdAxis1 =  np.std(numpyListArray, axis=1)

    stdList = [stdAxis0, stdAxis1, stdFlatten]
    return stdList
def maxCalculator(numpyListArray):
    
    maxFlatten = np.max(numpyListArray).flatten  
    maxAxis0 = np.max(numpyListArray, axis=0)
    maxAxis1 = np.max(numpyListArray, axis=1)
    maxList = [maxAxis0, maxAxis1, maxFlatten]
    return maxList

def minCalculator(numpyListArray):


    minFlatten = np.min(numpyListArray).flatten
    minAxis0 = np.min(numpyListArray, axis=0)
    minAxis1 = np.min(numpyListArray, axis=1)
    
    minList = [minAxis0, minAxis1, minFlatten]
    return minList
def sumCalculator(numpyListArray):

    print(np.sum(numpyListArray).flatten())
    print(np.sum(numpyListArray, axis=0))
    print(np.sum(numpyListArray, axis=1),'\n')

    sumFlatten = np.sum(numpyListArray).flatten
    sumAxis0 = np.sum(numpyListArray, axis=0)
    sumAxis1 = np.sum(numpyListArray, axis=1)
    sumList = [sumAxis0, sumAxis1, sumFlatten]
    return sumList

