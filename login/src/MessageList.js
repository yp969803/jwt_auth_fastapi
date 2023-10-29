import React from "react";
import Message from "./Message";
// import "./MessageList.css";

function MessageList(props) {
  return (
    <div className="MessageList">
      {props.messages.map((message, i) => (
        <Message key={i} {...message} />
      ))}
    </div>
  );
}

export default MessageList;
