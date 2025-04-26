
/**
 * @file server.js
 * @author Brendan Dileo, April 2025
 * 
 * Setup for the backend API, handling the routes and interacts with the sqlite database.
 */


// Setup the Express server
const express = require('express');
const sqlite = require('sqlite3').verbose();
const app = express();
const port = 3001;
const cors = require('cors');

// Middleware
app.use(cors());
app.use(express.json());

// Create the database
const db = new sqlite.Database('./xp_system.db', (error) => {
    if (error) {
        console.error('There was an error opening the database: ', error.message);
    } else {
        console.log('Successfully Connected to the SQLite Database!');
    }
});

// Create the table to store user xp data
db.run(`
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        xp FLOAT NOT NULL DEFAULT 0.0,
        level INTEGER NOT NULL DEFAULT 0
    )
`);

// Defines the POST route for adding a user to the database
app.post('/user', (req, res) => {
    const { username } = req.body;
    if (!username) return res.status(400).json({ message: 'Username is required to perform this action!' });

    db.run('INSERT INTO users (username) VALUES (?)', [username], function (err) {
        if (err) return res.status(500).json({ error: err.message });
        res.status(201).json({ id: this.lastID, username, xp: 0.0, level: 0 });
    });
});

// Defines the GET route for retreiving a user by username
app.get('/user/:username', (req, res) => {
    const { username } = req.params;
    db.get('SELECT * FROM users WHERE username = ?', [username], (err, row) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else if (row) {
            res.json(row);
        } else {
            res.status(404).json({ message: 'User not found' });
        }
    });
});

// Defines the PUT route to update the users xp and level
app.put('/user/:username', (req, res) => {
    const { username } = req.params;
    const { xp, level } = req.body;

    db.run(
        'UPDATE users SET xp = ?, level = ? WHERE username = ?',
        [xp, level, username],
        function (err) {
            if (err) return res.status(500).json({ error: err.message });
            if (this.changes == 0) return res.status(404).json({ message: 'User not found!' });
            res.json({ message: 'User updated successfully!' });
        }
    );
});

// Defines the DELETE route for deleting a user
app.delete('/user/:username', (req, res) => {
    const { username } = req.params;

    db.run('DELETE FROM users WHERE username = ?', [username], function (err) {
            if (err) return res.status(500).json({ error: err.message });
            if (this.changes === 0) return res.status(404).json({ message: 'User not found' });
            res.json({ message: 'User deleted successfully' });
        }
    );
});

  
// Starts the server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});







