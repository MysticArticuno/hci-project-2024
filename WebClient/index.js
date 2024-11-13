const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'public')));

// app.get('/kitchen', (req, res) => {
//     con.query("SELECT species FROM rentals ORDER BY species", function (err, result) {
//         const rentals = JSON.stringify(result);
//         res.send(rentals);
//     });
// });

// app.get('/dynamax/bosses', (req, res) => {
//     con.query("SELECT species FROM bosses ORDER BY species", function (err, result) {
//         const bosses = JSON.stringify(result);
//         res.send(bosses);
//     });
// });

// app.get('/dynamax/rentals-full', (req, res) => {
//     con.query("SELECT * FROM rentals ORDER BY species", function (err, result) {
//         const rentals = JSON.stringify(result);
//         res.send(rentals);
//     });
// });

// app.get('/dynamax/bosses-full', (req, res) => {
//     con.query("SELECT * FROM bosses ORDER BY species", function (err, result) {
//         const bosses = JSON.stringify(result);
//         res.send(bosses);
//     });
// });

// app.get('/dynamax/rentals/:species', (req, res) => {
//     const rental = req.params["species"];
//     con.query(`SELECT * FROM rentals WHERE species="${rental}"`, function (err, result) {
//         const newRental = JSON.stringify(result);
//         res.send(newRental);
//     });
// });

// app.get('/dynamax/bosses/:species', (req, res) => {
//     const boss = req.params["species"];
//     con.query(`SELECT * FROM bosses WHERE species="${boss}"`, function (err, result) {
//         const newRental = JSON.stringify(result);
//         res.send(newRental);
//     });
// });

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));