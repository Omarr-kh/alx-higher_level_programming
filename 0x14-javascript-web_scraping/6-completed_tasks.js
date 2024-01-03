#!/usr/bin/node
const request = require('request');
const urlAPI = process.argv[2];

request.get(urlAPI, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const todos = JSON.parse(body);
  const usersData = {};
  for (const todo of todos) {
    if (!(todo.userId in usersData) && todo.completed) {
      usersData[todo.userId] = 1;
    } else if (todo.completed) {
      usersData[todo.userId] += 1;
    }
  }
  console.log(usersData);
});
