def can_invest (plec, wiek, poziomzdolnosci):
    if wiek<18 or poziomzdolnosci== "Don't even try, beggar":
        return print ("nie mozesz inwestowac")
    if wiek>18 and( poziomzdolnosci== "Invest in gold" or poziomzdolnosci== "Invest in diamonds"  or poziomzdolnosci== "Invest in palacyki" ):
        return print("inwestuj")
