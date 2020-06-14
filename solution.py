def snail(snail_map):
    final = []

    while len(snail_map) > 0:
        final += snail_map[0]
        del snail_map[0]

        if len(snail_map) > 0:
            for i in snail_map:
                final += [i[-1]]
                i.pop()

            if snail_map[-1]:
                final += snail_map[-1][::-1]
                snail_map.pop()

            for i in reversed(snail_map):
                final += [i[0]]
                del i[0]

    return final
