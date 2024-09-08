import sqlite3 as ww

conn = ww.connect('youtube_videos.db')
cursor =conn.cursor()
cursor.execute("""create table if not exists videos(
               id integer primary key,
               name text not null,
               time text not null ) """)

def list_videos():
    cursor.execute("select * from videos")
    for row in cursor.fetchall():
       print(row)

def add_video ():
  name = input("Enter the name of video")
  time = input("Enter the time of video")
  cursor.execute("Insert into videos(name,time) values(?,?)",(name, time))
  conn.commit()

  
def update_video():
   
   id = int(input("Enter the id of video"))
   name = input("Enter the name of video")
   time = input("Enter the time of video")
   cursor.execute("update videos set name = ?, time = ? where id = ?",(name,time,id))
   conn.commit()

def delete_video():
    id = int(input("Enter the id of video that you want too delete"))
    cursor.execute("delete from videos where id = ?",(id,))
    conn.commit()




def main():
   while True:
    print("youtube Manager")
    print("1.list all youtube videos")
    print("2.ADD a youtube videos")
    print("3.Update youtube video details")
    print("4.Delete a  youtube videos")
    print("5.Exit the app")
    choice = int(input("enter your choice: "))

    if choice == 1:
       list_videos()
    elif choice ==2:
       add_video()
    elif choice ==3:
       update_video()
    elif choice ==4:
       delete_video()
    elif choice == 5:
       break
    else:
       print("invalid choice")

    #conn.close()   
          




if __name__ == "__main__":
    main()