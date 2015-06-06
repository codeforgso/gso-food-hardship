var express = require('express');
var router = express.Router();
var db = require('../models/database');
var fs = require('fs');

/* GET home page. */

router.get('/', function(req, res) {
	var geoData = fs.readFileSync('./test-data/data.txt'); // replace this with query

  	res.render('index', { title: 'Express', geoData: geoData});
});

module.exports = router;
