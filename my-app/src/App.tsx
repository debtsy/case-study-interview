// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import SearchPage from './SearchPage';
import AccountDetails from './AccountDetails';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" Component={SearchPage} />
      </Switch>
    </Router>
  );
}

export default App;
