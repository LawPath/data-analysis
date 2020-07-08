// import React and React DOM libraries
import React from 'react';
import ReactDOM from 'react-dom';
//Custom Function
function getButtonText(){
    return "Click mii"
} 

// Create a react component

const App = () => {
    //const buttonText= 'click me ;)';
    
    return (
        <div>
            <label className = "label" for="name">
                Enter name: 
            </label>
            <input id ="name" text="text"></input>
            <button style={{backgroundColor: 'blue', color: 'white'}}>
                {getButtonText()}
            </button>
        </div>
    )
};

// Take react component and show on screen
ReactDOM.render(
    <App />, 
    document.querySelector("#root") //standard function in all browser
);