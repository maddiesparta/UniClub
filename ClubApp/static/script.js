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
  
document.getElementById("dark-mode").addEventListener("click", enable_dark_mode);