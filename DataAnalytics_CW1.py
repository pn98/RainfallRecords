
class RainfallRecord:
    def __init__(self, year, month, temp_min, temp_max, average_fall, rainfall_value, sun_hours):
        self.year = year
        self.month = month
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.average_fall = average_fall
        self.rainfall_value = rainfall_value
        self.sun_hours = sun_hours
   

class Driver:
    def __init__(self):
        self.records = []

    def read_csv(self, filename):
            with open(filename) as f:            
                self.records = []
                for line in f:
                    self.records.append(RainfallRecord(*line.replace('\n', "").split(",")))
        
    def getRainfallRecords(self):
        return self.records

def return_driver(file_name):
    driver = Driver()
    driver.read_csv(file_name)
    return driver

""" rainfall takes as input a month and return the value of the rainfall in the given month of the year, and city. """
def rainfall(year, city):
    month = input("Enter the month: ")
    for record in city.getRainfallRecords():
        if record.year == year and record.month == month:
            return record.rainfall_value
    
    return "No rainfall data for the given month"


# this returns the average rainfall for the given months
def average_rainfall(year, city):
    months = input("Enter the months: ")
    months = months.split(" ")
    total = 0
    count = 0
    for record in city.getRainfallRecords():
        if record.year == year and record.month in months:
            if record.rainfall_value != "---":
                total += float(record.rainfall_value)
                count += 1

    if count == 0:
        return "No rainfall data for the given months"
    else:
        return total / count


# this deletes the rainfall record in the file but keeps the rest of the data
def delete(year, city, city_name):
    month = input("Enter the month: ")
    for record in city.getRainfallRecords():
        if record.year == year and record.month == month:
            record.rainfall_value = "---"

            with open(city_name, "w") as f:
                for record in city.getRainfallRecords():
                    f.write(record.year + "," + record.month + "," + record.temp_min + "," + record.temp_max + "," + record.average_fall + "," + record.rainfall_value + "," + record.sun_hours + "\n")
                
            return "Record deleted"
    
    return "No rainfall data for the given month"


# this updates the value that is already in the file
def insert(year, city, city_name):
    month = input("Enter the month: ")
    rainfall_value = input("Enter the rainfall value: ")
    for record in city.getRainfallRecords():
        if record.year == year and record.month == month:
            record.rainfall_value = rainfall_value

            with open(city_name, "w") as f:
                for record in city.getRainfallRecords():
                    f.write(record.year + "," + record.month + "," + record.temp_min + "," + record.temp_max + "," + record.average_fall + "," + record.rainfall_value + "," + record.sun_hours + "\n")

            return "Record updated"
    
    return "No rainfall data for the given month"

# this inserts the value based on the season that is inputted
def insert_quarter(year, city, city_name):
    try:
        print("1. Winter (December, January, February)")
        print("2. Spring (March, April, May)")
        print("3. Summer (June, July, August)")
        print("4. Autumn (September, October, November)")
        season_input = int(input("Enter the season (i.e. 1-4): "))
        if season_input == 1:
            season = [12, 1, 2]
        elif season_input == 2:
            season = [3, 4, 5]
        elif season_input == 3:
            season = [6, 7, 8]
        elif season_input == 4:
            season = [9, 10, 11]
        else:
            print("Invalid season. Please enter a number between 1 and 4")
            return 0
    except ValueError:
        print("Invalid season. Please enter a number between 1 and 4")
        return 0

    for month in season:
        rainfall_value = input("Enter the rainfall value for month " + str(month) + ": ")
        for record in city.getRainfallRecords():
            if record.year == year and record.month == str(month):
                record.rainfall_value = rainfall_value
                with open(city_name, "w") as f:
                    for record in city.getRainfallRecords():
                        f.write(record.year + "," + record.month + "," + record.temp_min + "," + record.temp_max + "," + record.average_fall + "," + record.rainfall_value + "," + record.sun_hours + "\n")
    
    return "Record updated"


