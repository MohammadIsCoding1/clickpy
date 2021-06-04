import clickpy
import random
import pyautogui

intA=int()
intB=int()
strA=str()
strB=str()

pyautogui.FAILSAFE=False

class atrubutes:
    def click_atrubutes():
        clickpy.click=random.randint(intA, intB)
        clickpy.ran.click=pyautogui.click()
        clickpy.move_cursor=pyautogui.move(intA, intB)
        clickpy.random.move_cursor=pyautogui.move(random.randint(0, 1365), random.randint(767))
    def write_atrubutes():
        clickpy.write=pyautogui.write(strA, strB)
        clickpy.alert_screen=pyautogui.alert(strA)
    def random_number():
        clickpy.ran_number=random.randint(intA, intB)
    def make_things():
        clickpy.make_text_file=file_make=open(strA, 'a')


    if __name__=='__main__':
        click_atrubutes()
        write_atrubutes()
        random_number()
        make_things()
