//opgave 1
/*
const tall1 = parseInt(prompt("skriv inn det første tallet:"));
const tall2 = parseInt(prompt("skriv inn det andre tallet:"));
const operasjon = prompt("skriv inn operasjonen du ønsker å utføre (+, -, *, /):");

if (operasjon === "+") {
    console.log(tall1 + tall2);
} else if (operasjon === "-") {
    console.log(tall1 - tall2);
} else if (operasjon === "*") {
    console.log(tall1 * tall2);
} else if (operasjon === "/") {
    console.log(tall1 / tall2);
} else {
    console.log("Ugyldig operasjon");
}
*/

//opgave 2
/*
const lengde = parseInt(prompt("skriv inn lengden i cm:"));
const bredde = parseInt(prompt("skriv inn bredden i cm:"));

const areal = lengde * bredde;
const omkrets = 2 * (lengde + bredde);

console.log("areal:", areal);
console.log("omkrets:", omkrets);
*/

//opgave 3
const navn = prompt("skriv inn ditt navn:");
const alder = parseInt(prompt("skriv inn din alder:"));
const årtilhundre = 100 - alder;
alert(navn + " har " + årtilhundre + " år til hundre.");