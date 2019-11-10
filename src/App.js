import React from 'react';
import {Route, Switch, Router} from 'react-router-dom';
import history from './history.js';
import './App.css';
import Home from './app/views/Home/Home'
import Play from './app/views/Play/Play'
import ScoreScreen from "./app/views/ScoreScreen/ScoreScreen";


function App() {
    return (
        <div className="App">
            <Router history={history}>
                <Switch>
                    <Route exact path='/' component={Home}/>
                    <Route exact path='/Play' component={Play}/>
                    <Route exact path='/Score' component={ScoreScreen}/>
                </Switch>
            </Router>
        </div>
    );
}

export default App;
