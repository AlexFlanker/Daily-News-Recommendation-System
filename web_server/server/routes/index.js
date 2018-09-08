var express = require('express');
var router = express.Router();
var path = require('path');
// var logger = require('logger');
/* GET home page. */
router.get('/', function(req, res, next) {
  // logger.info('Got request for path: \'/\'');
  res.sendFile('index.html', { root: path.join(__dirname, '../../client/build/') });
});

module.exports = router;
