const pantalla = document.querySelector(".pantalla");
const botones = document.querySelectorAll(".btn");

botones.forEach(boton => {
    boton.addEventListener("click", () => {
        const botonApretado = boton.textContent;

        if(boton.id === "ac") {
            pantalla.textContent = "0";
            return;
        }

        if(boton.id === "borrar") {
             if (pantalla.textContent.length === 1 || pantalla.textContent === "ERROR!") {
                pantalla.textContent = "0";
            } else {
                pantalla.textContent = pantalla.textContent.slice(0, -1);
            }
            return;
        }
        
        if (boton.id === "cos") {
            let rad = eval(pantalla.textContent) * Math.PI / 180;
            pantalla.textContent = Math.cos(rad).toFixed(9);
            return;
        }
        
        if (boton.id === "tan") {
            let rad = eval(pantalla.textContent) * Math.PI / 180;
            pantalla.textContent = Math.tan(rad).toFixed(9);
            return;
        }
        
        if (boton.id === "potencia") {
            pantalla.textContent += "^";
            return;
        }
        
        if (boton.id === "raiz") {
            pantalla.textContent = Math.sqrt(eval(pantalla.textContent)).toFixed(6);
            return;
        }
        
        if(boton.id === "igual") {
            try {
                let expresion = pantalla.textContent.replace(/\^/g, "**");
                pantalla.textContent = eval(expresion);
            } catch {
                pantalla.textContent = "ERROR!";
            }
            return;
        }
        
        
        if(pantalla.textContent === "0" || pantalla.textContent === "ERROR!") {
            pantalla.textContent = botonApretado;
        } else {
            pantalla.textContent += botonApretado;
        }

    })
})