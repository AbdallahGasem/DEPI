if ("wheel" == n.config.game_type) {
    var c = 450 - 30 * (r + .5);
    n.wheelContainer.classList.add("hktapps-playing"),
    setTimeout((function() {
        n.wheelContainer.style.transform = "rotate(".concat(3600 + c, "deg)"),
        setTimeout((function() {
            n.setWinPrice(o, i, s),
            n.switchPopupScreen("hktapps-screen-win"),
            n.updateContinueButton(i, a),
            n.endPlay()
        }
        ), 1e4)
    }
    ), 1e3)
}
