import express from "express";

const app = express();
const port = 4000;
const masterKey = "1VGP2DN-6EWM4SJ-D6FGRHV-Z3PR3TT";

app.use(express.urlencoded({ extended: true }))
app.use(express.json());

// GET http://localhost:4000/movies to get all the list of movies
app.get("/movies", (req, res) => {
    console.log(movies);
    res.json(movies);
});

// GET http://localhost:4000/movies/1 to get the movie with specific ID
app.get("/movies/:id", (req, res) => {
    const id = parseInt(req.params.id);
    const foundMovie = movies.findIndex((movie) => movie.id === id)
    if (foundMovie !== undefined) {
      console.log(movies[foundMovie]);
      res.json(movies[foundMovie]);
    } else {
        res.status(404).json({ error: "Movie not found" });
    }
});

// GET http://localhost:4000/random to get a random movie
app.get("/random", (req, res) => {
    const randomIndex = Math.floor(Math.random() * movies.length) + 1;
    const randomMovie = movies.find((movie) => movie.id === randomIndex);
    console.log(randomMovie);
    res.json(randomMovie);
});

// POST http://localhost:4000/post to post a movie to the movies array
app.post("/post", (req, res) => {
    const postId = movies.length + 1;
    const newPost = {
      id: postId,
      movieName: req.body.movie,
      description: req.body.description,
      releaseDate: req.body.date
    }
    movies.push(newPost);
    console.log(newPost);
    res.status(201).json(newPost);
});

// PATCH http://localhost:4000/alterPost/1 to alter a movie (you can either alter all of it, or some of it)
app.patch("/alterPost/:id", (req, res) => {
  const alterPostId = parseInt(req.params.id);
  const foundAlterPost = movies.findIndex((movie) => movie.id === alterPostId);
  if (foundAlterPost !== -1) {
    movies[foundAlterPost] = {
      id: alterPostId,
      movieName: req.body.movie || movies[foundAlterPost].movieName,
      description: req.body.description || movies[foundAlterPost].description,
      releaseDate: req.body.date || movies[foundAlterPost].releaseDate
    }
    res.status(200).json({ message: 'Post altered successfully', alteredPost: movies[foundAlterPost]});
  }
  else {
    res.status(404).json({ message: 'Post not found' });
  }
});

// PUT http://localhost:4000/updatePost/1 to update a movie (you need to update every property)
app.put("/updatePost/:id", (req, res) => {
  const updatePostId = parseInt(req.params.id);
  const foundUpdatePost = movies.findIndex((movie) => movie.id === updatePostId);
  if (foundUpdatePost !== -1 && req.body.movie && req.body.description && req.body.date) {
    movies[foundUpdatePost] = {
      id: updatePostId,
      movieName:  req.body.movie,
      description:  req.body.description,
      releaseDate:  req.body.date
    }
    res.status(200).json({ message: 'Post updated successfully', updatedPost: movies[foundUpdatePost]});
  }
  else {
    res.status(404).json({ message: 'error has occured' });
  }
});

// DELETE http://localhost:4000/deletedPost/1 to delete a post with a specified ID
app.delete("/deletePost/:id", (req, res) => {
  const deletedPost = movies.findIndex((movie) => movie.id === parseInt(req.params.id));
  if (deletedPost === -1) {
    res.status(404).json({ message: "Post not found" });
  }
  movies.splice(deletedPost, 1);
  res.json({ message: "Post deleted" });
});

// DELETE http://localhost:4000/deleteAll?key=1VGP2DN-6EWM4SJ-D6FGRHV-Z3PR3TT used to delete every single movie that is held in array (this action can only be performed with the key 1VGP2DN-6EWM4SJ-D6FGRHV-Z3PR3TT)
app.delete("/deleteAll", (req, res) => {
  const userKey = req.query.key;
  if (userKey === masterKey) {
    movies = [];
    res.sendStatus(200);
  } else {
    res.status(404).json({ error: `You are not authorised to perform this action.` });
  }
});

app.listen(port, () => { console.log( `API is running on port ${port}.` )});

