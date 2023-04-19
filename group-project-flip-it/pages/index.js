import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import React, { useEffect, useState } from "react";
import Tiles_on_Board from "./Tiles_on_Board";
import Each_tile from "./Each_tile";
// import HOF from './HOF';


const inter = Inter({ subsets: ['latin'] })

function Home() {
//  const [gameTiles, setgameTiles] = useState([]); //part 1 late - create const [] to hold the tiles, import useState, replace consolelog in fetch with setgameTiles (will be an empty array)

//   useEffect(() => {
//     fetch("http://localhost:8000/tiles") //part 1 early -main db; plural variable
//       .then((res) => res.json())
//       .then((gameTiles) => setgameTiles(gameTiles)); // conlog - full array of obj was present set implies it will watch tiles
//   }, []);

  return (
    <div>
      <Each_tile />
      <Tiles_on_Board />
    </div>
  );
}

export default Home;
