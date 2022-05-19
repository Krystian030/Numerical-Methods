from Macd import Macd
from LinearFunction import LinearFunction


class HolyGrail:

    def __init__(self, macd: Macd, startDay, period):
        self.macd = macd
        self.start = startDay
        self.end = startDay + period
        self.stocks = 1000
        self.startStock = 1000
        self.wallet = 0
        self.profitVal = 0
        self.currentDay = self.start
        self.lastBuy = self.currentDay
        self.lastSell = 0

    # funkcja wyświetlająca aktualną liczbę akcji i pieniędzy w portfelu oraz sumę tych wartości
    def printStat(self):
        print("=== DAY " + str(self.currentDay) + " ===")
        print("ALL: " + str(round(self.wallet + self.stocks * self.macd.samples[self.currentDay], 2)))
        print("STOCKS: " + str(round(self.stocks, 2)))
        print("WALLET: " + str(round(self.wallet, 2)))
        print()

    def printStatWithFlag(self, transaction):
        if transaction == 1:
            print("============ BUY ============")
            self.printStat()
        elif transaction == 2:
            print("============ SELL ============")
            self.printStat()

    # funkcja wyświetlająca zysk z algorytmu
    def profit(self):
        self.profitVal = (self.stocks * self.macd.samples[self.end - 1] + self.wallet) / (
                self.startStock * self.macd.samples[self.start]) * 100
        self.printStat()
        print("Profit: " + str(round(self.profitVal-100, 2)) + "%") # - 100 ponieważ chcemy policzyć procent zysku

    # algorytm podstawowy
    def basicAlgorithm(self, currentDay):
        if 0 <= currentDay - 1 <= len(self.macd.samples):
            macdLinear = LinearFunction([currentDay - 1, self.macd.macdIndicators[currentDay - 1]],  # Point A
                                        [currentDay, self.macd.macdIndicators[currentDay]])  # Point B

            signalLinear = LinearFunction([currentDay - 1, self.macd.signalIndicators[currentDay - 1]],  # Point A
                                          [currentDay, self.macd.signalIndicators[currentDay]])  # Point B

            currentValue = self.macd.samples[currentDay]

            buyIndicator = 0.001

            transaction = 0  # Transaction flag: 0 - None, 1 - Buy, 2 - Sell

            if macdLinear.isIntersectInRange(signalLinear):

                # MACD przecina SIGNAL od góry - sprzedaż akcji
                if macdLinear.isUpper(signalLinear):
                    if self.stocks > 0:
                        transaction = 2
                        self.wallet += self.stocks * currentValue
                        self.stocks = 0

                # MACD przecina SIGNAL od dołu - zakup akcji
                else:
                    if self.wallet >= (currentValue * buyIndicator):
                        transaction = 1
                        self.stocks = self.wallet / currentValue
                        self.wallet -= self.stocks * currentValue
                self.printStatWithFlag(transaction)

    # symulacja algorytmu
    def simulator(self, algorithm):
        print("======================== START ========================")
        self.printStat()
        for day in range(self.start, self.end):
            self.currentDay = day
            algorithm(day)
        print("======================== PROFIT ========================")
        self.profit()
        print("========================================================")
