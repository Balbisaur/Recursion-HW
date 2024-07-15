file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

# We will create a recursive function that will search through the file system

def search_file(file_system, target):
    for item in file_system:
        if isinstance(item, list):
            if search_file(item, target):
                return True

        if item == target:
            print("Big HOORAY!")
            
    

# Now we can call our function with the file system and the target file

search_file(file_system, "chicken_dinner.txt")