let movies = [
    {
      id: 1,
      movieName: "Inception",
      description: "A mind-bending science fiction thriller directed by Christopher Nolan.",
      releaseDate: "2010-07-16"
    },
    {
      id: 2,
      movieName: "The Shawshank Redemption",
      description: "A classic drama film based on Stephen King's novella, directed by Frank Darabont.",
      releaseDate: "1994-09-23"
    },
    {
      id: 3,
      movieName: "The Dark Knight",
      description: "A superhero film directed by Christopher Nolan, featuring Batman and the Joker.",
      releaseDate: "2008-07-18"
    },
    {
      id: 4,
      movieName: "Pulp Fiction",
      description: "A cult classic crime film directed by Quentin Tarantino.",
      releaseDate: "1994-10-14"
    },
    {
      id: 5,
      movieName: "Forrest Gump",
      description: "A heartwarming drama film directed by Robert Zemeckis.",
      releaseDate: "1994-07-06"
    },
    {
      id: 6,
      movieName: "The Matrix",
      description: "A groundbreaking science fiction film directed by the Wachowskis.",
      releaseDate: "1999-03-31"
    },
    {
      id: 7,
      movieName: "Schindler's List",
      description: "A historical drama film directed by Steven Spielberg, based on the novel by Thomas Keneally.",
      releaseDate: "1993-11-30"
    },
    {
      id: 8,
      movieName: "Titanic",
      description: "A romantic drama film directed, written, co-produced, and co-edited by James Cameron.",
      releaseDate: "1997-12-19"
    },
    {
      id: 9,
      movieName: "Fight Club",
      description: "A psychological thriller film directed by David Fincher, based on the novel by Chuck Palahniuk.",
      releaseDate: "1999-10-15"
    },
    {
      id: 10,
      movieName: "The Lord of the Rings: The Fellowship of the Ring",
      description: "An epic fantasy adventure film directed by Peter Jackson, based on J.R.R. Tolkien's novel.",
      releaseDate: "2001-12-19"
    },
    {
      id: 11,
      movieName: "The Godfather",
      description: "A crime film directed by Francis Ford Coppola, based on the novel by Mario Puzo.",
      releaseDate: "1972-03-14"
    },
    {
      id: 12,
      movieName: "The Godfather: Part II",
      description: "A sequel to The Godfather, directed by Francis Ford Coppola.",
      releaseDate: "1974-12-20"
    },
    {
      id: 13,
      movieName: "The Godfather: Part III",
      description: "The final installment in The Godfather trilogy, directed by Francis Ford Coppola.",
      releaseDate: "1990-12-25"
    },
    {
      id: 14,
      movieName: "Goodfellas",
      description: "A crime film directed by Martin Scorsese, based on the book Wiseguy by Nicholas Pileggi.",
      releaseDate: "1990-09-09"
    },
    {
      id: 15,
      movieName: "Casablanca",
      description: "A romantic drama film directed by Michael Curtiz, set during World War II.",
      releaseDate: "1942-11-26"
    },
    {
      id: 16,
      movieName: "Star Wars: Episode IV - A New Hope",
      description: "The original Star Wars film directed by George Lucas.",
      releaseDate: "1977-05-25"
    },
    {
      id: 17,
      movieName: "Saving Private Ryan",
      description: "A war film directed by Steven Spielberg, set during the invasion of Normandy in World War II.",
      releaseDate: "1998-07-24"
    },
    {
      id: 18,
      movieName: "The Silence of the Lambs",
      description: "A psychological horror film directed by Jonathan Demme, based on the novel by Thomas Harris.",
      releaseDate: "1991-02-14"
    },
    {
      id: 19,
      movieName: "Braveheart",
      description: "An epic historical war film directed by Mel Gibson, based on the life of William Wallace.",
      releaseDate: "1995-05-24"
    },
    {
      id: 20,
      movieName: "Gladiator",
      description: "An epic historical drama film directed by Ridley Scott, set in ancient Rome.",
      releaseDate: "2000-05-01"
    },
    {
      id: 21,
      movieName: "Django Unchained",
      description: "A Western film directed by Quentin Tarantino, set in the American South during the antebellum era.",
      releaseDate: "2012-12-25"
    },
    {
      id: 22,
      movieName: "The Usual Suspects",
      description: "A mystery thriller film directed by Bryan Singer.",
      releaseDate: "1995-07-19"
    },
    {
      id: 23,
      movieName: "The Green Mile",
      description: "A fantasy crime drama film directed by Frank Darabont, based on the novel by Stephen King.",
      releaseDate: "1999-12-10"
    },
    {
      id: 24,
      movieName: "American History X",
      description: "A drama film directed by Tony Kaye.",
      releaseDate: "1998-10-30"
    },
    {
      id: 25,
      movieName: "The Pianist",
      description: "A biographical war film directed by Roman Polanski.",
      releaseDate: "2002-09-24"
    },
    {
      id: 26,
      movieName: "The Departed",
      description: "A crime thriller film directed by Martin Scorsese, based on the Hong Kong film Infernal Affairs.",
      releaseDate: "2006-10-06"
    },
    {
      id: 27,
      movieName: "The Intouchables",
      description: "A French comedy-drama film directed by Olivier Nakache and Éric Toledano.",
      releaseDate: "2011-11-02"
    },
    {
      id: 28,
      movieName: "The Lion King",
      description: "An animated musical film directed by Roger Allers and Rob Minkoff.",
      releaseDate: "1994-06-15"
    },
    {
      id: 29,
      movieName: "The Great Gatsby",
      description: "A romantic drama film directed by Baz Luhrmann, based on F. Scott Fitzgerald's novel.",
      releaseDate: "2013-05-10"
    },
    {
      id: 30,
      movieName: "The Shining",
      description: "A psychological horror film directed by Stanley Kubrick, based on Stephen King's novel.",
      releaseDate: "1980-05-23"
    },
    {
      id: 31,
      movieName: "Inglourious Basterds",
      description: "A war film directed by Quentin Tarantino.",
      releaseDate: "2009-08-21"
    },
    {
      id: 32,
      movieName: "The Social Network",
      description: "A biographical drama film directed by David Fincher, based on the founding of Facebook.",
      releaseDate: "2010-09-24"
    },
    {
      id: 33,
      movieName: "The Revenant",
      description: "A survival drama film directed by Alejandro G. Iñárritu.",
      releaseDate: "2015-12-25"
    },
    {
      id: 34,
      movieName: "Jurassic Park",
      description: "A science fiction adventure film directed by Steven Spielberg, based on Michael Crichton's novel.",
      releaseDate: "1993-06-11"
    },
    {
      id: 35,
      movieName: "Eternal Sunshine of the Spotless Mind",
      description: "A romantic science fiction film directed by Michel Gondry.",
      releaseDate: "2004-03-19"
    },
    {
      id: 36,
      movieName: "A Beautiful Mind",
      description: "A biographical drama film directed by Ron Howard, based on the life of John Nash.",
      releaseDate: "2001-12-13"
    },
    {
      id: 37,
      movieName: "Dead Poets Society",
      description: "A drama film directed by Peter Weir.",
      releaseDate: "1989-06-09"
    },
    {
      id: 38,
      movieName: "The Prestige",
      description: "A mystery thriller film directed by Christopher Nolan.",
      releaseDate: "2006-10-20"
    },
    {
      id: 39,
      movieName: "Memento",
      description: "A psychological thriller film directed by Christopher Nolan.",
      releaseDate: "2000-09-05"
    },
    {
      id: 40,
      movieName: "La La Land",
      description: "A musical romantic drama film directed by Damien Chazelle.",
      releaseDate: "2016-12-09"
    },
    {
      id: 41,
      movieName: "The Matrix Reloaded",
      description: "A science fiction action film directed by the Wachowskis.",
      releaseDate: "2003-05-07"
    },
    {
      id: 42,
      movieName: "The Matrix Revolutions",
      description: "The final installment in The Matrix trilogy, directed by the Wachowskis.",
      releaseDate: "2003-11-05"
    },
    {
      id: 43,
      movieName: "The Sixth Sense",
      description: "A psychological horror film written and directed by M. Night Shyamalan.",
      releaseDate: "1999-08-06"
    },
    {
      id: 44,
      movieName: "American Beauty",
      description: "A drama film directed by Sam Mendes.",
      releaseDate: "1999-09-08"
    },
    {
      id: 45,
      movieName: "The Hangover",
      description: "A comedy film directed by Todd Phillips.",
      releaseDate: "2009-06-05"
    },
    {
      id: 46,
      movieName: "Interstellar",
      description: "A science fiction film directed by Christopher Nolan.",
      releaseDate: "2014-11-07"
    },
    {
      id: 47,
      movieName: "The Wolf of Wall Street",
      description: "A biographical black comedy crime film directed by Martin Scorsese.",
      releaseDate: "2013-12-25"
    },
    {
      id: 48,
      movieName: "The Grand Budapest Hotel",
      description: "A comedy film directed by Wes Anderson.",
      releaseDate: "2014-02-06"
    },
    {
      id: 49,
      movieName: "The Martian",
      description: "A science fiction film directed by Ridley Scott, based on Andy Weir's novel.",
      releaseDate: "2015-10-02"
    },
    {
      id: 50,
      movieName: "Avengers: Endgame",
      description: "A superhero film directed by Anthony and Joe Russo, part of the Marvel Cinematic Universe.",
      releaseDate: "2019-04-26"
    }
];
  
