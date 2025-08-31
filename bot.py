import pyautogui
import time
import pyperclip
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

 # 1. Click the chrome icon at coordinate 1007,1056
pyautogui.click(1118,993)
time.sleep(1) # To ensure click is registerd

while True:
    # 2. Drag the mouse from 1476,225 to 1072,933 to select the text
    pyautogui.moveTo(1476,225)
    pyautogui.dragTo(1072,933)

    # 3. Copy the selected item to clipboard
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.click(1994,281) # To deselect the text

    # 4. Retrieve the text from clipboard and store in a variable
    chat_history = pyperclip.paste()

    print(chat_history)

    completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named Vaibhav who speaks Hindi as well as English. "
                "You are from India and you are a DevOps Engiiner. You analyze the chat history and respond like Vaibhav."
                "Output should be the next chat response as Vaibhav."},
                {"role": "user", "content": chat_history}
            ]
    )

    response =  completion.choices[0].message.content
    # Copy content of pyperclip
    pyperclip.copy(response)

    # Once we get the response, we need to send the response back to the chat

    # 5. Click at coordinates 1808,1328
    pyautogui.click(1808,1328)
    time.sleep()

    # 6. Paste the content
    pyautogui.hotkey('ctrl','v')
    time.sleep()

    # 7. Press enter
    pyautogui.press('enter')


    