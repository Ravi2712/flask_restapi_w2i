def wordsToInteger(userInput, wordsDict={}):

    if not wordsDict:
        units = [
                 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                 "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen",
                 ]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        # add words into dictionary
        wordsDict["negative"] = (-1, 0)
        for idx, word in enumerate(units):
            wordsDict[word] = (1, idx)
        for idx, word in enumerate(tens):
            wordsDict[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            wordsDict[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    isNegativeNumber = False
    for word in userInput.split("-"):
        if word not in wordsDict:
            print ("Not a valid word: " + word)

        # check for negative number
        if word == "negative":
            isNegativeNumber = True
            continue

        scale, increment = wordsDict[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return -1 * (result + current) if isNegativeNumber else result + current