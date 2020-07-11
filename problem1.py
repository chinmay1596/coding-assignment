
#We have a string “input_str”, and input_str can be any alpha-numeric text with length of 10 to 10000. 

#Example of input_str:
#Input_str = “With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative.”

#We have another variable, an array of words called “validation_array”. It can have upto 1000 items. 

#Example of validation_array:
#Validation_array = [“food”, “face”, “donation”, “coalition”, “economy”, “sector”]

#We need to identify and print the output that the items in “validation_array” are occurring how many times in input_str. 

#Example:

#input_str = “With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative with a target of $2M in donation”

#validation_array = [“food”, “face”, “the”, “donation”, “coalition”, “economy”, “sector”]

#output:

#food: 1
#face: 1
#the: 6
#donation: 2
#coalition: 1
#economy: 1
#sector: 1

solution - 

Input_str = 'With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative with a target of $2M in donation”'

Validation_array = ["food", "face", "the", "donation", "coalition", "economy", "sector"]
l = Input_str.lower()

for i in Validation_array:
    s = l.count(i)
    print(i,':',s)



