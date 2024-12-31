// NOTE : IN THIS I'VE GIVEN THE COORDINATES OF THE WHATSAPP ICON AND THE TEXT BOX WHERE THE BOT WILL TYPE THE REPLY. YOU CAN CHANGE THE COORDINATES ACCORDING TO YOUR SCREEN RESOLUTION.


import pyautogui
import time
import pyperclip
from openai import OpenAI  


client = OpenAI(
  api_key="ENTER YOUR OWN API KEY",
) 
def is_last_message_from_sender(chat_log, sender_name="Jerry"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
# Give the user a few seconds to switch to the correct window
time.sleep(3)
# Click on the whatsapp icon 
pyautogui.click(686, 744)

# Function to perform the sequence of actions
def automate_text_selection():
    
    time.sleep(0.5)  # Wait a bit for any UI updates if necessary
     
    # Click and drag from (509, 113) to (1347, 663) to select text
    pyautogui.moveTo(603, 263)
    pyautogui.dragTo(1300, 630, duration=1.0)  # Dragging duration can be adjusted
    
    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for the text to be copied to the clipboard
    pyautogui.click(592, 224)
    
    # Get the copied text from the clipboard
    copied_text = pyperclip.paste()
    print(copied_text)
    
    
    if is_last_message_from_sender(copied_text):
      completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system", "content": "You are a virtual assistant named jerry skilled in general tasks like Alexa and Google Cloud. Give short responses."},
          {"role": "user", "content": copied_text}
      ]
      )

      response = completion.choices[0].message.content
      pyperclip.copy(response)

      # Click at (896, 688) and paste the text
      pyautogui.click(896, 688)
      pyautogui.hotkey('ctrl', 'v')
      time.sleep(0.5)  # Wait a moment for the paste action to complete
      
      # Press Enter at (1326, 690)
      pyautogui.click(1326, 690)
      pyautogui.press('enter')
while True:
  automate_text_selection()

