def arithmetic_coding_encode(message, source_information):
    intervals = {}
    sum = 0
    for symbol, prob in source_information.items():
        intervals[symbol] = [sum, sum + prob]
        sum = intervals[symbol][1]

    print(f"Initial intervals: {intervals}")

    for i, symbol in enumerate(message):
        intervals = update_intervals(source_information, intervals, symbol)
        print(f"Intervals after {i+1} symbol: {intervals}")

    code = next(iter(intervals.items()))[1][0]

    return code


def update_intervals(source_information, intervals, symbol):
    new_lower_bound = intervals[symbol][0]
    new_upper_bound = intervals[symbol][1]

    new_intervals = {}

    sum = new_lower_bound
    for s, interval in intervals.items():
        new_intervals[s] = [
            sum,
            sum + (new_upper_bound - new_lower_bound) * source_information[s],
        ]
        sum = new_intervals[s][1]

    return new_intervals


source_information = {"A": 0.2, "B": 0.3, "C": 0.5}

print("The source information with the given probabilities is: ")
for symbol, prob in source_information.items():
    print(f"p({symbol}) = {prob}")

message = "CACBCC"
print(f"The message is: {message}")

code = arithmetic_coding_encode(message, source_information)

print(f"The code for the message is: {code}")
