import requests
def main():
 nam = input("\n Enter the name of city or country you want to know the temperature ...")
 url ="https://api.weatherapi.com/v1/current.json?key=06b157bce91e4ab59d5144827241407&q={name}"
 response = requests.get(url.format(name=nam))
 data = response.json()
 print(f" The temperature of  {nam} is  {data['current']['temp_c']} C")



if __name__ =="__main__":
  main()
  print("success")
