import React from "react";

function Each_tile({ tile, onClick, Image }) {

  //   below, in the return:render tile if it is flipped
  //   'tile' object initialized here
  // if tile.flipped property is true, show the image
  
  return (
    <>
      <div className="tile" onClick={() => onClick(tile)}>
        {tile && tile.flipped ? (
          <Image src={tile.image} alt={`Tile ${tile.value}`} />
        ) : null}
      </div>
    </>
  );
}
export default Each_tile;
