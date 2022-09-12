let answer = 0
input.onButtonPressed(Button.A, function () {
    answer = randint(1, 9)
    if (answer == 1) {
        basic.showString("Cow")
    } else if (answer == 2) {
        basic.showString("Zebra")
    } else if (answer == 3) {
        basic.showString("Panda")
    } else if (answer == 4) {
        basic.showString("Flamingo")
    } else if (answer == 5) {
        basic.showString("Dog")
    } else if (answer == 6) {
        basic.showString("Cat")
    } else if (answer == 7) {
        basic.showString("Fish")
    } else if (answer == 8) {
        basic.showString("Bird")
    } else if (answer == 9) {
        basic.showString("Guinea Pig")
    }
})
