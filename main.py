answer = 0

def on_button_pressed_a():
    global answer
    answer = randint (1,9)
    if answer == 1:
        basic.show_string ("Cow")
    elif answer == 2:
        basic.show_string ("Zebra")
    elif answer == 3:
        basic.show_string ("Panda")
    elif answer == 4 :
        basic.show_string ("Flamingo")
    elif answer == 5:
        basic.show_string ("Dog")
    elif answer == 6:
        basic.show_string ("Cat")
    elif answer == 7:
        basic.show_string ("Fish")
    elif answer == 8:
        basic.show_string ("Bird")
    elif answer == 9:
        basic.show_string ("Guinea Pig")

input.on_button_pressed(Button.A, on_button_pressed_a)