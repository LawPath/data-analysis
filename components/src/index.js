import React from 'react';
import ReactDOM from 'react-dom';
import faker from 'faker';
import CommentDetails from './CommentDetails'; //you need to specify filepath. no need to stick .js in it -- weback does it. Components are inputted as if they were JSX tags
import ApprovalCard from './ApprovalCard'


const App = () => {
    return(
        <div className="ui container comments">
            <ApprovalCard>
                <CommentDetails 
                    author="Sam" 
                    timeAgo="Today at4:45" 
                    comment="hello" 
                    imgSrc={faker.image.avatar()}
                />
            </ApprovalCard>
            
            <CommentDetails 
                author ="Alex" 
                timeAgo="Today at 2:45" 
                comment="haller" 
                imgSrc={faker.image.avatar()} 
            />
            <CommentDetails 
                author ="Jane" 
                timeAgo="Yesterday at 6:45" 
                comment="char" 
                imgSrc={faker.image.avatar()} 
            /> 
        </div>
    );
};

ReactDOM.render(
    <App />, document.getElementById('root')
);
