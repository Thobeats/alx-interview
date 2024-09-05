#!/usr/bin/node
const request = require('request');
const arg = process.argv;

const url = `https://swapi-api.hbtn.io/api/films/${arg[2]}/`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(element => {
      request(element, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
