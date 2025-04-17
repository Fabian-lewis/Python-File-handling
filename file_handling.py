# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.


def open_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return None

    
def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except IOError:
        print(f"Error: The file '{filename}' could not be written to.")
        return None
    

def modify_content(content):
    to_replace = input("Enter the text you want to replace: ")
    replacement = input("Enter the replacement text: ")
    modified_content = content.replace(to_replace, replacement)
    return modified_content


def print_menu():
    print("=============================================")
    print("      Welcome to the File Read & Write Tool      ")
    print("=============================================\n")

    print("{:<10} {:<30}".format("Option", "Description"))
    print("-" * 40)
    print("{:<10} {:<30}".format("1", "Read a file"))
    print("{:<10} {:<30}".format("2", "Write to a file"))
    print("{:<10} {:<30}".format("3", "Modify content of a file"))
    print("{:<10} {:<30}".format("4", "Exit"))
    print()



def main():
    # Print the menu
    print_menu()

    # Get the option from the user
    option = input("Enter your option (Input the option number): ")

    try:
        option = int(option)
        if(option < 1 or option > 4):
            print("Invalid option. Please enter a number between 1 and 4.")
            return main()
        if option == 1:
            filename = input("Enter the name of the file to read: ")
            content = open_file(filename)
            if content:
                print("File content:")
                print(content)

            # Ask the user if they want to perfomr another action
            continue_answer = input("Do you want to read another file or perform another action? (yes/no): ").strip().lower()
            if continue_answer == 'yes':
                return main()
            else:
                print("Exiting the program. Goodbye!")
                return None
            
        elif option == 2:
            filename = input("Enter the name of the file to write to: ")
            content = input("Enter the content to write to the file: ")
            write_file(filename, content)
            print(f"Content written to {filename} successfully.")
            # Ask the user if they want to perfomr another action
            continue_answer = input("Do you want to read another file or perform another action? (yes/no): ").strip().lower()
            if continue_answer == 'yes':
                return main()
            else:
                print("Exiting the program. Goodbye!")
                return None
            
        elif option == 3:
            filename = input("Enter the name of the file to modify: ")
            content = open_file(filename)
            if content:
                modified_content = modify_content(content)
                print("Modified content:")
                print(modified_content)

                # Write the modified content to a new file
                new_filename = input("Enter the name of the new file to save the modified content: ")
                write_file(new_filename, modified_content)
                print(f"Content modified and written to {new_filename} successfully.")
            else:
                print("No content to modify.")
                return main()
            
            # Ask the user if they want to perfomr another action
            continue_answer = input("Do you want to read another file or perform another action? (yes/no): ").strip().lower()
            if continue_answer == 'yes':
                return main()
            else:
                print("Exiting the program. Goodbye!")
                return None
            
        elif option == 4:
            print("Exiting the program. Goodbye!")
            return None
    except ValueError:
        print("Invalid option. Please enter a number.")
        return main()
    
    
if __name__ == "__main__":
    main()  # Run the main function to execute the program.