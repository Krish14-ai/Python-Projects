import json

file_name = 'vids.txt'
vids =[] ## this empty list is where all the videos will be stored

##========================================================================

## this method is used to save the data of vids
def save_data(vids): 
    with open('vids.txt','w') as file:
        json.dump(vids, file)

## this method is used to load the data of vids
def  load_data():
    try :
        with open(file_name,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# to list all the videos 
def list_all_vids():
    for idx, vids in enumerate(vids,start=1):
            print(f"{idx}. {vids}")

# to add videos in the list 
def add_vids():
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    vids.append({'name':name,'time':time})
    save_data(vids)

def update():
    pass

def delete():
    pass

##===========================================================================

def main():
   
  

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
            
## this is the entry point of the app 
if __name__ == "__main__":
    main()