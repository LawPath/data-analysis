import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor(props){
    super(props); //supersedes the props constructor in React.Component
    
    //initialise state object
    this.state={ lat: null};
    window.navigator.geolocation.getCurrentPosition(
      position=> {
        this.setState({lat: position.coords.latitude}); //do not direct assign to .state. If you change it, you always have to call set state
      },
      err => {
        this.setState({errorMessage: err.message});
      }
    );

  }
  
  render(){
    if (this.state.errorMessage && !this.state.lat) {
      return <div>Error: {this.state.errorMessage}</div>
    }

    if(!this.state.errorMessage && this.state.lat){
      return <div>Latitude: {this.state.lat}</div>
    }

    if(!this.state.errorMessage && !this.state.lat) {
      return <div>Loading...</div>
    }

    
  }
}


ReactDOM.render(
  <App />,
  document.getElementById('root')
);
