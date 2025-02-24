import sounddevice as sd
from scipy.io.wavfile import write
import os
import keyboard  # Import the keyboard library
import sys
# import termios

# Audio recording parameters
sample_rate = 44100  # Sample rate in Hz
duration = 2  # Duration of recording in seconds
file_extension = '.wav'  # File extension for audio files


def record_audio(count, base_filename):

    print("Starting recording...")
    # Record audio for the given duration
    try:
      audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32', device=0)
      sd.wait()  # Wait for the recording to finish
    except Exception as e:
      print(e)
    # Generate filename with a sequential number
    filename = f"{base_filename}_{count}{file_extension}"
    path = os.path.join(base_filename, filename)
    # Save the audio file
    write("./samples/" + path, sample_rate, audio)
    print(f"\nRecording finished, file saved to: {path} \n\n")
    return count + 1
    
# def flush_input() :
#     try :
#         fd = sys.stdin.fileno()
#         termios.tcflush(fd, termios.TCIOFLUSH)
#     except Exception as e:
#         print("ERROR : ", e)

if __name__ == "__main__":

    print("###############################")
    print("##                           ##")
    print("##                           ##")
    print("##      Voice Recorder       ##")
    print("##                           ##")
    print("##                           ##")
    print("###############################")
    print("")
    run = True
        
    while run :
        count = 1
        # flush_input()
        print("")
        print("1. Backgroud")
        print("2. Up")
        print("3. Down")
        print("")
        usr_input2 = input("Please choose which type of sound to recored : ")
        
        print("You choose ", usr_input2)
        
        if usr_input2 == "2" :
            base_filename = "up"
        elif usr_input2 == "3" :
            base_filename = "down"
        else :
            base_filename = "background"
            
        base_filename = base_filename
        os.makedirs("./samples/" + base_filename, exist_ok=True)
        
        print("Press 'R' to start recording...")
        keyboard.wait('r')  # Wait for the 'R' key to be pressed
        while count <= 8:
            count = record_audio(count, base_filename)
            
            if count == 8 :
                print("We have ", 8-count+1, "time left. Press 'R' to record again, or Ctrl+C to stop the program.")
                keyboard.wait('r')  # Wait for the 'R' key to be pressed again
            elif count == 9 :
                pass
            else :
                print("We have ", 8-count+1, "times left. Press 'R' to record again, or Ctrl+C to stop the program.")
                keyboard.wait('r')  #  for the 'R' key to be pressed again
                
        # flush_input()
        usr_input = input("Record completed? y:YES, n:No : ")
    
        if usr_input == "y" or usr_input == "Y" :
            run = False
        else :
            run = True
