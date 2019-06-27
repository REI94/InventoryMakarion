const express = require('express');
const router = express.Router();

//Pool hace referencia a la conexión de la base de datos
const pool = require('../database');

router.get('/add', (req, res) =>{
    res.render('links/add');
});

router.post('/add', async (req, res) => {
    const {nombre, apellido, tipodi, numdi, edad, telefono, direccion, email, contrasenia} = req.body;
    const cliente = {
        nombre,
        apellido,
        tipodi,
        numdi,
        edad,
        telefono,
        direccion,
        email,
        contrasenia
    };
    //console.log(newLink);
    await pool.query('INSERT INTO clientes set ?', [cliente]);
    //res.render('links/index.hbs');
    res.redirect('/links/index');
});

router.get('/index', async (req, res) =>{
    //const clientes = await pool.query('SELECT * FROM clientes');
    console.log('¡Bienvenido!');
    res.render('links/index');
});

module.exports = router;