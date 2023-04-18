import '@/styles/globals.css'

// export default function App({ Component, pageProps }) {
//   return <Component {...pageProps} />
// }

import React, { useEffect } from 'react';
import socketIOClient from 'socket.io-client';

function App() {
  useEffect(() => {
    const socket = socketIOClient('http://localhost:3000');

    socket.on('connect', () => {
      console.log('Connected');
      socket.emit('my_event', {data: 'Connected'});
    });

    socket.on('my_response', (data) => {
      console.log(data);
    });

    return () => {
      socket.disconnect();
    }
  }, []);

  return (
    <div>
      <h1>Hello, World!</h1>
    </div>
  );
}

export default App;