import json


def load_data():
  try:
    with open("youtube.txt",'r') as file:
      data = json.load(file)
      print(data)
      return data
  except FileNotFoundError:
    print("File not found")
    return [] 

def helper(videos):
  with open('youtube.txt','w') as file:
    json.dump(videos,file) # it will  write the videos in file
    print("helper called")

def listallvideos(videos):
  print("\n")
  print("*" * 70)
  for index,video in enumerate(videos,start=1):
    print(f"{index}.{video['name']}, duration {video['time ']}")
  print("*" * 70)
def add_video(videos):
  videoname = input("enter video name: ")
  videotime = input("enter video length/time: ")
  videos.append({'name': videoname,'time ': videotime})
  helper(videos)

def update_video(videos):
  listallvideos(videos)
  index = int(input("enter the video number of video you want to update: "))
  if 1<=index<=len(videos):
    videoname = input("enter video name: ")
    videotime = input("enter video length/time: ")
    videos[index-1]['name'] = videoname
    videos[index-1]['time '] = videotime
    helper(videos)
  else:
    print("invalid input")

def delete_video(videos):
 listallvideos(videos)
 index=int(input("Enter a number to delete"))
 if 1 <= index <= len(videos):
   del videos[index-1]


def main():
  videos =load_data()
  while True:
    print("youtube Manager")
    print("1.list all youtube videos")
    print("2.ADD a youtube videos")
    print("3.Update youtube video details")
    print("4.Delete a  youtube videos")
    print("5.Exit the app")
    choice = int(input("enter your choice: "))

    match choice:
      case 1:
        listallvideos(videos)
      case 2:
        add_video(videos) 
      case 3:
        update_video(videos)
      case 4:
        delete_video(videos)
      case 5:
        break
      case _:
         print("Invalid choice")


if __name__=="__main__" :
  main()

