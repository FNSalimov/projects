var numbers = document.querySelectorAll(".com");
var sixteen;

function compareRandom(a, b) {
	return Math.random() - 0.5;
}

function mix() {
	var appnum = [];
	for (var i = 0; i < 16; i++) {
		appnum.push(i);
	}
	appnum.sort(compareRandom);
	for (var i = 0; i < 15; i++) {
		numbers[appnum[i]].style.backgroundColor = "green";
		numbers[appnum[i]].innerHTML = String(i+1);
	}
	numbers[appnum[15]].style.backgroundColor = "#0565ba";
	numbers[appnum[15]].innerHTML = "";
	sixteen = appnum[15];
}

function check() {
	var flag = true;
	for (var i = 0; i < 15; i++) {
		if (numbers[i].innerHTML != String(i+1)) {
			flag = false;
			break;
		}
	}
	if (flag) {
		var again = confirm("Вы сделали это! :) Хотите поиграть еще?");
		if (again) {
			mix();
		}
	}
}

mix()

function move(e) {
	switch(e.keyCode) {
		case 37:
			if (sixteen != 3 && sixteen != 7 && sixteen != 11 && sixteen != 15) {
				numbers[sixteen].style.backgroundColor = "green";
				numbers[sixteen].innerHTML = numbers[sixteen+1].innerHTML;
				numbers[sixteen+1].style.backgroundColor = "#0565ba";
				numbers[sixteen+1].innerHTML = "";
				sixteen++;
			}
			check();
			break;
		case 38:
			if (sixteen < 12) {
				numbers[sixteen].style.backgroundColor = "green";
				numbers[sixteen].innerHTML = numbers[sixteen+4].innerHTML;
				numbers[sixteen+4].style.backgroundColor = "#0565ba";
				numbers[sixteen+4].innerHTML = "";
				sixteen += 4;
			}
			check();
			break;
		case 39:
			if (sixteen != 0 && sixteen != 4 && sixteen != 8 && sixteen != 12) {
				numbers[sixteen].style.backgroundColor = "green";
				numbers[sixteen].innerHTML = numbers[sixteen-1].innerHTML;
				numbers[sixteen-1].style.backgroundColor = "#0565ba";
				numbers[sixteen-1].innerHTML = "";
				sixteen--;
			}
			check();
			break;
		case 40:
			if (sixteen > 3) {
				numbers[sixteen].style.backgroundColor = "green";
				numbers[sixteen].innerHTML = numbers[sixteen-4].innerHTML;
				numbers[sixteen-4].style.backgroundColor = "#0565ba";
				numbers[sixteen-4].innerHTML = "";
				sixteen -= 4;
			}
			check();
			break;
	}
}

window.addEventListener("keyup", move);
