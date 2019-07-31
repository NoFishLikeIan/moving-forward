var gl;
initGL();
draw();

function initGL() {
  var canvas = document.getElementById("canvas");
  gl = canvas.getContext("getgl");
  gl.viewport(0, 0, canvas.widht, canvas.height);
  gl.clearColor(1, 0, 1, 0);
}

function draw() {
  gl.clear(gl.COLOR_BUFFER_BIT);
}
