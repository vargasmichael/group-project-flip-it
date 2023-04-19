import React, { useState, useEffect } from "react";
// import "./Tiles_on_Board.css";
import Each_tile from "./Each_tile";

function Tiles_on_Board() {
  const [gameTiles, setGameTiles] = useState([]);
  const [matchedTiles, setMatchedTiles] = useState(0);
  //part 1 late - create const [] to hold the heros, import useState, setGameTiles (will be an empty array)
  useEffect(() => {
    // fetch("https://cataas.com/cat/cage/width/200/height/300")
    fetch("https://picsum.photos/")
      .then((res) => res.json())
      .then((gameTiles) => console.log(gameTiles)); // set implies it will watch tiles
  }, []);
  // pass 'initialTiles' to 'setGameTiles' to set the initial state of the game
  useEffect(() => {

  ///how to create an array of 16 tiles
  const initialTiles = Array(16)
    .fill(null)
    .map((_, index) => ({
      id: index,
      // generate a value between 1 and 8 to use for each tile, see Math.floor
      value: Math.floor(index / 2) + 1,
      flipped: false,
      matched: false,
      image: index < 2 ? `https://picsum.photos/width/200/height/300?random=${((index - 2) / 2) + 1}` : null,
    }));
    setGameTiles(initialTiles);
  }, []);


  //by setting the 'flipped' property to true, the tile is flipped
  const flipTile = (id) => {
    const newTiles = gameTiles.map((tile) => {
      if (tile.id === id) {
        return {
          ...tile,
          flipped: true,
        };
      }
      return tile;
    });
    setGameTiles(newTiles);
  };
  // reset tiles if they don't match by setting 'flipped' property to false, the '...tile' is the spread operator, it copies the properties of the tile obj and sets them to the new obj, the 'flipped' property is then set to false
  const resetTiles = () => {
    const newTiles = gameTiles.map((tile) => {
      return {
        ...tile,
        flipped: false,
      };
    });
    setGameTiles(newTiles);
  };

  // checks if flipped tiles match and resets tiles if they don't
  const checkMatch = () => {
    const flippedTiles = gameTiles.filter((tile) => tile.flipped);
    if (flippedTiles.length === 2) {
      //restricts tiles from flipping if there are already two flipped
      if (flippedTiles[0].value === flippedTiles[1].value) {
        setMatchedTiles(matchedTiles + 1);
        resetTiles();
      } else {
        //resets flipped tiles after 1 second if they don't match
        setTimeout(resetTiles, 1000);
      }
    }
  };
  return (
    <div>
      <div className="tile-container">
        {/* maps through the array of tiles and returns a div for each tile, the key is the id of the tile, the className is the tile-open or tile-closed class, the onClick is the flipTile function, the ternary operator checks if the tile is flipped, if it is, it returns the image, if not, it returns portion of the floral design */}
        {gameTiles.map((tile) => (
          <div
            key={tile.id}
            className={`tile ${tile.flipped ? "tile-open" : "tile-closed"}`}
            onClick={() => flipTile(tile.id)}
          >
            {tile.flipped ? (
              <img src={tile.image} alt={tile.value} />
            ) : (
              <i className="fa fa-star game-tile"></i>
            )}
          </div>
        ))}
      </div>
      {matchedTiles === 8 && (
        <div className="overlay-win">
          <h2>You Win!</h2>
          <button id="replay">Play Again</button>
        </div>
      )}
    </div>
  );
}
export default Tiles_on_Board;
