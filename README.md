# HBNB Command Interpreter

## Project Description
The HBNB Command Interpreter is a tool designed to interact with the backend storage system of a hypothetical AirBnB clone. It provides a command-line interface for managing objects stored in a JSON file-based database. Users can create, retrieve, update, and delete instances of various classes such as User, State, City, Place, Amenity, Review, etc.

## How to Start
To start the HBNB Command Interpreter, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the directory containing the `console.py` file.
3. Run the command `./console.py` to start the interpreter.

## How to Use
Once the interpreter is running, you can use the following commands:

- **quit**: Exit the program.
- **EOF**: Exit the program when End of File (EOF) is reached.
- **create \<class>**: Create a new instance of the specified class.
- **show \<class> \<id>**: Print the string representation of a specified instance.
- **destroy \<class> \<id>**: Delete an instance based on the class name and id.
- **all \<class>**: Print all string representations of instances for a given class.
- **update \<class> \<id> \<attribute> \<value>**: Update an instance based on the class name and id.

## Examples
- To create a new instance of the BaseModel class:
	(hbnb) create BaseModel

- To show the details of a specific instance:
	(hbnb) show BaseModel <instance_id>

- To update an attribute of an instance:
	(hbnb) update BaseModel <instance_id> name "New Name"


- To list all instances of a specific class:
	(hbnb) all BaseModel

- To delete an instance:
	(hbnb) destroy BaseModel <instance_id>

- To quit the interpreter:
	(hbnb) quit
