# CLI Unit Converter


# cm to inches
def cm_inches(item):
    toInches = item * 0.0039370079
    return f"{toInches:.2f}"

# mm to inches
def mm_inches(item):
    toInches = item * 0.0003937008
    return  f"{toInches:.2f}"



print(cm_inches(10))
    