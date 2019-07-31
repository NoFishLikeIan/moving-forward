let G = 9.764
let l1 = 1.0
let l2 = 1.0
let m1 = 2.0
let m2 = 2.0

function theta1dot(theta1, theta2, p1,p2) {
    const derivative = (p1*l2 - p2*l1+Math.cos(theta1 - theta2)) / (l1**2 * l2 *(m1 + m2*Math.sin(theta1 - theta2)**2))
    return derivative;
}

function theta2dot(theta1, theta2, p1,p2) {
    const derivative = (p2*(m1+m2)*l1 - p1*m2*l2*Math.cos(theta1 - theta2))/(m2*l1*l2**2*(m1 + m2*Math.sin(theta1 - theta2)**2))
    return derivative;
}

function p1dot(theta1, theta2, p1, p2) {
    var A1 = (p1*p2*Math.sin(theta1-theta2)) / (l1*l2*(m1+m2*Math.sin(theta1-theta2)**2)),
     A2 = (p1**2*m2*l2**2 - 2*p1*p2*m2*l1*l2*Math.cos(theta1 - theta2) + p2**2*(m1 + m2)*l1**2)*Math.sin(2*(theta1 - theta2))/(2*l1**2*l2**2*(m1 + m2*Math.sin(theta1 - theta2)**2)**2);

    return -(m1 + m2)*G*l1*Math.sin(theta1) - A1 + A2;
}

function p2dot(theta1, theta2, p1, p2) {
    var A1 = (p1*p2*Math.sin(theta1 - theta2))/(l1*l2*(m1 + m2*Math.sin(theta1 - theta2)**2)),
        A2 = (p1**2*m2*l2**2 - 2*p1*p2*m2*l1*l2*Math.cos(theta1 - theta2) + p2**2*(m1 + m2)*l1**2)*Math.sin(2*(theta1 - theta2))/(2*l1**2*l2**2*(m1 + m2*Math.sin(theta1 - theta2)**2)**2);
    return -m2*G*l2*Math.sin(theta2) + A1 - A2;
  }

function f(Z) {
    return [theta1dot(Z[0], Z[1], Z[2], Z[3]), theta2dot(Z[0], Z[1], Z[2], Z[3]), p1dot(Z[0], Z[1], Z[2], Z[3]), p2dot(Z[0], Z[1], Z[2], Z[3])]
}

function RK4(Z_n, f, tau) {
    Array.prototype.scalarMultiply = function(x) { return this.map(function(d) { return x * d; }); }
  
    var Y1 = f(Z_n).scalarMultiply(tau);
    var Y2 = f([Z_n[0] + 0.5*Y1[0], Z_n[1] + 0.5*Y1[1], Z_n[2] + 0.5*Y1[2], Z_n[3] + 0.5*Y1[3]]).scalarMultiply(tau);
    var Y3 = f([Z_n[0] + 0.5*Y2[0], Z_n[1] + 0.5*Y2[1], Z_n[2] + 0.5*Y2[2], Z_n[3] + 0.5*Y2[3]]).scalarMultiply(tau);
    var Y4 = f([Z_n[0] + Y3[0], Z_n[1] + Y3[1], Z_n[2] + Y3[2], Z_n[3] + Y3[3]]).scalarMultiply(tau);
  
    return [
      Z_n[0] + Y1[0]/6 + Y2[0]/3 + Y3[0]/3 + Y4[0]/6,
      Z_n[1] + Y1[1]/6 + Y2[1]/3 + Y3[1]/3 + Y4[1]/6,
      Z_n[2] + Y1[2]/6 + Y2[2]/3 + Y3[2]/3 + Y4[2]/6,
      Z_n[3] + Y1[3]/6 + Y2[3]/3 + Y3[3]/3 + Y4[3]/6,
    ];
}

Zs = {
    var Z = [theta1, theta2, p1, p2],
        oldZ = Z;
  
    const initialRange = 10**-closeness;
    var deltas = d3.range(-initialRange/2, initialRange/2,initialRange/nPendula);
    var Zs = deltas.map(x=>[Z[0],Z[1]+x,Z[2],Z[3]])
    while(true) {
      yield Zs = Zs.map(Z=>RK4(Z, f, 1/60));
    }
  }


    const getCoords = function(Z) {
      return  {
        'x1':l1*Math.sin(Z[0]),
        'y1':l1*Math.cos(Z[0]),
        'x2':l1*Math.sin(Z[0]) + l2*Math.sin(Z[1]),
        'y2':l1*Math.cos(Z[0]) + l2*Math.cos(Z[1])
      };
    }
  
    const height = 500;
    const width = 500;
    const color = d3.scaleSequential(d3.interpolateRainbow).domain([0, nPendula]);
    
    const context = DOM.context2d(width, height);
    const canvas = context.canvas;
    
    const scale = d3.scaleLinear().domain([0,1]).range([0,100]);
    const massScale = d3.scaleSqrt().domain([1,10]).range([3,10]);
    
      var coords = Zs.map(Z=>getCoords(Z));
      
      for (var i=coords.length-1;i>=0;i--) {
        context.beginPath();
        context.strokeStyle=color(i);
        context.lineWidth=2;
        context.moveTo(width/2, height/2);
        context.lineTo(scale(coords[i].x1) + width/2, scale(coords[i].y1) + height/2);
        context.lineTo(scale(coords[i].x2) + width/2, scale(coords[i].y2) + height/2);
        context.stroke();
        context.beginPath();
        context.fillStyle=color(i);
        context.arc(scale(coords[i].x1) + width/2, scale(coords[i].y1) + height/2,massScale(m1),0,6.28);
        context.arc(scale(coords[i].x2) + width/2, scale(coords[i].y2) + height/2,massScale(m2),0,6.28);
        context.fill();
      }
    
    return canvas;
  }Zs = {
    var Z = [theta1, theta2, p1, p2],
        oldZ = Z;
  
    const initialRange = 10**-closeness;
    var deltas = d3.range(-initialRange/2, initialRange/2,initialRange/nPendula);
    var Zs = deltas.map(x=>[Z[0],Z[1]+x,Z[2],Z[3]])
    while(true) {
      yield Zs = Zs.map(Z=>RK4(Z, f, 1/60));
    }