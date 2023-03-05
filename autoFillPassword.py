import os
import subprocess
def send_username_password(username_password):
    send_key = ''
    for index_key in username_password:
        key = '{' + index_key + '}'
        send_key = send_key + '%SendKeys% ' + '"' + key + '"' + '\n'
    return send_key

def send_tab(loop):
    send_key = ''
    for tab in range(loop):
        send_key = send_key + '%SendKeys% ' + '"' + '{' + 'TAB' + '}' + '"' + '\n'
    return send_key

def send_enter():
    send_key = '%SendKeys% ' + '"' + '{' + 'ENTER' + '}' + '"' + '\n'
    return send_key

def send_esc():
    send_key = '%SendKeys% ' + '"' + '{' + 'ESC' + '}' + '"' + '\n'
    return send_key

def login_facebook_chrome(username, password):
    source_file = os.getcwd() + '\\AutoLogin.bat'
    auto_login_file = open(source_file,'w+')
    auto_login_file.write('@if (@CodeSection == @Batch) @then\n')
    auto_login_file.write('@echo off\n')
    auto_login_file.write('set SendKeys=CScript //nologo //E:JScript "%~F0"\n')
    auto_login_file.write('START Chrome "https://th-th.facebook.com/"\n')
    auto_login_file.write('timeout /t 5\n')
    auto_login_file.write(send_esc())
    auto_login_file.write(send_username_password(username))
    auto_login_file.write(send_tab(1))
    auto_login_file.write(send_username_password(password))
    auto_login_file.write(send_enter())
    auto_login_file.write('goto :EOF\n')
    auto_login_file.write('@end\n')
    auto_login_file.write('// JScript section\n')
    auto_login_file.write('var WshShell = WScript.CreateObject("WScript.Shell");\n')
    auto_login_file.write('WshShell.SendKeys(WScript.Arguments(0));')
    auto_login_file.close()
    subprocess.call(source_file)
    os.remove(source_file)

def login_facebook_edge(username, password):
    source_file = os.getcwd() + '\\AutoLogin.bat'
    auto_login_file = open(source_file,'w+')
    auto_login_file.write('@if (@CodeSection == @Batch) @then\n')
    auto_login_file.write('@echo off\n')
    auto_login_file.write('set SendKeys=CScript //nologo //E:JScript "%~F0"\n')
    auto_login_file.write('START MICROSOFT-EDGE:"https://th-th.facebook.com/"\n')
    auto_login_file.write('timeout /t 5\n')
    auto_login_file.write(send_esc())
    auto_login_file.write(send_username_password(username))
    auto_login_file.write(send_tab(1))
    auto_login_file.write(send_username_password(password))
    auto_login_file.write(send_enter())
    auto_login_file.write('goto :EOF\n')
    auto_login_file.write('@end\n')
    auto_login_file.write('// JScript section\n')
    auto_login_file.write('var WshShell = WScript.CreateObject("WScript.Shell");\n')
    auto_login_file.write('WshShell.SendKeys(WScript.Arguments(0));')
    auto_login_file.close()
    subprocess.call(source_file)
    os.remove(source_file)

def login_roblox_chrome(username, password):
    source_file = os.getcwd() + '\\AutoLogin.bat'
    auto_login_file = open(source_file,'w+')
    auto_login_file.write('@if (@CodeSection == @Batch) @then\n')
    auto_login_file.write('@echo off\n')
    auto_login_file.write('set SendKeys=CScript //nologo //E:JScript "%~F0"\n')
    auto_login_file.write('START Chrome "https://www.roblox.com/Login"\n')
    auto_login_file.write('timeout /t 5\n')
    auto_login_file.write(send_esc())
    auto_login_file.write(send_tab(10))
    auto_login_file.write(send_username_password(username))
    auto_login_file.write(send_tab(1))
    auto_login_file.write(send_username_password(password))
    auto_login_file.write(send_enter())
    auto_login_file.write('goto :EOF\n')
    auto_login_file.write('@end\n')
    auto_login_file.write('// JScript section\n')
    auto_login_file.write('var WshShell = WScript.CreateObject("WScript.Shell");\n')
    auto_login_file.write('WshShell.SendKeys(WScript.Arguments(0));')
    auto_login_file.close()
    subprocess.call(source_file)
    os.remove(source_file)

