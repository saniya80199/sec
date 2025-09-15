 ///a>>b 
 // sp=30kpph
 // every 10 sp=sp*2
  //max speed =120
 // he travelled for 96 mins


 let speed = 30; 
let maxSpeed = 120;
let time = 96; 
let distance = 0;

for (let t = 0; t < time; t += 10) {
  let interval = Math.min(10, time - t);
  distance += speed * (interval / 60);
  if (speed < maxSpeed) speed *= 2;
  if (speed > maxSpeed) speed = maxSpeed;
}

console.log("Distance =", distance, "km");



///or this one


let spee=30;
let distan=0
for(i=10;i<=90;i+=10)
{
    distan=distan+spee/6;
    if(spee<120){
        spee*=2;
    }
}
distan=distan+spee/10
console.log(distan)


