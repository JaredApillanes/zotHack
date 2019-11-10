import logo from "./league-of-legends-logo.png";
import React from "react";
import Button from "react-bootstrap/Button";

function Home(e) {
    return (
        <div className="App-header">
            <header>
            <img src={logo} className="App-logo" alt="logo" />
            </header>
        <Button variant = 'secondary'>Play</Button>
        </div>
    )
}

export default Home