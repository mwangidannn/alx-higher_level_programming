// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

//All movie titles must be list in the HTML tag UL#list_movies
//You can’t use document.querySelector to select the HTML tag
//You must use the JQuery API

let url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  let films = data.results;
  for (let film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
