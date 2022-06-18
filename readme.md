# Sider.py

## What?

A _Redis-like_ data-store practice project.
The name is just `redis` reversed.

## Design decisions

- Should use **TDD**
- Should use **functional core, imperative shell**

The main rationale behind using a functional core is to:

1. Write tons of unit tests, as formal provability is easy. Every function takes an input, returns a new copy of internal core. There's no mutable state.
2. Shell easily replaceable. Right now it's a CLI, it can easily be hooked to a Flask API or Desktop GUI as the shell is just a layer which calls the core and displays the output

### Limitations

- Limited to `str` <> `str` mapping
- Some compromises had to be made to make the core functional (i.e unset)

## Resources

- [Harry Percival: Obey the Testing Goat!](https://www.obeythetestinggoat.com/pages/book.html#toc)
- [Gary Bernhardt: screencast on Functional Core, Imperative Shell](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)
