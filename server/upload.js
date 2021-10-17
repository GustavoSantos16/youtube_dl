const uploadYT = require('upload-youtube');

(async () => {
    const email = "email"
    const password = "senha"
    await uploadYT.loginByParams(email, password);
    const ytID = await uploadYT.uploadVideoToYoutube(
        "./cookies-" + email + ".json",
        "./video.mp4",
        "",
        {
            title: "Example Title",
            description: "Example Description",
            keywords: ["keywords1", "keywords2"],
            playlist: "Playlist Name",
        }
    )
    console.log(`Upload success: https://youtu.be/${ytID}`)
})()