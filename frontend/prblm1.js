//b=30 for 4km
//for the next 5km the price is 10
//for the next 10km the price is 15
//if the kms are more that will be 20
//person travelled 19.5kms what will be the price


function calculateFare(km) {
  let fare = 0;

  if (km <= 4) {
    fare = 30;
  } else if (km <= 9) {
    fare = 30 + 10;
  } else if (km <= 19) {
    fare = 30 + 10 + 15;
  } else {
    fare = 30 + 10 + 15 + 20;
  }

  return fare;
}
// Example: person travelled 19.5 km
console.log("Fare =", calculateFare(19.5));
