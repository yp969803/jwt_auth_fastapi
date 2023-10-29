import React from "react";
import "./style.scss";
import Login from "./Login";
import Register from "./Register";
import {
  BrowserRouter as Router,
  Link,
  Route,
  Routes,
  // redirect,
} from "react-router-dom";
import Home from "./Home";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      messages: [],
    };
  }

  handleNewMessage = (text) => {
    this.setState({
      messages: [
        ...this.state.messages,
        { me: true, author: "Me", body: text },
      ],
    });
  };

  render() {
    return (
      <Router>
        <div className="App">
          <Routes>
            <Route path="/" element={<Home messages={this.state.messages} handleNewMessage={this.handleNewMessage} />} />
            <Route path="/login" Component={Login} />
            <Route path="/register" Component={Register} />
          </Routes>
        </div>
      </Router>
    );
  }
}

export default App;
