const fs = require('fs');
const ytdl = require('ytdl-core');

// Download video youtube
ytdl('https://www.youtube.com/watch?v=D26bLJ9ut88',{filter: 'audioandvideo', quality: 'highestvideo'})
.pipe(fs.createWriteStream('video.mp4'));


