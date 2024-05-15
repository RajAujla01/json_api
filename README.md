# JSON and APIs

## JSON

### What does it stand for?
JavaScript Object Notation

### What is it used for?
Storing and exchanging data between a server and a web application. It's commonly used for APIs (Application Programming Interfaces) to transfer data.

## What is it written in?
It is not really code. It is more like text. 

### What data types can it store/use?
* Strings (text) 
* Numbers 
* Booleans (true/false)
* Nulls
* Arrays (lists)
* Objects (collections of name/value pairs)

### What is the JSON syntax for:
- Name value pairs?

```
"name": "value"
```

- Objects?
An object is enclosed within curly braces { }, with name/value pairs separated by commas
```
{
    "name": "Ray",
    "age": 39,
    "isStudent": false
}
```

- How to separate data objects from one another?
Data objects are separated by commas when they appear within arrays or in a list of objects
```
{
    "name": "Ray",
    "age": 39,
    "isStudent": false
} , 
{
    "name": "Roxy",
    "age": 30,
    "isStudent": true
}
```

- JSON arrays (these are like lists in python)?
Arrays are enclosed within square brackets [ ], with elements separated by commas.
```
["apple", "banana", "orange"]
```