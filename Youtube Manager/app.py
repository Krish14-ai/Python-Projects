

def list_all_vids():
    pass

def add_vids():
    pass

def update():
    pass

def delete():
    pass

vids =[] ## this empty list is where all the videos will be stored

while True:
    print("Youtube Manager \n")
    print("1. Add a video")
    print("2. List all videos")
    print("3. Update the videos")
    print("4. Delete a video")
    print("5. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            list_all_vids(vids)
        case '2':
            add_vid(vids)
        case '3':
            update(vids)
        case '4':
            delete(vids)
        case '5':
            break   
        case _:
            print("Invalid choice")
        