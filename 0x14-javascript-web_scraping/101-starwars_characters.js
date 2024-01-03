#!/usr/bin/node

const request = require('request');
const urlAPI = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(urlAPI, function (error, response, body) {
  if (!error) {
    const movieCharacters = JSON.parse(body).movieCharacters;
    printChars(movieCharacters, 0);
  }
});

function printChars(movieCharacters, i) {
  request(movieCharacters[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i + 1 < movieCharacters.length) {
        printChars(movieCharacters, i + 1);
      }
    }
  });
}
