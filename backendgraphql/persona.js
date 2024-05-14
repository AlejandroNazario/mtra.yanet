const mongoose = require("mongoose");

const personaScheam = mongoose.Schema({
  nombre:String,
  apellidos:String,
  edad:String,
  pais:String
});
const personaModel = mongoose.model("personas", personaScheam);
module.exports = personaModel;

