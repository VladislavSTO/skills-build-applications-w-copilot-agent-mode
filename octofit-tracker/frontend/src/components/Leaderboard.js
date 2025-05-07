import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    fetch('https://fluffy-space-meme-v5j4g4x4g9rfwvgj-8000.app.github.dev/api/leaderboard/')
      .then(res => res.json())
      .then(data => setEntries(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="mb-4 display-5">Leaderboard</h1>
      <div className="card shadow">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-primary">
              <tr>
                <th>Team</th>
                <th>Points</th>
                <th>Week</th>
              </tr>
            </thead>
            <tbody>
              {entries.map((entry, idx) => (
                <tr key={idx}>
                  <td>{entry.team}</td>
                  <td>{entry.points}</td>
                  <td>{entry.week}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
