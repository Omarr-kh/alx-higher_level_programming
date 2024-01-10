$.get('https://swapi.co/api/films/?format=json', function (d) {
  $('UL#list_movies').append(...d.results.map(movie => `<li>${movie.title}</li>`));
});
