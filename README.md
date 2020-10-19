
# EPAI Session 11 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Module".  We have used the timer decorator created in earlier session to time the function calls. We have session10.pynb file to check the logs of functions

# Below are key functions in session10.py file.

### A) Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings)

### 1.create_fake_library_by_namedtuple
Generates a database of fake profiles based on user input.
for example create_fake_library_by_namedtuple(10) will return named tuple of 10 named tuple of fake profiles

### 2. largest_bg
Return the most common blood group of fake profiles stored as named tuple of named tuple

### 3. mean_current_location
Return the mean current location ( average lat and long co-ordinates) of fake profiles stored in named tuple of named tuple

### 4. oldest_person_age
Return the oldest person's age of fake profiles stored in named tuple of named tuple

### 5. average_age
Return the oldest person's age of fake profiles stored in named tuple of named tuple

### B) Use Faker library to get 10000 random profiles. Using dictionary, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings)
### 6. create_fake_library_by_dict
Generates a database of fake profiles based on user input for example create_fake_library_by_dict(10) will return dictionary of 10 dictionary of fake profiles

### 7. largest_bg_dict
Return the most common blood group of fake profiles stored in dictionary of dictionary

### 8. mean_current_location_dict
Return the mean current location ( average lat and long co-ordinates) of fake profiles stored in dictionary of dictionary

### 9. oldest_person_age_dict
Return the oldest person's age of fake profiles stored in dictionary of dictionary

### 10. average_age_dict
Return the oldest person's age of fake profiles stored in dictionary of dictionary

### 11. compare_time
function to compare the performance of named tuple vs dict. Function takes input as fake profiles library implemented as named tuple of named tuple and dictionary of dictionary. For named tuples based libraries, it runs and time 100 iterations of function named largest_bg, mean_current_location, oldest_person_age,  average_age and add it to a timer variable. It repeates the same for library implemented as dictionary of dictionary while timing the 100 times execution of each of largest_bg, mean_current_location,        oldest_person_age, average_age and storing it in another timer variable.
Finally it compares the timing as based on it prints the winner as well as returns both timer variables

### C) Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random.

### 12. create_stock_exchange
function to create fake company profiles and list them on a fake stock exchange.
Function follows the following steps
        *1. Function generates the a class  for named tuple and then
        generates a random weights in the named tuple
        *2. Take the sum of all weights to generate a named tuple of
        normalized weights
        *3. Create class for named tuple for a company with fields as
        'company_name', 'symbol', 'value', 'open', 'high', 'low', 'close'
        *4. Company Name: Create named tuple class for stock exchange
        *5. in loop get the fake company name by faker
        *6. Symbol: Generate the symbol of company by selection first letter and
        last letters of the company name while randomly choosing the middle
        letter while making sure its not a special character
        *7. Value: Randomly select the value of company between 3000 to 5000
        *8. Open: Companies contribution can be found as normalized weight * value
        *9. High: Open multiple with random value between .8 to 1.3
        *10. Low: Low can be from .5 multiple with open to high value for that company on a given day
        *11. Close: Close can be any number between Low and High including them

### 13. stock_exchange_details
Calculate the days open, low, high and closing for stock exchange. Loops through the tuples of top 100 companies listed in exchange and returns on calculation, the day_open, day_high, day_low and day_close value for exchange

# Below are test cases functions in test_session10.py file.

## Check for coding standards-

## 1. test_readme_exists :
Test for readme exists

## 2. test_readme_contents :
Test for readme contents are more than 500 words

## 3. test_readme_proper_description :
Test for all important functions/class described well in your README.md file

## 4. test_readme_file_for_formatting :
Test for readme formatting

## 5. test_indentations :
Test for source code formatting. No tabs but four spaces are used for indentation

## 6. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

# Test cases for assignments

## 7. test_compare_perforamce:
Test to check the performance of named tuple is better than dictionary

## 8. test_doc_string:
Test to check the doc string exists

## 9. test_stock_exchange :
Test to check the stock exchange numbers are correct
