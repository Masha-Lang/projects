function loaded() {
    // Variablen Deklarieren
    let array = [0, 1, 2, 3, 4, 5, 6, 7, 8];
    let möglichkeiten = [];
    let ergebnis = [];
    let am_besten = [];
    let a;
    let u_array;
    let max_layer = 1;
    let a_max_layer = false;

    anfangen();

    // Wer fängt an?
    function anfangen() {
        if (window.confirm("Möchtest du Anfangen?") == false) {
            c_move();
        }
    }

    // Setze X auf Feld
    function u_move(id) {
        document.getElementById(id).innerHTML = "X";
        c_move();
    }

    // Setze O auf Feld
    function setzte_auf(element) {
        try {
            document.getElementById(element).innerHTML = "O";
        }
        catch {
            alert("Unendschieden");
            nochmal();
        }
        get_array()
        if (gewonnen(array, "O")) {
            alert("O hat gewonnen");
            nochmal();
        }
    }

    // Reset Progress
    function nochmal() {
        if (window.confirm("möchtest du nochmal spielen?")) {
            clear();
            for (i = 0; i < 9; i++) {
                document.getElementById(i).innerHTML = "";
            }
            anfangen();
        }
    }

    // Überprüft, ob das Spiel beendet wurde
    function gewonnen(c_array, player) {
        if (
        (c_array[0] == c_array[1] && c_array[1] == c_array[2] && c_array[2] == player) ||
        (c_array[3] == c_array[4] && c_array[4] == c_array[5] && c_array[5] == player) ||
        (c_array[6] == c_array[7] && c_array[7] == c_array[8] && c_array[8] == player) ||
        (c_array[0] == c_array[3] && c_array[3] == c_array[6] && c_array[6] == player) ||
        (c_array[1] == c_array[4] && c_array[4] == c_array[7] && c_array[7] == player) ||
        (c_array[2] == c_array[5] && c_array[5] == c_array[8] && c_array[8] == player) ||
        (c_array[0] == c_array[4] && c_array[4] == c_array[8] && c_array[8] == player) ||
        (c_array[2] == c_array[4] && c_array[4] == c_array[6] && c_array[6] == player)
        ) {
            return true;            
        }
    }

    // Alle möglichkeiten anzeigen
    function alle_möglichkeiten(c_array) {
        möglichkeiten = [];
        for (let j of array) {
            if (j != "X" && j != "O") {
                möglichkeiten.push(array[j]);
            }
        }
    }

    // Besten Zug für O berechnen
    function bester_zug(c_array, player, layer) {
        alle_möglichkeiten(c_array);
        if (gewonnen(c_array, "X")) {
            return -1;
        }
        else if (gewonnen(c_array, "O")) {
            return 1;
        }
        if (möglichkeiten.length == 0) {
            return 0;
        }

        for (let j of möglichkeiten) {
            c_array[j] = player
            if (player == "O") {
                a = {layer: layer, score: bester_zug(c_array, "X", layer + 1)};
            }
            else {
                a = {layer: layer, score: bester_zug(c_array, "O", layer + 1)};
            }
            c_array[j] = j;
            if (a.score != 10) {
                if (a.score < 0) {
                    a.score *= (a_max_layer - a.layer) + 1;
                }
                else {
                    a.score *= (a_max_layer - a.layer) + 1;
                }
            }
            ergebnis.push(a);
            if (layer > max_layer) {
                max_layer = layer;
            }
            if (JSON.stringify(u_array) === JSON.stringify(c_array)) {
                // Für jeden Layer
                for (i = max_layer; i > 0; i--) {
                    let min = Infinity;
                    let max = -Infinity;
                    // Für jedes Element in Ergebnis
                    for (k = 0; k < ergebnis.length; k++) {
                        if (ergebnis[k].layer == i-1 && ergebnis[k].score == 10) {
                            if (min == Infinity) {
                                ergebnis[k].score = max;
                            }
                            else {
                                ergebnis[k].score = min;
                            }
                            min = Infinity;
                            max = -Infinity;
                        }
                        if (ergebnis[k].layer == i) {
                            if (i % 2) { // O ist am Zug
                                if (ergebnis[k].score > max) {
                                    max = ergebnis[k].score;
                                }
                            }
                            else { // X ist am Zug
                                if (ergebnis[k].score < min) {
                                    min = ergebnis[k].score;
                                }
                            }
                        }
                    }
                    if (min == Infinity) {
                        ergebnis.push({layer: i-1, score: max});
                    }
                    else {
                        ergebnis.push({layer: i-1, score: min});
                    }
                }
                am_besten.push(ergebnis.pop().score);
                max_layer = 1;
                ergebnis = [];
            }
        }
        return 10;
    }

    // Alle Felder Einlesen und Speichern
    function get_array() {
        for (i = 0; i < 9; i++) {
            if (document.getElementById(i).innerHTML != "") {
                array[i] = document.getElementById(i).innerHTML;
            }
        }
    }

    // Variablen auf Standartwerte zurücksetzen
    function clear() {
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8];
        möglichkeiten = [];
        ergebnis = [];
        am_besten = [];
        max_layer = 1;
    }

    // Computer am Zug
    function c_move() {
        get_array();
        u_array = array.slice();
        a_max_layer = u_array.filter(e => e !== 'X' && e !== 'O').length;
        bester_zug(array, "O", 1);
        u_array = u_array.filter(e => e !== 'X' && e !== 'O');
        setzte_auf(u_array[am_besten.indexOf(Math.max(...am_besten))]);
        clear();
    }

    // X ist am Zug
    document.querySelectorAll("#feld button").forEach(feld => {
        feld.addEventListener("click", function variable() {
            u_move(feld.getAttribute("id"));
        })
    });
}