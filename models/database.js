/**
 * Use pg to set up the database connection
 */
var pg = require('pg');
var dbUrl = process.env.DATABASE_URL | 'postgres://localhost:5432/food';

var client = new pg.Client(dbUrl);
client.connect();

module.exports = client;