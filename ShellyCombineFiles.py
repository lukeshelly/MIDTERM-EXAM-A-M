"""
Program: ShellyCombineFiles.py
Student: Luke Shelly

Description:
This class combines multiple text files into one text file.
The user can enter any number of file names separated by commas.
The class also reads the combined file and displays statistics.
"""


class ShellyCombineFiles:

    def __init__(self):
        self.file_names = []
        self.combined_file = ""
        self.number_of_lines = []

    # Ask for the names of the files
    def get_file_names(self):

        user_files = input(
            "Enter file names separated by commas: "
        )

        self.file_names = user_files.split(",")

        # Remove spaces from each file name
        for i in range(len(self.file_names)):
            self.file_names[i] = self.file_names[i].strip()

    # Ask for the combined file name
    def get_combined_name(self):

        self.combined_file = input(
            "Enter the name for the combined file: "
        ).strip()

    # Combine the files
    def combine_files(self):

        self.number_of_lines = []

        # Create the new combined file
        with open(self.combined_file, "w") as combined:

            for file_name in self.file_names:

                line_count = 0

                # Read the original file
                with open(file_name, "r") as original:

                    for line in original:

                        combined.write(line)
                        line_count += 1

                self.number_of_lines.append(line_count)

    # Read and print the combined file
    def print_combined_file(self):

        print("\n===== COMBINED FILE =====")

        with open(self.combined_file, "r") as combined:

            for line in combined:
                print(line, end="")

        print("\n=========================")

    # Print statistics
    def print_statistics(self):

        print("\n===== STATISTICS =====")

        print(
            "Number of files combined:",
            len(self.file_names)
        )

        for i in range(len(self.file_names)):

            print(
                "File:",
                self.file_names[i],
                "| Lines:",
                self.number_of_lines[i]
            )

        total_lines = sum(self.number_of_lines)

        print("Combined file:", self.combined_file)
        print("Lines in combined file:", total_lines)

        print("======================")