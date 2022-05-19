from Macd import Macd
from HolyGrail import HolyGrail
import datetime

if __name__ == '__main__':
    macd = Macd(1000, "eurpln")

    macd.readData()
    simulator = HolyGrail(macd, 400, 201)
    simulator.simulator(simulator.basicAlgorithm)
