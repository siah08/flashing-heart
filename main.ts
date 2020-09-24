input.onButtonPressed(Button.A, function () {
    control.reset()
})
input.onButtonPressed(Button.B, function () {
    while (true) {
        basic.showIcon(IconNames.Heart)
        basic.showIcon(IconNames.SmallDiamond)
    }
})
