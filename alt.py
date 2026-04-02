import pandas as pd
import snappy
import ast

df = pd.read_csv("knotinfo.csv")
df = df[(df["Unknotting Number"].str.startswith("[1")) & (df["Alternating"] == "Y")]

df2 = pd.DataFrame(columns=["Name","Unknotting Number"])

def crossing_change(pd_code,i):
    # Given a PD code, we change the ith crossing
    # (indexing of i begining at 0)
    X = pd_code[i]
    if X[1]<X[3]:
        new_X = (X[1],X[2],X[3],X[0])
    elif X[1]>X[3]:
        new_X = (X[3],X[0],X[1],X[2])
    pd_code[i] = new_X
    return pd_code

def unknot_check(K):
    # We assume total_rank = 1 implies the knot K must be trivial
    K.simplify("global")
    if (int(K.knot_floer_homology()["total_rank"]) == 1):
        return True
    else:
        return False
    
def update_unknotting_val(row, found_unknot):
    
    Name = row["Name"]

    if found_unknot == True:
        df2.loc[len(df2)] = [Name, "1"]
    elif found_unknot == False:
        if row["Unknotting Number"] == "[1;2]":
            df2.loc[len(df2)] = [Name, "2"]
        else:
            # We modify the lower bound to be 2
            new_bounds = list(row["Unknotting Number"])
            new_bounds[1] = "2"
            new_bounds = "".join(new_bounds)
            df2.loc[len(df2)] = [Name, new_bounds]

            

for index, row in df.iterrows():
    found_unknot = False
    i = 0

    # We convert the knotinfo PD notation into an interable object
    pd_code = row["PD Notation"]
    pd_code = pd_code.replace(";",",")
    pd_code = ast.literal_eval(pd_code)

    # We iterate through each possible crossing change until we find an unknot
    while i < len(pd_code) and found_unknot == False:
        new_pd = crossing_change(pd_code,i)
        K = snappy.Link(new_pd)
        if unknot_check(K) == True:
            found_unknot = True
        i += 1

    update_unknotting_val(row, found_unknot)

df2.to_csv("updated_u(K)_values.csv", index=False)

unknotting_1 = len(df2[df2["Unknotting Number"] == "1"])
unknotting_2 = len(df2[df2["Unknotting Number"] == "2"])
bounds_improved = len(df2) - unknotting_1 - unknotting_2

print(f"Total Number of Knots Considered: {len(df2)}")
print(f"Number of Knots Determined to have Unknotting Number 1: {unknotting_1}")
print(f"Number of Knots Determined to have Unknotting Number 2: {unknotting_2}")
print(f"Number of Knots with Improved Unknotting Number Bounds: {bounds_improved}")
print("--------------------------------------------------------------------------------")    