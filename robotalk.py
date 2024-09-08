import os
import keyboard 


def main():
    while True:
         print("Welcome to the robospeaker 1.1 ")
         x= input("Enter what you want me to speak")
         if x == "quit" or x=="shutup" or x=="chup" or x=="shutdown":
             x="okay by it was great to talk to you"
             command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
             os.system(command)
             break
       
         command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
         os.system(command)
        
            

        

if __name__ =="__main__":
   main();