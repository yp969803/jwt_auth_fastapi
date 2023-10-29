import React from "react";
import MainBox from "./MainBox";
import Navbar from "./Navbar";
import MessageList from "./MessageList";
import MessageForm from "./MessageForm";

function Home(props) {
  return (
    <div>
      <Navbar />
      <MainBox />
      <div className="chatbot">
        <MessageList messages={props.messages} />
        <MessageForm onMessageSend={props.handleNewMessage} />
      </div>
    </div>
  );
}

export default Home;
