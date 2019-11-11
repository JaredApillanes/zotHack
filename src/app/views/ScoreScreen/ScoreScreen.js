import React, {useState, useEffect} from "react";
import './ScoreScreen.css';
import Table from "react-bootstrap/Table";

import axios from "axios";


function ScoreScreen() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:5000/player/list").then(res => {
            console.log(res.data)
             setUsers(res.data);
                // .map((user, s) => (
                //         <div index={s} key={s}>
                //             <tr>
                //                 <td>user.username</td>
                //                 <td>user.score</td>
                //             </tr>
                //         </div>
                //     ))
        }).catch(() => {console.log("NOOOOO")})
    }, []);

        return (
            <div class="App-header">
                <Table class="Score">
                    <thead>
                    <th>
                        USERNAME
                    </th>
                    </thead>
                    <th>
                        SCORE
                    </th>
                    <tbody>
                    {JSON.stringify(users)}
                    </tbody>
                </Table>
            </div>
        )
    }

    export default ScoreScreen;