import React from 'react';


const CommentDetails = (props) => {
    return (
        <div className="ui container comments">
            <div className ="comment">
                <a href="/" className="avatar">
                    <img alt="avatar" src={props.imgSrc} />
                </a>
                <div className="content">
                    <a href="/" className="author">
                        {props.author}
                    </a>
                    <div className="metadata">
                        <span className="date"> {props.timeAgo} </span>
                    </div>
                    <div className="text">
                        {props.comment}
                    </div>
                </div>
            </div>
        </div>
    );
};

//you need an export statement to make the CommentDetails exportable
export default CommentDetails;
