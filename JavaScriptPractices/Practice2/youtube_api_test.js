const request = require('request-promise')
const q = require('q')

var video_list = [];

/*Discord bot testing to print youtube videos of channel 
with the objective to build a bot for discord*/
(async() => {

    var page_token = '';

    for (;;){
        var url = 'youtube_api_url_with'

        if (page_token){
            url += '&pageToken' + page_token;
        }
        var videos = await request({
            method: 'get',
            url: url,
            json: true,
            simple: true
        });

        page_token = videos.nextPageToken;
    
        videos.items.forEach(video => {
            video_list.push({
                id: video.id.videoId,
                title: video.snippet.title
            });
        });

        if (!page_token) break;
    }

    video_list = video_list
        .filter(video => {
                return !!~video.title.to_lower_case().index_of(term.to_lower_case())
        });
    
        
        if (video_list.length === 0){
            //message.reply('no videos found for: ' + term);
        }else if (video_list.length === 1){
            //message.reply ('i found a good video: https:// https://www.youtube.com/watch?v=' + video.id)
        }else{
            var msg = 'i found several videos:';
            video_list.forEach(video =>{
                msg += 'https://www.youtube.com/watch?v=' + video.id + '\n';
            });
            //message.reply(msg)
        }
})();


