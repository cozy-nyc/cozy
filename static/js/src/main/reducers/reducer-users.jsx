const UserReducer = (state={}, action) => {
   switch (action.type) {
      case "CHANGE_NAME":{
         state = {... state, name: action.payload}
         break;
      }
      case "CHANGE_AGE":{
         state = {... state, age: action.payload}
         break;
      }
      default:

   }
   return state;
};

export default UserReducer;
