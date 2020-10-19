"""Assignment for session 10 based on Tuples and Named Tuples"""
from faker import Faker
from collections import namedtuple
from collections import Counter
from datetime import datetime
import random
import math
import re

# - Utility Code -
# TODO: Timer decorator to time functions with number of iterations
def timer_factory(repeat):
    """
    decorator factory to create a decorator.
    Inputs:
        repaet: number of times the decorated function will be called
    Returns:
        time_it: decorator
    """
    def time_it(func):
        """
        decorator function called to decorate a function by timing it.
        Inputs:
            func: name of function which has to be timed ( will be free variable)
        Returns:
            time_it: function
        """
        from time import perf_counter
        from functools import wraps
        # Check for a valid  function is passed to create a decorator
        if not hasattr(func, '__call__'):
            raise NameError(f"{func} is not a valid function")

        @wraps(func)
        def timer(*args, **kwargs):
            """
            find average time to execute a function while running it for n times.
            # Inputs:
                *args: positioned parameters
                **kwargs: named parameters
            # Returns:
                Returns output of function func(*args,**kwargs)

            # Functionality:
                Function check's how much time it takes on an average for n runs to execute a function

            For eg: after decorating fact function for repeat = 100, we will get how much time it takes for
            fact function to run for any given inputs on an average for 100 runs. In this case we will get -
            fact(5)
            Function fact takes average run time of 2.3930000179461787e-06 for 100 iterations
            """
            total_elapsed = 0
            for i in range(repeat):
                start = perf_counter()
                result = func(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / repeat
            print(f'Function {func.__name__} takes average run time of {avg_run_time} for {repeat} iterations')
            return result, avg_run_time
        return timer
    return time_it

# TODO: 1. Use Faker library to get 10000 random profiles. Using namedtuple,
# calculate the largest blood type, mean-current_location, oldest_person_age
#  and average age (add proper doc-strings)
def create_fake_library_by_namedtuple(num):
    """
    function to create fake profiles library
    # Inputs:
        num: Number of profiles in library
    # Returns:
        faker_db:  Fake profiles database of
        Named tuple of named tuples with
        required number for profiles

    # Functionality:
        Generates a database of fake profiles
        based on user input for example
        create_fake_library_by_namedtuple(10)
        will return named tupel of 10 named
        tuple of fake profiles
    """
    # Create faker instance
    fake = Faker()

    # Get a dummy fake profile
    dummy = fake.profile()

    # Create a namedtuple class
    FakePrf = namedtuple('FakePrf', dummy.keys())

    # Overwrite doc string
    FakePrf.__doc__ = "Represents random fake profile"

    # Create a namedtuple class for fake profiles db
    FakePrfDb = namedtuple('FakePrfDb', 'FakePrf_0')

    for i in range(num):
        # get a fake profile
        f_prfl = fake.profile()

        # Create tuple from namedtuple class to store the f_prfl
        fake_profile = FakePrf(**f_prfl)


        # Add profile to Fake Profile DB
        if i==0:
            faker_db = FakePrfDb(fake_profile)
        else:
            FakePrfDb = namedtuple('FakePrfDb', FakePrfDb._fields + ('FakePrf_'+str(i),))

            # Overwrite doc string
            FakePrfDb.__doc__ = f"Represents database of {num} random fake profile"

            faker_db = FakePrfDb._make(faker_db + (fake_profile,))

    return(faker_db)

#TODO: 1.1 #  Calculate the largest blood type
@timer_factory(100)
def largest_bg(faker_db):
    """
    Return the most common blood group
    of fake profile db as named tuple
    """
    count = len(faker_db)
    bl_grp = []
    for i in range(count):
        bl_grp.append(faker_db[i][5])
    return Counter(bl_grp).most_common(1)[0][0]

#TODO 1.2 # Calculate mean-current_location
@timer_factory(100)
def mean_current_location(faker_db):
    """
    Return the mean-current_location
    of fake profile db as named tuple
    """
    count = len(faker_db)
    lat = []
    long = []
    for i in range(count):
        lat.append(faker_db[i][4][0])
        long.append(faker_db[i][4][1])
    return sum(lat)/count,sum(long)/count

#TODO 1.3 # Calulate oldest person's age
@timer_factory(100)
def oldest_person_age(faker_db):
    """
    Return the oldest person's age
    of fake profile db as named tuple
    """
    size = len(faker_db)
    age = []
    days_in_year = 365.2425
    today = datetime.date(datetime.today())
    for i in range(size):
        age.append((today - faker_db[i][12]).days / days_in_year)
    return max(age)

#TODO 1.4 # Calculate average age
@timer_factory(100)
def average_age(faker_db):
    """
    Return the average age
    of fake profile db as named tuple
    """
    count = len(faker_db)
    age = []
    days_in_year = 365.2425
    today = datetime.date(datetime.today())
    for i in range(count):
        age.append((today - faker_db[i][12]).days / days_in_year)
    return sum(age)/count

# TODO: 2. Use Faker library to get 10000 random profiles. Using dictionary,
# calculate the largest blood type, mean-current_location, oldest_person_age
#  and average age (add proper doc-strings)
def create_fake_library_by_dict(num):
    """
    function to create fake profiles library
    # Inputs:
        num: Number of profiles in library
    # Returns:
        faker_db_dict:  Fake profiles database of
        dictionary of dictionary with
        required number for profiles

    # Functionality:
        Generates a database of fake profiles
        based on user input for example
        create_fake_library_by_dict(10)
        will return dictionary of 10 dictionary
        of fake profiles
    """

    # Create faker instance
    fake = Faker()

    # Create a fake profile DB dictonary object
    faker_db_dict = {}

    for i in range(num):
        # get a fake profile
        f_prfl = fake.profile()

        # prepare next key
        key = 'fk_pr_' + str(i+1)

        # Add profile to Fake Profile DB
        faker_db_dict[key] = f_prfl

    return(faker_db_dict)

# TODO: 2.1: Calculate the largest blood type
@timer_factory(100)
def largest_bg_dict(faker_db_dict):
    """
    Return the most common blood group for
    fake profile db as dictionary
    """
    count = len(faker_db_dict)
    bl_grp = []
    for i in range(count):
        key = 'fk_pr_' + str(i+1)
        bl_grp.append(faker_db_dict[key]['blood_group'])
    return Counter(bl_grp).most_common(1)[0][0]


# TODO: 2.2:  Calculate mean-current_location
@timer_factory(100)
def mean_current_location_dict(faker_db_dict):
    """
    Return the mean-current_location
    of fake profile db as dictionary
    """
    count = len(faker_db_dict)
    lat = []
    long = []
    for i in range(count):
        key = 'fk_pr_' + str(i+1)
        lat.append(faker_db_dict[key]['current_location'][0])
        long.append(faker_db_dict[key]['current_location'][1])
    return sum(lat)/count,sum(long)/count

# TODO: 2.3: Calculate oldest person's age
@timer_factory(100)
def oldest_person_age_dict(faker_db_dict):
    """
    Return the oldest person's age
    of fake profile db as dictionary
    """
    size = len(faker_db_dict)
    age = []
    days_in_year = 365.2425
    today = datetime.date(datetime.today())
    for i in range(size):
        key = 'fk_pr_' + str(i+1)
        age.append((today - faker_db_dict[key]['birthdate']).days / days_in_year)
    return max(age)

# TODO: 2.4: Calculate average age
@timer_factory(100)
def average_age_dict(faker_db_dict):
    """
    Return the average age
    of fake profile db as dictionary
    """
    count = len(faker_db_dict)
    age = []
    days_in_year = 365.2425
    today = datetime.date(datetime.today())
    for i in range(count):
        key = 'fk_pr_' + str(i+1)
        age.append((today - faker_db_dict[key]['birthdate']).days / days_in_year)
    return sum(age)/count

# TODO: 2.5 # Compare the Named Tuple Vs Dict Performance
def compare_time(nt_db, dict_db):
    """
    function to compare the performance
    of named tuple vs dict
    # Inputs:
        nt_db: profile database implemented
        as named_tuple of named tuples

        dict: profile datebase implemented
        as dictionary of dictionary
    # Returns:
        nt_timer: Sum of average time taken
        for the exectuion of multiple
        iterations of functions using named
        tuple based profile DB

        dict_timer: Sum of average time taken
        for the exectuion of multiple
        iterations of functions using dictionary
        based profile DB

    # Functionality:
        Function takes input as fake profiles library implemented as
        named tuple of named tuple and dictionary of dictionary.
        for named tuples based libraries, it runs and time 100 iterations of
        function named largest_bg,mean_current_location,oldest_person_age,average_age
        and add it to a timer variable.
        It repeates the same for library implemenetd as dictionary of dictinary while
        timing the 100 times exection of each of largest_bg,mean_current_location,
        oldest_person_age,average_age and storing it in another timer variable.
        Finally it compares the timing as based on it prints the winner as well as
        returns both timer variables
    """
    nt_func_list = [largest_bg,mean_current_location,oldest_person_age,average_age]
    nt_timer = 0
    for i in range(len(nt_func_list)):
        _, time = nt_func_list[i](nt_db)
        nt_timer += time

    print('\n',"========================")

    dict_func_list = [largest_bg_dict,mean_current_location_dict,oldest_person_age_dict,average_age_dict]
    dict_timer = 0
    for i in range(len(dict_func_list)):
        _, time = dict_func_list[i](dict_db)
        dict_timer += time

    print('\n',"========================")
    print(f"{'Named Tuple'if dict_timer > nt_timer else 'Dictionory'} performed {round(dict_timer/nt_timer) if dict_timer > nt_timer else round(nt_timer/dict_timer)} times faster")
    print('\n',"========================")

    return(nt_timer, dict_timer)

# TODO: 3. Create a fake data (you can use Faker for company names) for imaginary
# stock exchange for top 100 companies (name, symbol, open, high, close). Assign
# a random weight to all the companies. Calculate and show what value stock market
# started at, what was the highest value during the day and where did it end.
# Make sure your open, high, close are not totally random.
def create_stock_exchange(num_of_listed_comp = 100):
    """
    function to create fake company profiles and list
    them on a fake stock exchange.
    # Inputs:
        num_of_listed_comp: Number of top companies to
        be listed in stock exchage
    # Returns:
        stock_exchange:  Stock exchange implemened as
        named tuple with top fake companies with their
        company name, symbol, value, open, high, low and
        closing values as a named tuple

    # Functionality:
        Function follows the following steps
        1. Function generates the a class  for named tuple and then
        generates a random weights in the named tuple
        2. Take the sum of all weights to generate a named tuple of
        normalised weights
        3. Create class for named tuple for a company with fields as
        'company_name', 'symbol', 'value', 'open', 'high', 'low', 'close'
        4. Company Name: Create named tuple class for stock exchange
        5. in loop get the fake company name by faker
        6. Symbol: Generate the symbol of company by selection first letter and
        last letters of the company name while randomly chosing the middle
        letter while making sure its not a special charcater
        7. Value: Randomly select the value of company between 3000 to 5000
        8. Open: Companies contribution can be found as normalized weight * value
        9. High: Open*random value between .8 to 1.3
        10. Low: Low can be from .5*open to high value for that company on a given day
        11. Close: Close can be any number between Low and High including them

    """
    # Create a named tuple to store 100 random weights
    Weights = namedtuple('Weights', ['wgt'+str(i) for i in range(num_of_listed_comp)])

    weight = Weights(*[round(random.random(),2) for _ in range(num_of_listed_comp)])

    wght_sum = sum(weight)

    # Create a named tuple for normalized weights
    norm_weight = Weights(*[wght/wght_sum for wght in weight])

    # Sum is 1, hence we got the normalized weights
    assert round(sum(norm_weight),2) == 1

    # Create a namedtuple class for a company
    FakeComp = namedtuple('FakeComp', ['company_name', 'symbol', 'value', 'open', 'high', 'low', 'close'])

    FakeComp.__doc__ = "Represents a fake company"

    # Create a namedtuple class for a fake Stock Exchange
    StkXchange = namedtuple('StkXchange', 'fake_comp_0')

    StkXchange.__doc__ = "Represents a fake stock exchange"

    # Create faker instance
    fake = Faker()

    # Create fake companies and stock exchange
    for i in range(num_of_listed_comp):
        # Company name
        comp_name = fake.company()
        # Symbol
        symbol = comp_name[0].upper() + random.choice(re.sub('\W+','', comp_name[1:-1])).upper() + comp_name[-1].upper()
        # Value
        value = random.randint(3000,5000)
        # Open_
        open_ = round(value*norm_weight[i],2)
        # High
        high = round(open_*(random.randint(80,130)/100),2)
        # Low
        low = random.randint(math.floor(open_*100*.5),math.floor(high*100))/100
        # Close
        close = random.randint(math.floor(low*100),math.floor(high*100))/100

        # Create Fake Company
        fake_comp = FakeComp(comp_name,symbol,value, open_,high,low,close)
        # List the Fake company in Fake stock exchange
        if i==0:
            stock_exchange = StkXchange(fake_comp)
        else:
            StkXchange = namedtuple('StkXchange', StkXchange._fields + ('fake_comp_'+str(i),))

            stock_exchange = StkXchange._make(stock_exchange + (fake_comp,))

    return(stock_exchange)

# TODO 3.1: Calculate the days open, low, high and closing for stock exchange
def stock_exchange_details(stock_exchange):
    """
    Returns stock exchange details
    # Inputs:
        stock_exchange: Input the named tuple for stock exchange
    # Returns:
        day_open: Opening index value for exchange
        day_high: Highest achieved index value for exchange
        day_low:  Lowest index value for exchange
        day_close: Closing index value for exchange
    # Functionality:
        loops through the tuples of top 100 companies
        listed in exchange and returns on calculation,
        the day_open, day_high, day_low and day_close
        value for exchange
    """
    day_open=0
    day_high=0
    day_low=0
    day_close=0
    for i in range(100):
        day_open  += stock_exchange[i].open
        day_high  += stock_exchange[i].high
        day_low   += stock_exchange[i].low
        day_close += stock_exchange[i].close

    return(round(day_open,2),round(day_high,2),round(day_low,2),round(day_close,2))
