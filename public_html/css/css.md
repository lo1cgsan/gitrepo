# Precyzja selektorów

* każdy selektor elementu wnosi precyzję 0,0,0,1
* każda klasa, pseudoklasa, selektor atrybutu mają precyzję 0,0,1,0
* każdy identyfikator ma precyzję 0,1,0,0

## Określ precyzję poniższych selektorów:

* div ul ul li
* div.aside ul li
* a:hover
* div.navlinks a:hover
* \#title em
* h1#title em
* div#header { background: purple; }
* `<div id="header" style="background: blue;">`

# Reguła ważności

* a:hover {color: red !important; text-decoration: none;}

# Zapis skrócony

* `strong { font: bold italic small-caps medium/1.2 Verdana, sans-serif; }`
* `strong { font: medium Verdana, sans-serif}`

**Nieokreślone właściwości w zapisie skróconym przyjmują wartości domyślne!**

* np.: `strong {font: normal normal normal small/normal Verdana, sans-serif;}`

## Przesłanianie własności:

```
border: 3px dotted black
border-left-color: red;
```

## Wyjątki:

* margin: 1em; margin: 1em 1em 1em 1em;
* padding: 10px 25px; padding: 10px 25px 10px 25px;

# Selektor uniwersalny

* `div * {border: 1px solid red;}`
