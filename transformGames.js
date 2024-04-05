const games = require('./games.json');

// var newGames = {}

const newGames = games.results.map(game => {
    let currentGame = {};
    currentGame["name"] = game.name;
    currentGame["image"] = game.background_image;
    currentGame["platforms"] = game.parent_platforms.map(({ platform }) => {
        return platform.name;
    });
    currentGame["screenshots"] = game.short_screenshots.map(print => {
        return print.image;
    });
    return currentGame;
})
console.log("🚀 ~ games:", JSON.stringify(newGames))

