import cv2
import numpy as np
import pyautogui
import time

def VideoRecord(fps: float, 
                SCREEN_SIZE: any, 
                name_file: str):
  
    fourcc = cv2.VideoWriter_fourcc(*"XVID");
    out = cv2.VideoWriter(name_file, fourcc, fps, (SCREEN_SIZE))

    print("Press 'CTRL + C' for exit...")

    while True:
        
        img = pyautogui.screenshot()

        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

        if cv2.waitKey(0) & 0xFF == ord('q'):            
            break
              
    
    cv2.destroyAllWindows()
    out.release()

