class User:

    def __init__(self, userId: int):
        self.userId = userId
        self.check = [] 
    
    def checkIn(self, checkIn: int, name: str):
        self.check.append((checkIn, name))
    
    def checkOut(self, checkOut: int):
        time, name = self.check.pop()
        val = checkOut - time
        return (val, name)

class Station:

    def __init__(self, name: str):
        self.name = name
        self.distinctTime = {}
    
    def pushTime(self, time: int, name:str):
        if name not in self.distinctTime:
            self.distinctTime[name] = [time]
            return
        self.distinctTime[name].append(time)
    
    def getAvg(self, name: str):
        if name not in self.distinctTime:
            return 0
        return sum(self.distinctTime[name])/len(self.distinctTime[name])

class UndergroundSystem:

    def __init__(self):
        self.user = {}
        self.station = {}
    
    def validateUser(self,id: int):
        if id not in self.user:
            self.user[id] = User(id)
    def validateStation(self, name: str):
        if name not in self.station:
            self.station[name] = Station(name)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.validateUser(id)
        self.validateStation(stationName)

        self.user[id].checkIn(t, stationName)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.validateUser(id)
        self.validateStation(stationName)
        time, name = self.user[id].checkOut(t)
        self.station[stationName].pushTime(time, name)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        return self.station[endStation].getAvg(startStation)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)