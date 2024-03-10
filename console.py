#!/usr/bin/python3
"""Console module for HBNB project."""
import cmd
import re
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models import storage


def tokenize_arguments(arg):
    """
    Tokenizes the arguments in the given string.

    Args:
        arg (str): The string containing arguments.

    Returns:
        list: A list of tokens extracted from the string.
    """
    curly_match = re.search(r"\{(.*?)\}", arg)
    bracket_match = re.search(r"\[(.*?)\]", arg)

    if curly_match is None:
        if bracket_match is None:
            return [token.strip(",") for token in split(arg)]
        else:
            tokens_before_bracket = split(arg[:bracket_match.span()[0]])
            token_list = [token.strip(",") for token in tokens_before_bracket]
            token_list.append(bracket_match.group())
            return token_list
    else:
        tokens_before_curly = split(arg[:curly_match.span()[0]])
        token_list = [token.strip(",") for token in tokens_before_curly]
        token_list.append(curly_match.group())
        return token_list


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "
    classes = {
            "BaseModel", "User", "State",
            "City", "Place", "Amenity", "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Print help message for the quit command."""
        print("Quit command to exit the program")
        print("")

    def do_EOF(self, arg):
        """Exit the program when End of File (EOF) is reached."""
        print("")
        return True

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        command_mapping = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }

        dot_match = re.search(r"\.", arg)

        if dot_match is not None:
            start_index = dot_match.span()[0]
            end_index = dot_match.span()[1]
            command_parts = [arg[:start_index], arg[end_index:]]

            paren_match = re.search(r"\((.*?)\)", command_parts[1])

            if paren_match is not None:
                command_arg_start = command_parts[1][:paren_match.span()[0]]
                command_arg_content = paren_match.group()[1:-1]
                command_args = [command_arg_start, command_arg_content]

                if command_args[0] in command_mapping.keys():
                    updated_command = (
                            "{} {}".format(command_parts[0], command_args[1])
                            )
                    return command_mapping[command_args[0]](updated_command)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        arg_list = tokenize_arguments(arg)

        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg_list[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Print the string representation of an instance."""
        
        arg_list = tokenize_arguments(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = arg_list[0] + '.' + arg_list[1] 
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        arg_list = tokenize_arguments(arg)
        key = arg_list[0] + '.' + arg_list[1] 
        all_objs = storage.all()
        if not arg:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif key not in all_objs.keys():
            print("** no instance found **")
        else:
            del all_objs[key]
            storage.save()

    def do_all(self, arg):
        """Print all string representations of instances."""
        arg_list = tokenize_arguments(arg)
        all_objs = storage.all()
        if arg_list and arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in all_objs.values():
                if arg_list and arg_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)
    
    def do_count(self, arg):
        """Count the number of instances of a class."""
        arg_list = tokenize_arguments(arg)
        count = 0

        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        arg_list = tokenize_arguments(arg)
        all_objs = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False

        instance_key = "{}.{}".format(arg_list[0], arg_list[1])
        if instance_key not in all_objs.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            obj = all_objs[instance_key]
            if arg_list[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = val_type(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = all_objs[instance_key]
            for attr_name, attr_value in eval(arg_list[2]).items():
                if (attr_name in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[attr_name]) in
                        {str, int, float}):
                    val_type = type(obj.__class__.__dict__[attr_name])
                    obj.__dict__[attr_name] = val_type(attr_value)
                else:
                    obj.__dict__[attr_name] = attr_value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
