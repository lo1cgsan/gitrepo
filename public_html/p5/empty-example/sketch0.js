function setup() {
  // put setup code here
  createCanvas(640, 480);
}

function draw() {
  // put drawing code here
  // strokeWeight(5);
  // stroke('#F47A9D');
  // fill(255, 0, 0);
  // ellipse(50, 50, 80, 80);
  //
  // strokeWeight(4);
  // stroke('#79cbf2');
  // fill(0, 255, 0);
  // ellipse(150, 150, 200, 80);
  //
  // strokeWeight(8);
  // stroke('#40b259');
  // fill(0, 0, 255);
  // rect(200, 200, 55, 55);
  noFill();
  noStroke();
  if (mouseIsPressed) {
    if (mouseButton === LEFT) {
      r = random(255);
      g = random(255);
      b = random(255);
      strokeWeight(10);
      fill(r, g, b, 127);
      stroke(r, g, b);
    }
    if (mouseButton === CENTER) {
      strokeWeight(20);
      fill(255, 255, 255);
      stroke(255, 255, 255);
      rect(mouseX-10, mouseY-10, 20, 20);
    }
  } else {
    noFill();
    noStroke();
  }
  point(mouseX, mouseY);
}
