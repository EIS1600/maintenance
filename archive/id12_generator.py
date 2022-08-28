from random import randint
def generate12IDs(iterations):
    IDs = []
    for i in range(0, iterations):
        IDs.append(str(randint(400000000000, 999999999999)))
    IDs = list(set(IDs))
    print("IDs: {:,}".format(len(IDs)))
    return(IDs)

ids = generate12IDs(1000000)

print(len(ids))