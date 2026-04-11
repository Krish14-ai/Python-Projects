import json

file_name = 'vids.txt'

# ========================================================================

# 4) this method is used to save the data of vids
def save_data(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

# this method is used to load the data of vids
def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# 2) to list all the videos 
def list_all_vids(videos):
    print('\n') 
    print('*' * 70)                     
    if not videos:
        print("No videos found.")
        return
    for idx, vid in enumerate(videos, start=1):
        print(f"{idx}. {vid['name']} - {vid['time']}")  

    print('\n') 
    print('*' * 70)

# 1) to add videos in the list 
def add_vids(videos):
    print(f"These are your previously added videos: \n{videos}\n")
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({'name': name, 'time': time})  # FIX 4: append to `full_data`, not the empty global
    save_data(videos)

# 3) to update the videos 
def update(videos):
    index = int(input("Enter the index of your video you want to update: "))
    
    if index >=1 or index <= len(videos):
        new_name = input("Enter the new name of the video: ")
        new_time = input("Enter the new time of the video: ")
        videos[index-1] = {'name': new_name, 'time': new_time}
        save_data(videos)
    else :
        print('invalid index')
        
    

# 4) to delete the videos 
def delete(videos):
    list_all_vids(videos)
    index =int(input("Enter the index of the video you wanna delete : "))
    if index >=1 or index < len(videos):
        del videos[index -1]
        save_data(videos)

        print("Your selected video has been deleted successfully\n")
        print("Remaining videos are : ")
        list_all_vids(videos)
    else:
        print("Invalid index")


# 5) to Display all the video name
def load_vid_names(videos):
    print('\n') 
    print('*' * 70)
    print("All the names of Your videos are as listed below : ")
    for i in range(len(videos)):
        print(f"{i+1}. {videos[i]['name']}")


    print('*' * 70)




# ===========================================================================

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager\n")
        print("1. Add a video")
        print("2. List all videos")
        print("3. Update the videos")
        print("4. Delete a video")
        print("5. Display all video names")
        print("6. Exit")
        choice = int(input("Enter your choice : "))
        print(f"You chose {choice}\n")
        match choice:
            case 1:
                add_vids(videos)
            case 2:
                list_all_vids(videos)
            case 3:
                update(videos)
            case 4:
                delete(videos)
            case 5:
                load_vid_names(videos)
            case 6:
                print("Thankyou for using Youtube Manager")
                break
            case _:
                print("Invalid choice\n")

if __name__ == "__main__":
    main()

