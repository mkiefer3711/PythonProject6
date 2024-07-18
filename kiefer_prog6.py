import os

# Function that validates the input file
def validate_input_file(inputfile):
    # Grabs the last four places in the input file
    inputfileextension = inputfile[-4:]
    # If statement that adds .txt to the file if it is not included
    if inputfileextension != ".txt":
        inputfile = inputfile + ".txt"
    print("\nInput file: ", inputfile)
    # Exception handling that determines if the input file exists and is readible
    try:
        input_file_handle = open(inputfile, "r")
        input_file_handle.close()
        return inputfile
    except:
        return ""
# Function that validates the output file
def validate_output_file(outputfile):
    # Grabs the last four places in the output file
    outputfileextension = outputfile[-4:]
    # If statement that adds .txt to the file if it is not included
    if outputfileextension != ".txt":
        outputfile = outputfile + ".txt"
    print("Output file: ", outputfile)
    # Exception handling that determines if the output file is writable
    try:
        output_file_handle = open(outputfile, "w")
        output_file_handle.close()
        return outputfile
    except:
        return ""


def main():
    input_file = ""
    output_file = ""
    # While loop that asks for the file name inputs
    while input_file == "" or output_file == "":
        inputfilename = input("Name of input file: ")
        outputfilename = input("Name of output file: ")
        # Calls the two validating file functions
        input_file = validate_input_file(inputfilename)
        output_file = validate_output_file(outputfilename)
        # If an empty string was returned from the functions, it will ask for different inputs
        if input_file == "" or output_file == "":
            print("\nOperation failed: No such file or directory\n")
    # Creates the file handles and reads the input file and writes to the output file
    input_file_handle = open(input_file, "r")
    output_file_handle = open(output_file, "w")
    # While loop that reads each line of the input file one at a time
    while True:
        theline = input_file_handle.readline()
        if len(theline) == 0:
            print("\nDone!", end="")
            break
        # Makes each line in the input file into a list
        thelist = theline.split()
        if len(thelist) == 0:
            continue
        # Changes each list to lowercase and gives the position of ch
        ch = thelist[0].lower()
        result = 0
        # Exception handling that will complain if something is not followed by two integers
        try:
            # Gives the position of num1 and num2
            num1 = int(thelist[1])
            num2 = int(thelist[2])
        except:
            result = ch + " Commands must be followed by two integers"
            # Writes the complaint to the output file and continues looping
            output_file_handle.write(str(result) + "\n")
            continue
        # If ch is add, it will change result to add the two numbers
        if ch == "add":
            result = ch + "(" + str(num1) + "," + str(num2) + ")" + " = " + str(num1 + num2)
        # If ch is sub, it will change result to subtract the two numbers
        elif ch == "sub":
            result = ch + "(" + str(num1) + "," + str(num2) + ")" + " = " + str(num1 - num2)
        # If ch is multiply, it will change result to multiply the two numbers
        elif ch == "multiply":
            result = ch + "(" + str(num1) + "," + str(num2) + ")" + " = " + str(num1 * num2)
        # If ch is divide, it will change result to divide the two numbers
        elif ch == "divide":
            # Exception handling that will divide normally unless it is division by zero, then it will complain
            try:
                result = ch + "(" + str(num1) + "," + str(num2) + ")" + " = " + str(num1 / num2)
            except ZeroDivisionError:
                result = ch + "(" + str(num1) + "," + str(num2) + ")" + " = Cannot divide by 0"
        # If ch is power, it will change result and put num1 to the power of num2
        elif ch == "power":
            result = ch + "(" + str(num1) + "," + str(num2) + ")" + " = " + str(num1 ** num2)
        # Will complain if it is not one of the 5 commands
        else:
            result = ch + " Is not a command"
        # Writes the result variable to the output file
        output_file_handle.write(str(result) + "\n")
    # Closes the input and output files
    input_file_handle.close()
    output_file_handle.close()
       
# Calls the main function    
main()