import logo from "../../../logo.svg";
import React from "react";
import Button from 'react-bootstrap/Button';

function Home(e) {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
                <Button>Test Button</Button>

            </header>
        </div>
    )
}

export default Home