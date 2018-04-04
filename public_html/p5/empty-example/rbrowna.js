szerokosc = 840;
wysokosc = 480;

xprzes = szerokosc / 2;
yprzes = wysokosc / 2;

n = prompt("Ilość ruchów:", 50);
x = y = 0;
lx = [0];
ly = [0];
krok = 30;

function getRnd(min, max) {
	return Math.random() * (max - min) + min;
}

for (i = 0; i < n; i++) {
    rad = Math.floor(getRnd(0, 360)) * Math.PI / 180;
		x = x + Math.cos(rad) * krok;
    y = y + Math.sin(rad) * krok;
    // console.log(x);
    // console.log(y);
    lx[i] = x;
    ly[i] = y;
}

// console.log(ly);

function setup() {
  createCanvas(szerokosc, wysokosc);
  background('#fff');
	stroke('#000');
  line(szerokosc / 2, 0, szerokosc / 2, wysokosc);
  line(0, wysokosc / 2, szerokosc, wysokosc / 2);
}

function draw() {
	stroke('#000');
	for (i = 0; i < n; i++) {
		console.log(lx[i], ly[i]);
		line(lx[i] + xprzes, ly[i] + yprzes, lx[i+1] + xprzes, ly[i+1] + yprzes);
	}
}
