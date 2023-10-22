const jokeContainer = document.getElementById('joke-container');
const jokeText = document.getElementById('joke-text');
const newJokeButton = document.getElementById('new-joke-button');

async function fetchJoke() {
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random')
    if (!response.ok) {
      throw new Error('Error fetch data from API.')
    }

    const data = await response.json();
    jokeText.textContent = data.value;
  } catch (error) {
    console.log(error);
    jokeText.textContent = 'Failure to find the Joke. Try again.'
  }
}
newJokeButton.addEventListener('click', fetchJoke);

fetchJoke();