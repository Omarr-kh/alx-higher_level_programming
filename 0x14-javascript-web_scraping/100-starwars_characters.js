#!/usr/bin/node

const req = require('request');
const userID = process.argv[2];
const urlAPI = 'https://swapi-api.hbtn.io/api/films/';
req.get(urlAPI + userID, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const charactersData = data.characters;
    for (const i of charactersData) {
      req.get(i, (error, response, body2) => {
        if (error) {
          console.log(error);
        }
        const data2 = JSON.parse(body2);
        console.log(data2.name);
      });
    }
  }
});
