a = 1  # int
b = 1.0  # float
c = "1"  # string, char not exists
d = True  # boolean, -1 is true as well, False - 0 or empty object
e = [1, "2"]  # list, e[-1] -> last element from the list
f = e  # assign/copy reference to the list, not new object
g = list(e)  # create new object with the same value
f[1] = 3
g[0] = 3
print(e, f, g)
h = (1, 2)  # tuple (krotka :) -> immutable
i = {  # dict, key/value pairs, value can be e.g. another dict
    "1": {
        "jeden": "one"
    }
}
