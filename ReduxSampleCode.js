//Step 1:  Action Creators
//type is usually in all caps with understore
//payloads are usually arguments to action creator
//nearly all action creators gonna look like this

const createPolicy =(name, amount)=> {
    return {
        type: 'CREATE_POLICY',
        payload: {
            name: name,
            amount: amount
        }
    } ;
};

const deletePolicy =(name)=>{
    return {
        type:'DELETE_POLICY',
        payload: {
            name: name
        }
    };
};

const createClaim = (name,amount)=>{
    return {
        type: 'CREATE_CLAIM',
        payload: {
            name: name,
            amount: amount
        }
    };
};

//Step 2: Create Reducers
//dispatch is part of redux library
//each function is a different 'department'

const claimsHistory =(existingClaims=[], action)=>{
    if(action.type==='CREATE_CLAIM'){
        return [...existingClaims, action.payload]; 
    }
    return existingClaims;
    
    //takes list of array, all records in ... added into new array, then addes action.payload to the end
    //...means you don't nest it.
    
};

//assumes we have $100 cash in the business
const accounting =(existingMoney=100, action)=>{
    if(action.type ==='CREATE_CLAIM'){
        return existingMoney - action.payload.amount;
    } else if(action.type==='CREATE_POLICY'){
        return existingMoney + action.payload.amount;
    }
    return existingMoney;

};

const policies =(policyList=[], action)=> {
    if(action.type==='CREATE_POLICY'){
        return [...policyList, action.payload.name];
    } else if (action.type==='DELETE_POLICY'){
        return policyList.filter(name=> name !== action.payload.name);
    }
    return policyList;
};

//Step 3: You throw this all in a store

//Creates Store
const {createStore, combineReducers} = Redux;

//Combines all reducers
const ourDepartments=combineReducers({
    accounting:accounting,
    claimsHistory:claimsHistory,
    policies: policies
});

//initiates store
const store = createStore(ourDepartments);
store;

//how to dispatch new information into store
//each dispatch is a separate execution of entire redux cycle
const action = createPolicy('Alex', 20);
store.dispatch(action);
store.dispatch(createPolicy('Jim', 30)); //also can
//gets central respository of data
store.getState();