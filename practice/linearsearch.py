
def linear_search(n, item):
    index = -1
    for i in range(len(n)):
        if n[i] == item:
            index = i
            break

    return index


print(linear_search([1,2,3,4,5], 3))

print(linear_search([1,2,3,4,5], 6))