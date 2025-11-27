var isDark = false;
function enable_dark_mode() {
        if (isDark) {
            var element = document.body;
            element.classList.remove("dark-mode-background");
            element.classList.remove("dark-mode-text");

            var h3s = document.getElementsByTagName("h3");
            for (const h3 of h3s) {
                h3.classList.remove("dark-mode-text");
            }

            var h1s = document.getElementsByTagName("h1");
            for (const h1 of h1s) {
                h1.classList.remove("dark-mode-text");
            }

            var element = document.getElementById("logo");
            element.classList.remove("dark-mode-background");

            var element = document.getElementById("header");
            element.classList.remove("dark-mode-background-lighter");

            var element = document.getElementById("uniclub-title");
            element.classList.remove("dark-mode-text")

            var element = document.getElementById("menubar");
            element.classList.remove("dark-mode-background")

            var element = document.getElementById("dark-mode");
            element.textContent = "Modo oscuro"

        } else {
            var element = document.body;
            element.classList.add("dark-mode-background");
            element.classList.add("dark-mode-text");

            var h3s = document.getElementsByTagName("h3");
            for (const h3 of h3s) {
                h3.classList.add("dark-mode-text");
            }

            var h1s = document.getElementsByTagName("h1");
            for (const h1 of h1s) {
                h1.classList.add("dark-mode-text");
            }

            var element = document.getElementById("logo");
            element.classList.add("dark-mode-background");

            var element = document.getElementById("header");
            element.classList.add("dark-mode-background-lighter");

            var element = document.getElementById("uniclub-title");
            element.classList.add("dark-mode-text")

            var element = document.getElementById("menubar");
            element.classList.add("dark-mode-background")

            var element = document.getElementById("dark-mode");
            element.textContent = "Modo claro"
        }
    
        isDark = !isDark
      }
  

console.log("hola")      
document.getElementById("dark-mode").addEventListener("click", enable_dark_mode);


async function getWeather(){
    let response = await fetch ('https://api.open-meteo.com/v1/forecast?latitude=43.2627&longitude=-2.9253&hourly=temperature_2m&models=ecmwf_ifs&forecast_days=1')
    let data= await response.json()
    let temperatures = data.hourly.temperature_2m
    console.log(temperatures)
    

    var six_morning = document.getElementById("six")
    six_morning.textContent = "6:00: " + temperatures[6] + "ºC"

    var ten = document.getElementById("ten")
    ten.textContent = "10:00: " + temperatures[10] + "ºC"

    var two = document.getElementById("two")
    two.textContent = "14:00: " + temperatures[14] + "ºC"
    
    var six_evening = document.getElementById("six_e")
    six_evening.textContent = "18:00: " + temperatures[18] + "ºC"

}

// let arrayTemperatures = [temperatures[6],temperatures[10],temperatures[14], temperatures[18]]

let weather_array = getWeather()

