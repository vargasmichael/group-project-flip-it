import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function Main() {
  const Ranks = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
  ];
  const Suits = ["Clubs", "Hearts", "Diamonds", "Spades"];
  let Deck = [];

  const [deck, setDeck] = useState([]);
  const [score, setScore] = useState(0);
  const [card1, setCard1] = useState(null);

  useEffect(() => {
    const newDeck = [];
    let value = 1;

    Ranks.forEach((rank) => {
      Suits.forEach((suit) => {
        let cardValue = value;

        // high-low values feature (that a '2' is a 2, Jack is 11, etc)
        if (rank === "Jack" || rank === "Queen" || rank === "King") {
          cardValue = 10;
        } else if (rank === "Ace") {
          cardValue = 11;
        }

        newDeck.push({ name: `${rank} of ${suit}`, value: cardValue });
      });
      value++;
    });

    // shuffle feature
    const shuffledDeck = newDeck.sort(() => Math.random() - 0.5);

    setDeck(shuffledDeck);
  }, []);

  const handleDeal = () => {
    setCard1(deck.pop());
    setDeck([...deck]);
  };

  return (
    <div>
      <h1>Flippit</h1>
      <button onClick={handleDeal}>Deal</button>
      {card1 && <p>{`Card dealt: ${card1.name}`}</p>}
      <p>{`Score: ${score}`}</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Main} />
      </Switch>
    </Router>
  );
}

export default App;
