#!/usr/bin/node
const request = require('request');
const arg = process.argv;

const url = `https://swapi-api.hbtn.io/api/films/${arg[2]}/`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  }
});
