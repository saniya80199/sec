// //json
// console.log("=== json basics ===");

// let student={
//     name:"saniya",
//     age:1,
//     marks:[85,90,78]
// };

// //convert object to json string
//  let jsonstring=JSON.stringify(student);
//  console.log("JSON STRING:",jsonstring);

// //convert json string to object
// let parseobj=JSON.parse(jsonstring);
// console.log("parsed object:",parseobj);
 
// let book1={
//     title:"self love",
//     price:1000,
//     authname:"saniya"
// };
//  let jsonstr=JSON.stringify(book1);
//  console.log("JSON STRING:",jsonstr);
// //convert json string to object
// let parsedbj=JSON.parse(jsonstr);
// console.log("parsed object:",parsedbj);

// let books=[
//     {
//       title:"self love1",
//     price:1000,
//     authname:"saniya"
//     },
//     {
//         title:"self love2",
//     price:1000,
//     authname:"saniya"
//     },
//     {
//         title:"self love3",
//     price:1000,
//     authname:"saniya"
//     }
// ];

// console.log("books title:",books.map(b=>b.title));

// console.log("Ajax With Fetch");
// //output wii be one one 
// fetch("https://jsonplaceholder.typicode.com/posts/1")
//    .then(response=> response.json())
//    .then(data =>console.log("fetched data:",data))
//    .catch(error=> console.error("error:",error))

// //output will be more if we removw 1 from last in the below link
// fetch("https://jsonplaceholder.typicode.com/posts/")
//    .then(response=> response.json())
//    .then(data =>console.log("fetched data:",data))
//    .catch(error=> console.error("error:",error))


// //display json daata in webpage
// //fetch all users ands how to console + page
// fetch("https://jsonplaceholder.typicode.com/users")
//     .then(res => res.json())
//     .then(users => {
//         let output="<h3>user List</h3><ul>";
//         users.forEach(user => {
//             output += `<li>${user.name} - ${user.email}</li>`;
            
//         });
//         output += "</ul>";
//         //append result to page
//         document.body.innerHTML+=output;
//     } );


//     //weather info fetcher project
//     console.log("===weather info fetcher project===");


    //predefined city + coordinates


// Predefined city → coordinates
const cityCoords = {
  "bangalore": { lat: 12.97, lon: 77.59 },
  "delhi": { lat: 28.61, lon: 77.20 },
  "mumbai": { lat: 19.07, lon: 72.87 },
  "london": { lat: 51.51, lon: -0.13 },
  "new york": { lat: 40.71, lon: -74.01 }
};


// Event Listener for button
document.getElementById("fetchBtn").addEventListener("click", () => {
  let city = document.getElementById("cityInput").value.toLowerCase();

    if (!cityCoords[city]) {
    document.getElementById("weather").innerHTML = "⚠️ City not in list!";
    return;
  }

  let coords = cityCoords[city];
  let url = `https://api.open-meteo.com/v1/forecast?latitude=${coords.lat}&longitude=${coords.lon}&current_weather=true`;

  // AJAX Fetch
  fetch(url)
    .then(res => res.json())
    .then(data => {
      if (data.current_weather) {
        document.getElementById("weather").innerHTML = `
          <h3>Weather in ${city}</h3>
          <p>🌡 Temp: ${data.current_weather.temperature}°C</p>
          <p>💨 Wind: ${data.current_weather.windspeed} km/h</p>
          <p>⏱ Time: ${data.current_weather.time}</p>
        `;
      } else {
        document.getElementById("weather").innerHTML = "⚠️ No data available.";
      }
    })
    .catch(error => {
      console.error(error);
      document.getElementById("weather").innerHTML = "⚠️ Error fetching weather.";
    });
});


//use this and try
//https://newsapi.org/v2/everything?q=tesla&from=2025-08-12&sortBy=publishedAt&apiKey=5529ea051c742eaa88d6e1a86c6d788/