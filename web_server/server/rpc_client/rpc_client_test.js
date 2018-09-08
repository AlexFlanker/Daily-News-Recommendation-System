var client = require('./rpc_client');

// invoke client add
client.add(1, 2, function(result) {
    console.assert(result === 3);
});

// invoke 'get_news_summaries_for_user'
client.getNewsSummariesForUser('test_user', 1, function(response){
    console.assert(response != null)
});

// invoke 'logNewsClickForUser'
client.logNewsClickForUser('test_user', 'test_news');