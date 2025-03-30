# Open the original file in read mode
try:
    with open("original_file.txt", "r") as original_file:
        content = original_file.read()  # Read the file content

    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("modified_file.txt", "w") as modified_file:
        modified_file.write(modified_content)

    print("File has been modified and written to 'modified_file.txt'.")
except FileNotFoundError:
    print("Error: The original file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
