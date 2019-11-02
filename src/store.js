import { createStore, applyMiddleware } from 'redux';
import thunkMiddleware from 'redux-thunk';
import { createLogger } from 'redux-logger';

import rootReducer from './reducers';

const initialState = {
  count: 0,
}

const hooks = applyMiddleware(thunkMiddleware, createLogger());

export default createStore(
  rootReducer,
  initialState,
  hooks,
);
