# from first_python import chai

# chai("chai with second")

class car:
  total = 0
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
    car.total+=1

  def fullname(self):
    return f"{self.brand} {self.model}"
  
  @staticmethod
  def generaldescrition():
    return "the car is awesome"    
  

mycar = car("hhh","jjj")
# print(mycar.generaldescrition())
print(car.generaldescrition())  

# class Electriccar(car):
#   def __init__(self,brand,model,range):
#     super().__init__(brand,model)
#     self.__range=range

#     def get_range():
#       return self.__range



# ee=Electriccar("dd","ghdgb","eeee")
# print(ee.range) # if i want to make it private i do like thus __range 
# print(car.total)

import time

def timer(func):
  def wrapper(*args,**kwargs):
    start = time.time()
    result = func(*args,**kwargs)
    end = time.time()
    print(f"{func.__name__} ran in {end-start} time and it has arguments {args,result}")
    return result
  return wrapper


 # it means add will execute only after passing from timer
@timer
def add(a,b):
  return a+b

add(2,3)
timer(add(2,4))


import json


def load_data():
  try:
    with open("youtube.txt",'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return [] 

def helper(videos):
  with open('youtube.txt','w') as file:
    json.dump(videos,file) # it will  write the videos in file


def listallvideos(videos):
  for index,video in enumerate(videos,start=1):
    print(f"{index}. ")

def add_video(videos):
  videoname = input("enter video name:")
  videotime = input("enter video length/time")
  videos.append({'name': videoname,'time ': videotime})
  helper(videos)



def main():
  video =load_data()
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
        listallvideos(video)
      case 2:
        add_video(video) 
      case 3:
        update_video(video)
      case 4:
        delete_video(video)
      case 5:
        break
      case _:
         print("Invalid choice")


if __name__=="__main__" :
  main()

