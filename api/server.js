
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

// Makes GET request to get user XP and level
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
  
// Starts the server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});







