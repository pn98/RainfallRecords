# RainfallRecords

Classes:
RainfallRecord: This is a single record of rainfall information that includes sun hours, average rainfall, value, minimum and maximum temperatures, and year.
Driver: Oversees an assortment of RainfallRecord occurrences. One way to read data from a CSV file is included.
Archive: This is a representation of a city's rainfall records archive. It offers operations for adding, removing, and calculating a basic moving average.

Functions:
return_driver(file_name): Reads data from the given CSV file to create and return a Driver instance.
rainfall(year, city): This function asks the user to select a month and then returns the amount of rainfall that month in the specified year and city. It accepts a year and a city as input.
average_rainfall(year, city): This function asks the user to select months and then computes the average rainfall for those months within the entered year and city.
delete(year, city, city_name): This function accepts as inputs a Driver instance, a year, and a city name. The user is prompted for a month, after which the rainfall record for that month in the specified year and city is deleted.
insert(year, city, city_name) requires a driver instance, a city name, and a year.

Main Execution: A main execution block in the code asks the user to enter a city and year repeatedly. The user can then choose from a menu of options to carry out different operations related to rainfall records for the selected city and year. Viewing, editing, removing, and adding records are among the options. You can also compute averages and run a basic moving average.

Notes: It is assumed by the programme that rainfall data is kept in CSV files with city names appended to them, such as "Oxford.csv".
It appears that the Archive class offers more capabilities for archiving records and figuring out a basic moving average.
The user enters corresponding numbers to make choices through a text-based user interface.
