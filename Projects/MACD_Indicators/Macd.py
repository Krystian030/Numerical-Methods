import csv
import sys
from LinearFunction import LinearFunction


class Macd:
    samples = []
    macdIndicators = []
    signalIndicators = []
    intersectionPoints = []
    macdLinearFunctions = []
    signalLinearFunctions = []

    def __init__(self, samplesCount, fileName):
        self.samplesCount = samplesCount  # number of samples
        self.fileName = fileName
        self.readData()
        self.macdManagment()
        self.countIntersectionPoints(self.samplesCount)

    # funkcja odczytująca dane
    def readData(self):
        path = "./Data/" + self.fileName + ".csv"
        with open(path) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            try:
                counter = 0
                max = 1000
                next(reader)  # first row is header
                for row in reader:
                    if counter < max:
                        self.samples.append(float(row[4]))  # 0 - Data, 1 - Open, 2 - the highest, 3 - the lowest, 4 - closed (using this value), 5 - Volume
                        counter += 1
                    else:
                        break
            except csv.Error as e:
                sys.exit(e)

    # funkcja zapisująca dane
    def writeData(self, indicators, type):
        path = "./Files/" + self.fileName + "_" + type + ".csv"
        with open(path, mode='w', encoding='UTF8', newline='') as csvFile:
            try:
                if type != "MACD_INDICATORS" and type != "SIGNAL_INDICATORS":
                    writer = csv.writer(csvFile)
                    dates = indicators
                    for i in range(len(dates)):
                        writer.writerow([dates[i][0], dates[i][1]])
                else:
                    writer = csv.writer(csvFile, delimiter='\n')
                    writer.writerows([indicators])
            except csv.Error as e:
                sys.exit(e)


    # wyliczanie średniej kroczącej
    def emaCalc(self, period, current, series):
        alpha = 2 / (period + 1)
        component = 1 - alpha
        ema = 0
        denominator = 0
        for i in range(period + 1):
            if current - i >= 0:
                ema += series[current - i] * (component ** i)
                denominator += component ** i
            else:
                break
        return ema / denominator

    # wyliczanie MACD
    def macdManagment(self):
        for current in range(self.samplesCount):
            ema12 = self.emaCalc(12, current, self.samples)
            ema26 = self.emaCalc(26, current, self.samples)

            self.macdIndicators.append((ema12 - ema26))

            ema9 = self.emaCalc(9, current, self.macdIndicators)
            self.signalIndicators.append(ema9)

        self.writeData(self.macdIndicators, "MACD_INDICATORS")
        self.writeData(self.signalIndicators, "SIGNAL_INDICATORS")

    # wyliczanie punktów przecięcia
    def countIntersectionPoints(self, dateTo):

        for i in range(0, self.samplesCount):

            macdLinear = None
            signalLinear = None
            date = i
            if i - 1 >= 0 and date <= dateTo:
                macdLinear = LinearFunction([i - 1, self.macdIndicators[i - 1]], [i, self.macdIndicators[i]])
                signalLinear = LinearFunction([i - 1, self.signalIndicators[i - 1]], [i, self.signalIndicators[i]])

                X = macdLinear.intersection(signalLinear)

                if (i - 1) <= X[0] <= i:
                    self.intersectionPoints.append([X[0], X[1]])

            self.macdLinearFunctions.append(macdLinear)
            self.signalLinearFunctions.append(signalLinear)

        self.writeData(self.intersectionPoints, "INTERSECTION_POINTS")
