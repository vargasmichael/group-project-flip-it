import React, { useState, useEffect } from "react";
import styles from '../styles/HOF.module.css';

export default function HOF(){
  const [data, setData] = useState([]);
  const [sortBy, setSortBy] = useState('success_rate');

  useEffect(() => {
    fetch('/api/mydata')
      // that api will change to the sql data
      .then((response)=>response.json())
      .then((data)=>setData(data));
    }, [])

        
    const toggleSortBy = () => {
      if (sortBy === 'success_rate') {
        setSortBy('total_win');
      } else {
        setSortBy('success_rate');
      }
    };

    let sortedData = data;
    if (sortBy === 'success_rate') {
      sortedData = data.sort((a,b) => b.success_rate - a.success_rate);
    } else {
      sortedData = data.sort((a,b) => b.total_win - a.total_win);
    }
    

    return (
      <div className = {styles.body}>
        <h1>Hall of fame!</h1>
        <button onClick = {toggleSortBy}>
          Sort by {sortBy === 'success_rate' ? 'Total Wins' : 'Success Rate'}
        </button>
        <table className = {styles.table}>
          <thead>
            <tr>
              <th></th>
              <th>Player</th>
              <th>Games Won</th>
              <th>Success Rate</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>IMAGE</td>
              <td>UserTest</td>
              <td>7 wins</td>
              <td>72%</td>
            </tr>
            {data.map((item)=>(
              success_rate = item.total_wins / item.total_games * 100,
              <tr key = {item.id}>
                <td>{item.image}</td>
                <td>{item.username}</td>
                <td>{item.total_wins} wins</td>
                <td>{success_rate}%</td>
              </tr>
            ))}
          </tbody>
        </table>
        
      </div>
    
    )
}



// serialize_rules = ()
// id = db.Column(db.Integer, primary_key=True)
// username = db.Column(db.String)
// _password_hash = db.Column(db.String)
// total_wins = db.Column(db.Integer)
// total_games = db.Column(db.Integer)