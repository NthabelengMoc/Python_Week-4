while True:
	try:
		file_name = input("Enter the file name (or type 'exit' to quit): ")
		if file_name.lower() == 'exit':
			print("Exiting the program.")
			break
		with open(file_name, 'r') as file:
			print("File opened successfully!")
			# You can add further file processing logic here
			break
	except FileNotFoundError:
		print("Error: File not found. Please try again.")
	except PermissionError:
		print("Error: Permission denied. Please try again.")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")
print(f"An unexpected error occurred: {e}")