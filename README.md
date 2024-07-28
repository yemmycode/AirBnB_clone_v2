# HBNB - The Console

This repository contains the initial stage of a project to build a clone of the AirBnB website, implementing a backend console interface to manage data.

## Repository Contents by Project Task

| Tasks                 | Files                                                                                     | Description                                                       |
|-----------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| 0: Authors/README     | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS)                 | Project authors                                                   |
| 1: Pep8               | N/A                                                                                       | All code is pep8 compliant                                        |
| 2: Unit Testing       | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests)                    | All class-defining modules are unit tested                        |
| 3. Make BaseModel     | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes        |
| 4. Update BaseModel   | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance from a dictionary        |
| 5. Create FileStorage | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Defines a class to manage persistent file storage system           |
| 6. Console 0.0.1      | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py)           | Add basic console functionality (quit, handle empty lines, ^D)    |
| 7. Console 0.1        | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py)           | Update console with methods to create, destroy, show, and update  |
| 8. Create User class  | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Implement user class dynamically |
| 9. More Classes       | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) | Implement more classes dynamically |
| 10. Console 1.0       | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py)           | Update console and file storage to work dynamically with all classes |

## General Use

1. Clone the repository. 2. Navigate to the directory and run the console:

/AirBnB_clone$ ./console.py

3. The prompt `(hbnb)` will appear. Available commands: - `create`: Creates an instance based on given class - `destroy`: Destroys an object based on class and UUID - `show`: Shows an object based on class and UUID - `all`: Shows all objects or all objects of a given class - `update`: Updates existing attributes of an object - `quit`: Exits the program

### Alternative Syntax
- Commands can also be issued in an alternative syntax:

<class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])

## Examples

### Primary Command Syntax

- **Create an object**

(hbnb) create BaseModel

- **Show an object**

(hbnb) show BaseModel <id>

- **Destroy an object**

(hbnb) destroy BaseModel <id>

- **Update an object**
(hbnb) update BaseModel <id> <attribute_name> <attribute_value>

### Alternative Syntax

- **Show all User objects**

(hbnb) User.all()

- **Destroy a User**
(hbnb) User.destroy("<id>")

- **Update User by attribute**
(hbnb) User.update("<id>", name "Todd the Toad")

- **Update User by dictionary**
(hbnb) User.update("<id>", {'name': 'Fred the Frog', 'age': 9})

