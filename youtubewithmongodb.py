import pymongo
from bson import ObjectId
URL ="mongodb+srv://youtubemg:root@cluster0.qruozru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client=pymongo.MongoClient(URL)

db=client["ytmanager"]
video_collection =db["videos"]

print(video_collection)

def add_video():
   name=input("Enter the video name:")
   time=input("Enter the video time:")
   video_collection.insert_one({"name":name ,"time":time})

def list_videos():
   list=video_collection.find()
   for video in list:
      print(f"ID: {video['_id']},Name: {video['name']} ,Time : {video['time']}")

def update_video():
   id=input("Enter the video id:")
   name=input("Enter the video name:")
   time=input("Enter the video time:")
   video_collection.update_one({"_id":ObjectId(id)},{"$set":{"name":name,"time":time}})

def delete_video():
   id = input("enter the videos id to delete")
   video_collection.delete_one({"_id":ObjectId(id)})
   print("successfully deleted ")

def main():
   while True:
    print("\n youtube Manager App")
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


if __name__=="__main__":
    main()