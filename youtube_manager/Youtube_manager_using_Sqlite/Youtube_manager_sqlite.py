
import sqlite3
videos =[]
conn = sqlite3.connect('videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )

''')

#========================================
# Helper functions 

def list_all_vids():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_vids():
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update():
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE name = ?", (name, time, name))
    conn.commit()

def delete():
    name = input("Enter the name of the video: ")
    cursor.execute("DELETE FROM videos WHERE name = ?", (name,))
    conn.commit()

def load_vid_names():
    cursor.execute("SELECT name FROM videos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#==========================================================
def main():
    while True:
            print("\n Youtube manager app With Data Base")
            print("List all the videos")
            print("Add a video")
            print("Update a video")
            print("Delete a video")
            print("Exit")
            choice = int(input("Enter your choice : "))
            print(f"You chose {choice}\n")
            match choice:
                case 1:
                    add_vids()
                case 2:
                    list_all_vids()
                case 3:
                    update()
                case 4:
                    delete()
                case 5:
                    load_vid_names()
                case 6:
                    print("Thankyou for using Youtube Manager")
                    break
                case _:
                    print("Invalid choice\n")

#========================================
if __name__ == "__main__":
    main()


