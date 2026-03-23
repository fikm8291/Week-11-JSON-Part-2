# -------------------------------------------
# Exercise 1: Manchester Central Library Archive
# -------------------------------------------
# NEW CONCEPT: What is JSON?
# JSON (JavaScript Object Notation) is a way to store data in a text file.
# Up until now, your variables disappeared when you closed your program.
# JSON files stay on your hard drive forever, like a "Save Game" file.
#
# THE HANDSHAKE:
# To use JSON, we must "Open" the file, "Load" the data into a Python 
# variable, and then the file "Closes" automatically.
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Work in groups of 2–3. Share the same GitHub repository.
# Roles:
# - DRIVER: Types the code and runs commands.
# - NAVIGATOR: Observes, guides, and prevents "bugs".
# -------------------------------------------

import json # The toolkit needed to translate JSON into Python

# -------------------------------------------
# Task 1: The Initial Handshake (Reading Data)
# -------------------------------------------
# CONCEPT: 
# We use 'with open' to create a temporary bridge to the file.
# 'r' stands for Read mode. This task focuses on loading and filtering.
#
# EXAMPLE SYNTAX:
# with open('your_file.json', 'r') as some_variable:
#     data_list = json.load(some_variable)
#
# TODO:
# 1. Use the example above to open 'archive.json' in 'r' mode.
# 2. Load the data into a variable called 'mcr_data'.
# 3. Use a 'for' loop to iterate through 'mcr_data'.
# 4. Print each book's title and its price, but only if the price is 
#    over £12.00. 
# 5. Challenge: Format the output to say: "Premium Item: [Title] - £[Price]"
#
# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your program. You should see only the books that cost more than £12.00.
# If you get a "FileNotFoundError", check that archive.json is in the correct folder.
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message.
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 2: The Archive Audit
# -------------------------------------------
# CONCEPT: 
# Every time you want to check the data, you must perform the "Handshake".
# This ensures you are always looking at the most recent version of the file.
#
# TODO:
# 1. Open 'archive.json' and load it into a variable called 'audit_list'.
# 2. Create a variable 'empty_shelves' starting at 0.
# 3. Loop through 'audit_list'.
# 4. Logic: If the 'stock' of a book is 0, print a warning with the 
#    book's title and add 1 to your 'empty_shelves' counter.
# 5. After the loop, print the total number of out-of-stock items.
#
# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your program. Did it identify "Collected Poems" as being out of stock?
# Does it show a final count of "1" empty shelf?
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit.
# 3. Push to the repository.
# -------------------------------------------


# -------------------------------------------
# Task 3: Smart Search
# -------------------------------------------
# CONCEPT: 
# Real programs need to handle "User Input". We will combine a JSON 
# load with a string search that isn't picky about capital letters.
#
# TODO:
# 1. Open 'archive.json' and load it into a variable called 'search_vault'.
# 2. Ask the user: "Which Manchester author are you looking for? ".
# 3. Create a boolean variable 'match_found' and set it to False.
# 4. Loop through 'search_vault'. 
# 5. IF the user's input (in lowercase) is found inside the 'author' name 
#    (in lowercase), print the full details of that record and set 
#    'match_found' to True.
# 6. After the loop, if 'match_found' is still False, print "No records match that author."
#
# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Try searching for "Gaskell" or "Burgess". 
# Try searching for "gaskell" in all lowercase. Does it still work?
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage.
# 2. Commit.
# 3. Push.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: The Insurance Valuation Report
# -------------------------------------------
# CONTEXT: 
# Museums and libraries must value their collection for insurance 
# purposes. If a pipe bursts in the Central Library, we need to 
# know the financial "Replacement Value" of every item lost.
#
# TODO:
# 1. Load the JSON data from 'archive.json' into a new variable.
# 2. Create a 'running_total' variable starting at 0.0.
# 3. Loop through the data. For every item, calculate the value 
#    of its total stock (Price * Stock).
# 4. Add that value to your 'running_total'.
# 5. Print the final result formatted as a professional currency 
#    string. Example: "Total Archive Insurance Value: £145.50"
#
# Write your code below:


# Extension 2: Contributing to History (Writing Data)
# -------------------------------------------
# CONTEXT: 
# Data isn't static; it grows. When a new book is published in 
# Manchester, we must add it to the archive. This requires the 
# "Save" step: Loading, Modifying, and Overwriting the file.
#
# TODO:
# 1. Load the current 'archive.json' into a variable (this will be "your list").
# 2. Create a new dictionary representing a new book. You choose 
#     the details, but it MUST have the same keys: "id", "title", 
#    "author", "genre", "price", and "stock".
# 3. Use .append() to add your dictionary to the list you loaded.
# 4. Use 'with open('archive.json', 'w') as file:' to open the 
#    file in "Write" mode. This will wipe the old file and 
#    allow you to save the new, longer list.
# 5. Use json.dump(your_list, file, indent=4) to save.
#
# Write your code below:


# Extension 3: The Archive Catalogue Formatter
# -------------------------------------------
# CONTEXT: 
# Databases often contain "messy" data or very long strings. Before 
# displaying this to a user on a small screen (like a library kiosk), 
# we often have to "truncate" (shorten) text and create labels.
#
# TODO:
# 1. Load the JSON data from 'archive.json'.
# 2. Loop through every record.
# 3. Handle Long Titles: If a title is more than 20 characters long, 
#    print only the first 17 characters followed by "..." 
#    (Example: "The Condition of the Working Class..." becomes "The Condition of th...").
# 4. Create Stock Labels: If stock is 0, create a label saying "OUT". 
#    If stock is between 1 and 5, label it "LOW". If over 5, label it "HIGH".
# 5. Print a clean, formatted row for each item: 
#    "ITEM: [Short Title] | STATUS: [Stock Label]"
#
# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# 1. Run Extension 1: Is your valuation accurate?
# 2. Run Extension 2: Check your archive.json file. Is the new book there?
# 3. Run Extension 3: Are the long titles shortened correctly?
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with a descriptive message.
# 3. Push to the repository.
# -------------------------------------------


# -------------------------------------------
# ADVANCED: The Genre Security Check
# -------------------------------------------
# CONCEPT: 
# Creating a reusable program structure using functions.
#
# TODO:
# 1. Create a function called 'verify_genre'.
# 2. The function should ask the user for a genre (e.g. Poetry).
# 3. Load the JSON file and count how many books match that genre.
# 4. If the count is 0, print "Genre not found in the Manchester Archive."
# 5. If matches are found, print "We found [count] records for [genre]."
# 6. Call the function to test your program.
#
# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Check your 'archive.json' file in your text editor. 
# Do you see your new author added to the bottom of the list?
# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# Use Git to:
# 1. Stage your final changes.
# 2. Commit with a final message (e.g. "Completed all archive management tasks").
# 3. Push your final version to the repository.
# -------------------------------------------
