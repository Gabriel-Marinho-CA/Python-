
is_male = True
is_tall =  False


if is_male or is_tall:
    print("U are a male or tall or both")

if is_male and is_tall:
    print("U are a male or tall or both")

elif is_male and not (is_tall): #else if
    print("U are a short male")

elif not(is_male) and is_tall:
    print("U are not male but are tall")

else:   
    print("U're neither not ")
