my_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# Access the value for 'history'
history_value = my_dict["class"]["student"]["marks"]["history"]
print("History value:", history_value)
