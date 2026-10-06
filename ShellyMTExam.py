"""
Program: ShellyMTExam.py
Student: Luke Shelly

Description:
This is the main program. It creates a ShellyCombineFiles
object and uses the class methods to combine text files.
"""


from ShellyCombineFiles import ShellyCombineFiles


def main():

    try:

        # Create the class object
        files = ShellyCombineFiles()

        # Ask for the original file names
        files.get_file_names()

        # Ask for the new file name
        files.get_combined_name()

        # Combine all files
        files.combine_files()

        # Read and print the combined file
        files.print_combined_file()

        # Print the statistics
        files.print_statistics()

    except FileNotFoundError:
        print("\nERROR: One of the files was not found.")
        print("Check the file names and try again.")

    except PermissionError:
        print("\nERROR: You do not have permission to use a file.")

    except OSError:
        print("\nERROR: There was a problem opening a file.")

    except Exception as error:
        print("\nERROR:", error)


main()