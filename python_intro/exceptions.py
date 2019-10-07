#  full syntax
try:
    print(1 / 0)
except (TypeError, ZeroDivisionError) as e:
    print(e)

#  not obligatory
else:
    print("continue")
finally:
    print("always")
