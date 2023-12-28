# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  #missing brackets syntax error
# print "\n"      missing brackets and unknown variables and 1 tab in syntax error

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"      # == it isnt a mathematical equation so you only need 1 = sign
age = int(age_Str)  #years old from line 9 cant convert to integer run time error and wouldnt need this line
print("I'm " + str(age) + " years old.") #need to convert to str if you want to write it out

# Variables declaring additional years and printing the total years of age
years_from_now = int("3")
total_years = age + years_from_now

print("The total number of years:" + str(total_years)) #syntax error missing brackets concatenation is wrong
                                                        #and need to cast it run time error

# Variable to calculate the total amount of months from the total amount of years and printing the result
total = age + years_from_now
extra_months = int("6")
total_months = total * 12 +extra_months   #missing variable total run time error
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # syntax error

#HINT, 330 months is the correct answer

