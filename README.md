# Selenium-Whatsapp-Spammer
This is a script which can spam a conversation in WhatsApp Web. It uses the `selenium` python package. <br>
**Be very careful with this script! Read the how to use very carefully.**

## Prerequisites
1. Install the `selenium` package using pip. Run the following command:
  `pip3 install selenium`. (This commmand may vary depending on the OS and the python version.)

2. [Download the Chrome webdriver using this link](https://chromedriver.chromium.org/downloads). Make sure you select the right Chrome version while downloading this. You can find the Chrome version by clicking on the three dots on the top-right corner and going to the **About Chrome** tab in the **Help** menu.

After you have done these, we can use the script.

## How to use
1. Extract the `.zip` webdriver file downloaded. And put the executable file in an easily accessible location.
2. Copy the webdriver file's filepath, and put it in the `PATH` variable in the script.
3. Enter the name of the person or the group in the `TARGET` variable. **Make sure that when you search this string in WhatsApp Web, your target is the first search result.** Failing to do so may result in you spamming the wrong person. The script always spams the first result, so make sure you provide the full name of the conversation.
4. Fill in the `SPAM` and `TIMES` variable, denoting the text which you want to spam and how many times you want to spam it respectively.
5. Have your phone ready because you will have to scan the QR code to access WhatsApp Web. Unfortunately, we will have to do this everytime we want to a new spam.
6. Run the script, it will open a new Chrome instance.
7. Once WhatsApp Web loads, scan the QR code. Then just wait and see the script in action!
