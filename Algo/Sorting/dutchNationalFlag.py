
def dutchNationalFlag(balls: list[str]) -> list[str]:
    """Given an input array of characters R, G, B in random order,
    sort them to have R, G & B stacked together
    Ex: balls: ['R', 'B', 'G', 'G', 'R', 'R', 'B', 'B']
    output: ['R', 'R', 'R', 'G', 'G', 'B', 'B', 'B']

    Parameters
    ----------
    balls : list[str]
        Ex: balls: ['R', 'B', 'G', 'G', 'R', 'R', 'B', 'B']

    Returns
    -------
    list[str]
        create 3 partition of R, G and B
        output: ['R', 'R', 'R', 'G', 'G', 'B', 'B', 'B']
    """
    r, g = -1, -1
    for b in range(balls):
        if balls[b] == 'G':
            g += 1
            balls[b], balls[g] = balls[g], balls[b]
        elif balls[b] == 'R':
            g += 1
            balls[b], balls[g] = balls[g], balls[b]
            r += 1
            balls[g], balls[r] = balls[r], balls[g]
        else:  # balls[b] == 'B'
            # nothing needs to be done
            # for loop will increment value of b
    