import csv
import sys

#Create main execution sub
#parameters: Analytics engine, datasource, targetfields, includedfields, model key



#def main(AnalyticsEngine, DataSource, TargetFields, IncludedFields, ModelKey):

def main(DataSource):

    

    #Eventual HyperHyperparameters
    #NumberOfFolds = 5
    #OptimizationIterations = 1
    #UndersamplingPercentage = 100
    #OversamplingPercentage = 0
    #ObjectiveFunction = New TotalErrorClassificationMetric()


    #Generate Dataset from CSV
    with open(DataSource) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(row)


    #Process/Clean Dataset



    #Train Model



    #Test Model



    #Generate Statistics



    #Train Final Model



    #Compress Final Model



    #Store Results



if __name__ == '__main__':
    main(sys.argv[1])
