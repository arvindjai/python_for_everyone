import pandas

datasets = {
    "people" : ["Tall", "medium", "short"],
    "passing" : [3, 7, 2]
}

myvar = pandas.DataFrame(datasets)

print(myvar)