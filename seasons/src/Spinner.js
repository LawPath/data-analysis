import React from 'react';

const Spinner = props => {
    return (
        <div className="ui active dimmer">
        <div className="ui loader">
            {props.message}
        </div>
    </div>
    )
    
};

Spinner.defaultProps = {
    message: "Pending request"
};

export default Spinner;