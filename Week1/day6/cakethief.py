def max_duffel_bag_value(types, capacity):
    """Takes a list of cake types (kg's, value) and bag capacity, returns maximum
        >>> cake_tuples = [(7, 160), (3, 90), (2, 15)]
        >>> capacity    = 20
        >>> steal_better(cake_tuples, capacity)
        555
        >>> cake_tuples = [(3, 40), (5, 70)]
        >>> capacity    = 9
        >>> steal_better(cake_tuples, capacity)
        120
    """

    # initialize a histogram of max values for each capacity
    max_values_at_n_capacity = [0] * (capacity + 1)

    # iterate over every stealable weight
    for stolen_weight in range(capacity + 1):

        # initialize max profit for output
        max_profit_at_weight = 0
        
        # iterate over cakes
        for kilo, price in types:

            if kilo <= stolen_weight:

                # for each stealable weight, calculate available weight left
                remaining_weight = stolen_weight - kilo

                # calculate max profit value at n weight capacity
                max_value_for_cake = (price +
                        max_values_at_n_capacity[remaining_weight])

                # pick the bigger value: running max or newly calculated max
                max_profit_at_weight = max(max_value_for_cake,
                                                    max_profit_at_weight)

        max_values_at_n_capacity[stolen_weight] = max_profit_at_weight



    return max_values_at_n_capacity[capacity]
