import hashlib
def get_hash(filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    return hashlib.sha256(data).hexdigest()


# Get the name of the file you are trying to check
filename = input("Enter the name of the file you want to check: ")

# Tells python which file to look at(adress)
stored_files_hashes = filename + ".integrity" 


# Calls get_hash function and reads and gets hash and stores as a stirng in strating_hash 
starting_hash = get_hash(filename)


# Need try becuase it may not work if its the first time running the program(No stored hash)
try:
    
    # If can't open/read, Raise a FileNotFoundError
    hash_value = open(stored_files_hashes, "r") # opens the stored hash in the read mode(Don't need to read the bytes("rb"))
    stored_hash = hash_value.read() # Reads the stored hash value and stores it as a string in stored_hash
    hash_value.close()

    if stored_hash == starting_hash:
        print("File integrity is confirmed. The file has not been modified.")
    else:
        print("THE FILE HAS BEEN MODIFIED. THE HASH VALUES DO NOT MATCH.")
except FileNotFoundError: # Happens when the new .integrity file of a files hash does not exist yet.
    hash_value = open(stored_files_hashes, "w") # Opens the .integrity file in write mode to create it and write the hash value to it beucase Read does not create a file. 
    hash_value.write(starting_hash) # The current hash value of the file is added to the .integrity file
    hash_value.close()
    print("First time running the program. The hash value of the given file is now stored for future checks")
