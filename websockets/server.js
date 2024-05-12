const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const mysql = require('mysql');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Conexión a la base de datos MySQL
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'chat_db'
});

db.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Conexión a la base de datos establecida');
});

io.on('connection', (socket) => {
    console.log('Cliente conectado');

    socket.on('disconnect', () => {
        console.log('Cliente desconectado');
    });

    socket.on('mensaje', (mensaje) => {
        console.log('Mensaje recibido:', mensaje);
        io.emit('mensaje', mensaje); // Enviar el mensaje a todos los clientes conectados

        // Guardar el mensaje en la base de datos
        const sql = "INSERT INTO mensajes (mensaje) VALUES (?)";
        db.query(sql, [mensaje], (err, result) => {
            if (err) throw err;
            console.log("Mensaje guardado en la base de datos");
        });
    });
});

server.listen(3000, () => {
    console.log('Servidor escuchando en el puerto 3000');
});
