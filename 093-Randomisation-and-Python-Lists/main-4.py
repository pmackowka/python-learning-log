# Metody list - append, extend, insert, remove, pop, sort, reverse, index, count, copy.
states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]


states_of_america.append("Puerto Rico")
states_of_america.extend(
    ["Guam", "American Samoa", "U.S. Virgin Islands", "Northern Mariana Islands"]
)  # Add multiple items to the list
states_of_america.insert(1, "New York")  # Insert an item at a specific index
states_of_america.remove("New York")  # Remove an item by value
states_of_america.pop()  # Remove the last item
states_of_america.pop(1)  # Remove an item by index
states_of_america.sort()  # Sort the list
states_of_america.reverse()  # Reverse the list
print(states_of_america.index("Texas"))  # Get the index of an item
# states_of_america.clear()	# Clear the list
print(states_of_america.count("Texas"))  # Count the number of occurrences of an item
states_of_america_copy = states_of_america.copy()  # Copy the list
print(states_of_america_copy)
print(len(states_of_america))
