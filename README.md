# Airport Passenger Management System

This program simulates a simplified airport system where passengers, luggage, and flights are managed on a world board represented as a grid. The goal is to create an airport board with airports, passengers, luggage, and their elements, then process check-ins and flights, ensuring all rules regarding luggage weight and flight availability are followed. The task was part of the **Introduction to Programming** course in the second semester of 2019, as a **first-year Civil Engineering** student at **Pontificia Universidad Católica de Chile**.

## Table of Contents
- [Airport Passenger Management System](#airport-passenger-management-system)
  - [Table of Contents](#table-of-contents)
  - [Problem Context](#problem-context)
  - [Classes](#classes)
  - [Program Execution](#program-execution)
    - [Prerequisites](#prerequisites)
    - [How to Run](#how-to-run)
    - [Input Format](#input-format)
  - [Sample Input and Output](#sample-input-and-output)
    - [Sample Input](#sample-input)
    - [Sample Output](#sample-output)
    - [Execution Examples](#execution-examples)
  - [Conclusion](#conclusion)

---

## Problem Context

The program simulates the following:
1. The creation of an airport board, which is a 2D grid.
2. Instantiation of airports, passengers, luggage, and luggage elements.
3. Passengers are associated with their luggage, and each luggage contains elements that have weight.
4. Airports have a maximum allowed luggage weight, and passengers can only check in if they can fly from the airport to their destination and if their luggage complies with the weight restrictions.
5. The program processes the check-in, adjusts luggage weights if necessary, and simulates passengers traveling from their origin to their destination.

---

## Classes

The program contains the following classes:
- **`Aeropuerto`**: Represents an airport. Each airport has a name, maximum allowed luggage weight, and a list of destination airports.
- **`Pasajero`**: Represents a passenger. Each passenger has a name, age, origin, and destination.
- **`Maleta`**: Represents a passenger's luggage, which has a color and a list of elements.
- **`Elemento`**: Represents an item in the luggage with a name and weight.

The interaction between these classes is what defines the airport operations, such as check-in, luggage processing, and flight simulation.

---

## Program Execution

To execute the program, you will need to run the `main.py` file, which processes inputs for the airports, passengers, and their luggage. Follow these steps to run the program:

### Prerequisites

- Python 3.x installed.

### How to Run

1. Clone or download the repository containing the `main.py` file.
2. Execute the program with the following command in your terminal:

```bash
   python3 main.py
```

4. The program will process the input and display the results in the terminal, including the final state of the airport board.

### Input Format

1. Board Size
The first line of input is a string representing the dimensions of the board:

```
x,y
```

Where x represents the number of columns, and y the number of rows.

2. Airports
The second line is a string of airport names, their max allowed luggage weight, and a list of possible destinations for each airport:

```
airport_name_1,max_weight_1,destination_1_1,destination_1_2;airport_name_2,max_weight_2,destination_2_1,destination_2_2;...;airport_name_n,max_weight_n,destination_n_1,destination_n_2
```

3. Passengers
The third line is a string of passengers with their names, ages, origin, and destination:

```
name_1,age_1,origin_1,destination_1;name_2,age_2,origin_2,destination_2;...;name_n,age_n,origin_n,destination_n
```

4. Luggage and Elements
Subsequent lines define passengers' luggage and elements:

```
owner_name,color
item_1,weight_1;item_2,weight_2;...;item_n,weight_n
```

5. Airport Positions

The final input line is a string representing the positions of airports on the board:

```
name_1,x_1,y_1;name_2,x_2,y_2;...;name_n,x_n,y_n
```

## Sample Input and Output

### Sample Input

```
2,2
Vanuatu,18,Armenia;Armenia,20,Vanuatu
Monica,26,Vanuatu,Armenia
1
Monica,Amarillo
Sombrero,4.0;Toalla,5.0;Pantalones,0.5;Chalas,3.5;Calcetines,2
Vanuatu,0,1;Armenia,1,0
```

### Sample Output

```
Monica hizo check-in en el aeropuerto Vanuatu
Se ha ingresado la maleta de peso 15.0
[Sombrero, Toalla, Pantalones, Chalas, Calcetines]
```

### Execution Examples

The output will simulate the check-in process, and print the final state of passengers and luggage.

## Conclusion

This project was developed for the Introduction to Programming course during my first year as a Civil Engineering student at the Pontificia Universidad Católica de Chile in the second semester of 2019. It showcases object-oriented programming concepts such as class design, input parsing, and simulation of real-world processes.