import pyautogui
import time

pyautogui.PAUSE = 0.3

# Press the 'win' key to open the start menu
pyautogui.press("win")
time.sleep(1)

# Type "chrome" to search for Google Chrome
pyautogui.write("chrome")
time.sleep(1)

# Press 'enter' to open Google Chrome
pyautogui.press("enter")
time.sleep(3)

# Click on a specific location on the screen (Chrome's position)
pyautogui.click(x=719, y=499)
time.sleep(1)

# Click on a position to open the specific tab or area (e.g., URL bar)
pyautogui.click(x=219, y=74)

# Type the URL of the page to visit
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Click on a specific button or element on the page
pyautogui.click(x=698, y=662)
time.sleep(3)

# Importing pandas for data manipulation
import pandas as pd

# Reading a CSV file containing the products data
tabela = pd.read_csv("produtos.csv")

# Print the table to check the contents
print(tabela)

# Step 4: Register a product
for linha in tabela.index:
    # Click on the "code" input field
    pyautogui.click(x=396, y=322)
    
    # Get the product code from the table and enter it
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    
    # Move to the next field by pressing "tab"
    pyautogui.press("tab")
    
    # Fill in the brand field
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    # Fill in the type field
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    # Fill in the category field
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    # Fill in the unit price field
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    # Fill in the cost field
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    # If there are any observations, enter them
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    
    # Press 'enter' to submit the product
    pyautogui.press("enter")
    
    # Scroll up to the top of the page
    pyautogui.scroll(5000)

