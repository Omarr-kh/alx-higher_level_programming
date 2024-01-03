#!/usr/bin/node

const request = require('request');
const urlAPI = process.argv[2];

request(urlAPI, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completedTasks = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completedTasks === true) {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId]++;
        }
      }
    }
    console.log(completedTasks);
  } else {
    console.log('Error. Status code: ' + response.statusCode);
  }
});