class Archive:
    def __init__(self, records=None, city=None):
        self.records = records
        self.city = city

    # this deletes the whole value that is already in the file
    def delete(self, year, city):
        month = input("Enter the month: ")
        for record in city.getRainfallRecords():
            if record.year == year and record.month == month:
                city.getRainfallRecords().remove(record)

                with open("Oxford.csv", "w") as f:
                    for record in city.getRainfallRecords():
                        f.write(record.year + "," + record.month + "," + record.temp_min + "," + record.temp_max + "," + record.average_fall + "," + record.rainfall_value + "," + record.sun_hours + "\n")
                
                return "Record deleted"
        
        return "No rainfall data for the given month"
    
    # this inserts a whole record
    def insert(self, year, city, city_name):
        month = input("Enter the month: ")
        rainfall_value = input("Enter the rainfall value: ")
        for record in city.getRainfallRecords():
            if record.year == year and record.month == month:
                city.getRainfallRecords().remove(record)
        
        city.getRainfallRecords().append(RainfallRecord(year, month, "---", "---", "---", rainfall_value, "---"))
        
        city.getRainfallRecords().sort(key=lambda x: (x.year, x.month))

        with open(city_name, "w") as f:
            for record in city.getRainfallRecords():
                f.write(record.year + "," + record.month + "," + record.temp_min + "," + record.temp_max + "," + record.average_fall + "," + record.rainfall_value + "," + record.sun_hours + "\n")

        return "Record inserted"

    # Simple Moving Average that takes as inputs a city, a year one, a year two, and a number of months k to return the k months moving averages of rainfall over that city from year one to year two.
    def moving_average(self, city, year_one, year_two, k):
        if k > 12:
            return "Invalid number of months"
        if int(year_one) > int(year_two):
            return "Invalid year range"
        if int(year_one) == int(year_two):
            return "Invalid year range"

        for record in city.getRainfallRecords():
            if record.year == year_one and record.month == "1":
                start = city.getRainfallRecords().index(record)
            if record.year == year_two and record.month == "12":
                end = city.getRainfallRecords().index(record)

        moving_averages = []
        for i in range(start, end - k + 2):
            this_window = city.getRainfallRecords()[i:i+k]
            window_average = sum(float(record.rainfall_value) for record in this_window) / k
            moving_averages.append(window_average)

        return moving_averages



if __name__ == "__main__":

    while True:
# This takes the input city from the user, if the city is not listed under 'cities' then "invalid city" will be printed.
        cities = ["Oxford", "Aberporth", "Armagh"]
        city = input("Enter the city: ")

        if city not in cities:
            print("Invalid city")
            exit()
        driver = return_driver(city + ".csv")

        year = input("Enter the year: ")
# This will print the following if the city entered is one of the 'cities'.
        while True:
            print("Current city: " + city)
            print("Current year: " + year)
            print("--------------------")
            print("1. Return rainfall record")
            print("2. Update rainfall record")
            print("3. Delete rainfall record")
            print("4. Delete record from database")
            print("5. Calculate average rainfall")
            print("6. Insert record to database")
            print("7. Simple Moving Average")
            print("8. Insert Quarter")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                print(rainfall(year, driver))
            elif choice == "2":
                print(insert(year, driver, city + ".csv"))
            elif choice == "3":
                print(delete(year, driver, city + ".csv"))
            elif choice == "4":
                print(Archive().delete(year, driver))
            elif choice == "5":
                print(average_rainfall(year, driver))
            elif choice == "6":
                print(Archive().insert(year, driver, city + ".csv"))
            elif choice == "7":
                print(Archive().moving_average(driver, input("Enter the first year: "), input("Enter the second year: "), int(input("Enter the number of months: "))))
            elif choice == "8":
                print(insert_quarter(year, driver, city + ".csv"))
            elif choice == "9":
                break
            else:
                print("Invalid choice")
        