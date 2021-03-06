var express = require('express');
var router = express.Router();
// var logger = require('logger/logger');
var rpc_client = require('../rpc_client/rpc_client');
/* GET news summary list. */
router.get('/userId=:userId&pageNum=:pageNum', function(req, res, next) {
    user_id = req.params['userId'];
    page_num = req.params['pageNum'];

    rpc_client.getNewsSummariesForUser(user_id, page_num, function(response){
        res.json(response);
    });
});

/* Log News Click Event. */
router.post('/user_Id=:userId&newsId=:newsId', function(req, res, next) {
    console.log('Logging news click...');
    var user_id = req.params['userId'];
    var news_id = req.params['newsId'];

    rpc_client.logNewsClickForUser(user_id, news_id);
    res.status(200);
});

module.exports = router;