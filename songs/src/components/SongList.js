import React, {Component} from 'react';
import {connect} from 'react-redux';

import {selectSong} from '../actions';

class SongList extends Component {
    renderList(){
        return this.props.songs.map((song)=>{
            return(
                <div className='item' key={song.title}>
                    <div className='right floated content'>
                        <button 
                            className='ui button primary'
                            onClick={()=>this.props.selectSong(song)}
                        >
                            Select
                        </button>
                    </div>
                    <div className='content'>
                        {song.title}
                    </div>
                </div>
            );
        });
    };
    
    render() {
        return <div className='ui divided list'>{this.renderList()}</div>
    }
}

//this will always be the form of state mapping function
const mapStateToProps = (state)=>{
    console.log(state);
    return {songs: state.songs}
}

//this will always be how you connect your state mapping and your component
//takes selct song action creater and passes it as a prop
export default connect(mapStateToProps, {selectSong:selectSong})(SongList);

