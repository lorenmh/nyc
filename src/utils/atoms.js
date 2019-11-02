export default str => (
  str
  .join()
  .split(/\s+/)
  .filter(x => x)
  .reduce((a, c) => ((a[c] = Symbol(c) || 1) && a), {})
);
