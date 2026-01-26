## Task

I would like to create a custom directive for rendering a special type of TOC tree. An example of its use is given below,

```rst
.. book-tree:
    :max-depth: <depth>
    :caption: <caption>
    :width: <width>

    * - chapter-name-i
      - chapter-numeral-i
      - chapter-location-i
    * - chapter-name-ii
      - chapter-numeral-ii
      - chapter-location-ii
```

I would like this to render a "book-like" TOC tree, e.g. something like (this is approximated through text),

```text
chapter-name-i ........................ <a href="chapter-location-i">chapter-numeral-i</a>
chapter-name-ii ....................... <a href="chapter-location-ii">chapter-numeral-ii</a>
```

The essential constraint of the custom TOC tree is the number of dots should expand or contract to the fit the size of the panel, and the right hand numerals should always be lined up.

The `max-depth` and `caption` arguments of the directive should perform the same function as the standard `toctree` directive.