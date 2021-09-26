import time
import pyautogui
import webbrowser as wb

contact = ['1234567890', '222222222']  # List of contacts to whom you want to send message

message = ''' whatsapp script ''' # Type your message

for i in range(len(contact)):
    wb.open(f"https://wa.me/+91{contact[i]}?text={message}")
    time.sleep(20)
    pyautogui.click(1870, 1037)  # position of send button
    time.sleep(7)

# time.sleep(5)
# print(pyautogui.position())  # to get the position of send button of whatsapp



