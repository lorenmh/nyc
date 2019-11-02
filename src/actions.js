import atoms from './utils/atoms';

export const actions = atoms`
  INCREMENT_COUNT
  DECREMENT_COUNT
`

export const incrementCount = () => ({
  type: actions.INCREMENT_COUNT,
});

export const decrementCount = () => ({
  type: actions.DECREMENT_COUNT,
});