def login_roblox_edge(username, password):
    source_file = os.getcwd() + '\\AutoLogin.bat'
    auto_login_file = open(source_file,'w+')
    auto_login_file.write('@if (@CodeSection == @Batch) @then\n')
    auto_login_file.write('@echo off\n')
    auto_login_file.write('set SendKeys=CScript //nologo //E:JScript "%~F0"\n')
    auto_login_file.write('START MICROSOFT-EDGE:"https://www.roblox.com/Login"\n')
    auto_login_file.write('timeout /t 5\n')
    auto_login_file.write(send_esc())
    auto_login_file.write(send_tab(10))
    auto_login_file.write(send_username_password(username))
    auto_login_file.write(send_tab(1))
    auto_login_file.write(send_username_password(password))
    auto_login_file.write(send_enter())
    auto_login_file.write('goto :EOF\n')
    auto_login_file.write('@end\n')
    auto_login_file.write('// JScript section\n')
    auto_login_file.write('var WshShell = WScript.CreateObject("WScript.Shell");\n')
    auto_login_file.write('WshShell.SendKeys(WScript.Arguments(0));')
    auto_login_file.close()
    subprocess.call(source_file)
    os.remove(source_file)

def login_myku_chrome(username, password):
    source_file = os.getcwd() + '\\AutoLogin.bat'
    auto_login_file = open(source_file,'w+')
    auto_login_file.write('@if (@CodeSection == @Batch) @then\n')
    auto_login_file.write('@echo off\n')
    auto_login_file.write('set SendKeys=CScript //nologo //E:JScript "%~F0"\n')
    auto_login_file.write('START Chrome "https://my.ku.th/login/"\n')
    auto_login_file.write('timeout /t 5\n')
    auto_login_file.write(send_esc())
    auto_login_file.write(send_tab(20))
    auto_login_file.write(send_username_password(username))
    auto_login_file.write(send_tab(1))
    auto_login_file.write(send_username_password(password))
    auto_login_file.write(send_enter())
    auto_login_file.write('goto :EOF\n')
    auto_login_file.write('@end\n')
    auto_login_file.write('// JScript section\n')
    auto_login_file.write('var WshShell = WScript.CreateObject("WScript.Shell");\n')
    auto_login_file.write('WshShell.SendKeys(WScript.Arguments(0));')
    auto_login_file.close()
    subprocess.call(source_file)
    os.remove(source_file)

def login_myku_edge(username, password):
    source_file = os.getcwd() + '\\AutoLogin.bat'
    auto_login_file = open(source_file,'w+')
    auto_login_file.write('@if (@CodeSection == @Batch) @then\n')
    auto_login_file.write('@echo off\n')
    auto_login_file.write('set SendKeys=CScript //nologo //E:JScript "%~F0"\n')
    auto_login_file.write('START MICROSOFT-EDGE:"https://my.ku.th/login/"\n')
    auto_login_file.write('timeout /t 5\n')
    auto_login_file.write(send_esc())
    auto_login_file.write(send_tab(20))
    auto_login_file.write(send_username_password(username))
    auto_login_file.write(send_tab(1))
    auto_login_file.write(send_username_password(password))
    auto_login_file.write(send_enter())
    auto_login_file.write('goto :EOF\n')
    auto_login_file.write('@end\n')
    auto_login_file.write('// JScript section\n')
    auto_login_file.write('var WshShell = WScript.CreateObject("WScript.Shell");\n')
    auto_login_file.write('WshShell.SendKeys(WScript.Arguments(0));')
    auto_login_file.close()
    subprocess.call(source_file)
    os.remove(source_file)

def menu_browser():
    while True:
        print("========== MENU ==========")
        print("1) Chrome")
        print("2) Microsoft Edge")
        choose = input("Choose : ")
        try:
            choose = int(choose)
            if choose == 1 or choose == 2:
                return choose
            else:
                print("Please Select 1 or 2")
        except:
            print("Please Select 1 or 2")

def menu_website():
    while True:
        print("========== MENU ==========")
        print("1) Facebook")
        print("2) Roblox")
        print("3) MyKU")
        choose = input("Choose : ")
        try:
            choose = int(choose)
            if choose == 1 or choose == 2 or choose == 3:
                return choose
            else:
                print("Please Select 1 or 2 or 3")
        except:
            print("Please Select 1 or 2 or 3")

if __name__ == "__main__":
    browser = menu_browser()
    website = menu_website()
    username = input("Username : ")
    password = input("Password : ")
    if browser == 1 and website == 1:
        login_facebook_chrome(username, password)
    elif browser == 1 and website == 2:
        login_roblox_chrome(username, password)
    elif browser == 1 and website == 3:
        login_myku_chrome(username, password)
    elif browser == 2 and website == 1:
        login_facebook_edge(username, password)
    elif browser == 2 and website == 2:
        login_roblox_edge(username, password)
    elif browser == 2 and website == 3:
        login_myku_edge(username, password)
