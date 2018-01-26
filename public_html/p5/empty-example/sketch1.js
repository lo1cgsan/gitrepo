function setup() {
  // put setup code here
  createCanvas(640, 480);
}

function draw() {
  // put drawing code here
  r = random(255);
  g = random(255);
  b = random(255);
  strokeWeight(4);
  fill(r, g, b, 127);
  stroke(r, g, b);
}

function mouseClicked() {
  if (mouseButton === LEFT) {
    rect(mouseX-10, mouseY-10, 20, 20);
  } else {
    ellipse(mouseX-10, mouseY-10, 20, 20);
  }
}
