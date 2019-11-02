import { actions } from './actions';

export default (state, action) => {
  switch (action.type) {
    case actions.INCREMENT_COUNT:
      return {
        ...state,
        count: state.count + 1,
      };
    case actions.DECREMENT_COUNT:
      return {
        ...state,
        count: state.count - 1,
      };
    default:
      return state;
  }
};
