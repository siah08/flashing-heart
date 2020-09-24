def on_button_pressed_a():
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    while True:
        basic.show_icon(IconNames.HEART)
        basic.show_icon(IconNames.SMALL_DIAMOND)
input.on_button_pressed(Button.B, on_button_pressed_b)
