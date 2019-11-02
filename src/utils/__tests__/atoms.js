import atoms from '../atoms';

const data = atoms`
  one
  two
  three
`;

it('creates properties with the correct keys', () => {
  expect(data).toHaveProperty('one');
  expect(data).toHaveProperty('two');
  expect(data).toHaveProperty('three');
})

it('only has symbol properties', () => {
  Object.values(data).forEach(v => expect(typeof v).toBe('symbol'));
});

it('only has unique symbols for each property', () => {
  const symbols = new Set(Object.values(data));
  expect(symbols.size).toBe(3);
});
