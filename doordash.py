def test():
    cars =["dodge","lambo","cybertruck","audi","porsche"]
    print(cars)
    print(len(cars))
    print(cars[4])
    print(cars[1:4])
    cars[0]="toyota"
    cars.append("ford")
    cars.insert(3,"BMW")
    sports_cars=["corvette","mclaren","lexus","ferrari"]
    cars.extend(sports_cars)
    cars.remove("lexus")
    cars.pop(4)    
test()