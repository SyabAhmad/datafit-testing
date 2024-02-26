import datafit.datafit as df 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filepath = {
    "path":"dataset/newData.csv",
    "delimiter": ",",
    }

data = pd.read_csv(filepath["path"],delimiter=filepath["delimiter"])

print(data.head(5))


##############################################################
### Checking Datafit package
### Below are the functions datafit can support
# df.check_and_resample()  -------------------------------------- Not Used
# df.deleteMultipleColumns() ----------------------------5
# df.extract_numeric_values() -------------------------6
# df.handleCategoricalData() -----------------------3
# df.information() ----------------------------1
# df.selectFeatures() ----------------------------4
# df.handlingNullValues() ----------------------2
# df.normalization()  ------------------------------------------- Not Used
# df.export() ------------------------------------- 8
# df.standardize() --------------------------7
# df.tokenize_text_values() ------------------------------------- Not Used
##############################################################



# to get information about data ----------------------- 1

df.information(data)

print("###########################################")

# to handle null values  ----------------------- 2

data = df.handlingNullValues(data)

df.information(data)


print("###########################################")

# to handle categorical values ----------------------- 3

data = df.handleCategoricalData(data,["allergenity","protienORdna"])

print(data.columns) # To get new name of the column that are just categorized

print(data[['allergenity_allergen', 'allergenity_nonallergen','protienORdna_ProtienSeq']])

print("###########################################")

# to delete multiple columns  ----------------------- 4

data = df.deleteMultipleColumns(data,["seq"])


print("###########################################")

# Selecting features  ----------------------- 5

data, column, _ = df.selectFeatures(data,["turn"])

print(data.columns)

print("###########################################")


# Extracting numerical values of data may have ----------------------- 6

data = df.extract_numeric_values(data,["beta_sheet"])

print(type(data["beta_sheet"]))


# standardization of data  ----------------------- 7

data , _ = df.standardize(data)

print(data.head(5))

print("###########################################")

# to export the processed data  ----------------------- 8
df.export(data)


