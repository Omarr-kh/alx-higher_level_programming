#!/usr/bin/node

const request = require('request');
const urlAPI = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(urlAPI, (error, response, body) => {
  if (!error) {
    const movieCharacters = JSON.parse(body).movieCharacters;
    print(movieCharacters, 0);
  }
});

function print (movieCharacters, i) {
  request(movieCharacters[i], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i + 1 < movieCharacters.length) {
        print(movieCharacters, i + 1);
      }
    }
  });
}
