var contactListInstance = new Vue({
    el: "#contactos",
    data: {
        test: "hola",
        contactos: [
        {nombre: "Markel", email: "markel@markel.markel", tlf: 611462401},
        {nombre: "Naia", email: "naia@naia.naia", tlf: 43848343},
        {nombre: "Maddi", email: "maddi@maddi.maddi", tlf: 3828323},
        {nombre: "Sergio", email: "sergio@sergio.sergio", tlf: 138238}, 
        {nombre: "Josu", email: "josu@josu.josu", tlf: 32332323}, 
        ]
    },
    methods: {
       eliminarContacto: function(index, event) {
            this.contactos.splice(index, 1);
        }         
    }
});

var createContactInstance = new Vue({
    el: "#crear-contacto",
    data: {
        nombre: '',
        email: '',
        tlf: '',
        test: 'adios'
    },
    methods: {
        crearContacto: function(event) {
            this.test = "Holaa!"
            contactListInstance.contactos.push({"nombre": this.nombre, "email": this.email, "tlf": this.tlf})
        }
    }
});