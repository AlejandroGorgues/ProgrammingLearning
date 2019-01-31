const request = require('request-promise');
const q = require('q');

//Function that calculates avg of flipkey prices of 4 pages in async mode
/**
    (async function(){
    var total_results = [];    
    for (var i = 1; i < 4; i++) {
            var results = await request({
                method: 'get',
                url: 'https://flipkey.com/content/srp/srp_fk/index_json/book/destin/222604340//zoom.11?page'+i,
                json: true,
                simple:true
            });
            total_results = total_results.concat(results.results);
            
    }
        var daily_prices = total_results
            .map(r => r.dailyPrice)
            .filter(r => {
                if (!r) return false;
                return true;
            })
            .map (r => {
    
                r = +r.replace(/[^0-9]/gi, '');
                
                return r;
            });
        
        var sum = daily_prices.reduce((a, b) => a + b);
        console.log('calculation based on ' + daily_prices.length + ' values');
        console.log(sum / daily_prices.length)
    })();
*/

//Function that calculates avg of flipkey prices of 4 pages without async and promise chaining

    var total_results = [];    

    var chain = q.fcall(() => {});
    for (var i = 1; i < 4; i++) {
        chain = chain
            .then(() =>{
                return request({
                    method: 'get',
                    url: 'https://flipkey.com/content/srp/srp_fk/index_json/book/destin/222604340//zoom.11?page'+i,
                    json: true,
                    simple:true
                })
                .then(results => { 
                    total_results = total_results.concat(results.results);
                    return null;
                });
            });      
    }

    return chain
        .then(() => {
            var daily_prices = total_results
            .map(r => r.dailyPrice)
            .filter(r => {
                if (!r) return false;
                return true;
            })
            .map (r => {
    
                r = +r.replace(/[^0-9]/gi, '');
                
                return r;
            });
        
        var sum = daily_prices.reduce((a, b) => a + b);
        console.log('calculation based on ' + daily_prices.length + ' values');
        console.log(sum / daily_prices.length)
        });
        
