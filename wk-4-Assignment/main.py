def file_read_write():
    try:
        # Open input.txt and read content
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify content (make it uppercase)
        modified_content = content.upper()

        # Write modified content into output.txt
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File processed successfully. Check 'output.txt'")

    except FileNotFoundError:
        print("❌ The file 'input.txt' was not found.")


def error_handling_lab():
    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("📂 File content:\n", content)

    except FileNotFoundError:
        print(f"❌ The file '{filename}' does not exist.")
    except PermissionError:
        print(f"🚫 You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run both parts
file_read_write()
error_handling_lab()
