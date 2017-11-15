# Selektory CSS

## Pseudoklasy

* `:link`, `:visited`, `:hover`, `:active` – łącze nieodwiedzone, odwiedzone, nad którym jest kursor, zaznaczone kursorem (klikane);
* `:focus`, `:first-child` – element z fokusem, pierwsze dziecko;
* `:target`, `:nth-child()`, `:last-child`, `:checked` – pseudoklasy wprowadzone w CSS 3

## Pseudoelementy

* `::first-line`, `::first-letter`, `::before`, `::after` – pierwsza linia, pierwsza litera, przed i po elemencie.

## Precyzja selektorów

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

Wybranie wszystkich elementów w znaczniku `<div>`:

* `div * {border: 1px solid red;}`

# Identyfikatory czy klasy

Kolor odnośników w nagłówku strony `<div id="header">`:

```
#header {background: black;}
#header a {color: white;}
```

Próba zmiany kolorów na stronie kontaktowej (nie zadziała!):

```
#header {background: #bbb;}
.navlinks a {color: #257000;}
```

Rozwiązanie 1:

```
#header a, .navlinks a {color: #257000;}
```

Zmiana identyfikatora na klasę: `<div class="header">`:

```
.header {background: black;}
.header a {color: white;}
```

Zmiana kolorów na stronie kontaktowej:

```
.header {background: #bbb;}
.navlinks a {color: #257000;}
```

## Identyfikatory + klasy

Nadaj wszystkim panelom: obramowanie, kolor tła, kolor czcionki, oraz czcionkę. Następnie pogrub czcionkę panelu "pogoda" i zmień kolor tła panelu "ostatnie".

```
<div class="panel" id="pogoda">
<div class="panel" id="wiadomosci">
<div class="panel" id="ostatnie">
```

```
#pogoda {...}
.panel {...}
#pogoda.panel {...}
```

## Wiele klas

```
<div class="panel pogoda">
<div class="panel wiadomosci">
<div class="panel ostatnie">
```

```
.panel {...}
.pogoda {...}
.panel.pogoda {...}
```

# Selektory atrybutów

Selektory atrybutów mają precyzję: 0,0,1,0

## Atrybuty

* `a[href] {color: green;}`
* `img[src="/img/logo.png"] {...}`

## Klasy

* `div[class="panel"] {...}`
* `div[class~="panel"] {...}`
* `div.panel {...}`
* `img[alt~="obraz"]`
* `*[title~="2016"]`

## Identyfikatory

* `p[id="naglowek"] {font-weight: normal; font-style: italic;}`
* `p#naglowek {font-weight: bold;}`

# Selektory podłańcuchów

* `a[href*="w3.org"] {...}` – * oznacza, że podany ciąg musi wystąpić;
* `a[href*="/news"] {...}`
* `img*[src="logo.png"] {...}`
* `a[href^='ftp']` – ^ znajduje dopasowanie na początku ciągu;
* `a[href$='.pdf'] {padding-right: 18px; background: url(/pix/pdf.png) 100% 50% no-repeat;}` – $ znajduje dopasowanie na końcu ciągu;

**Zadanie**: Używając selektora podłańcuchów, zastosuj obramowanie do dwóch pierwszych obrazków:

```
<img src="rys1.jpg" alt="Rysunek 1." />
<img src="rys2.jpg" alt="Rysunek 2." />
<img src="rys3.jpg" alt="Zobacz rysunek." />
```

# Selektory dzieci

* `div#header a {...}` – wszystkie tagi `a`, potomkowie, w `div#header`;
* `ol > li {list-style-type: upper-alpha;}` – wszystkie elementy `li`, dzieci `ol`;

```
<ol>
  <li>Punkt A</li>
  <li>Punkt B
    <ul>
      <li>Podpunkt</li>
      <li>Podpunkt</li>
      <li>Podpunkt</li>
    </ul>
  </li>
  <li>Punkt C</li>
  <li>Punkt D</li>
  <li>Punkt E</li>
</ol>
```
# Selektory elementów siostrzanych

Wybór elementu występującego bezpośrednio za innym:

```
h2 {margin-bottom: 0;}
h2 + p {margin-top: 0;}
```

```
<h2>Nagłówek 2</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
<h2>Nagłówek 3</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
```

Wybór elementu występującego za elementem, ale nie bezpośrednio:

* `h1 ~ ul {list-style-type: lower-alpha;}`

```
<body>
  <ul><li>El 1<li></ul>
  <h1>Nagłówek</h1>
  <p>Akapit</p>
  <ul><li>El 1<li></ul>
  <ul><li>El 1<li></ul>
  <ul><li>El 1<li></ul>
  <h2>Nagłówek</h2>
  <p>Akapit</p>
  <ul><li>El 1<li></ul>
</body>
```

# Pseudoelementy

* `li:before {content: "Pkt: "; border-bottom: 1px solid gray;}`
* `li:before {content: "\BB ";}`
* `a[href]:after {content: " [" attr[href] "]"; font-size: smaller;}`

Zob. technika stopniowego ulepszania (ang. *progressive enhancement*),
m. in w stylach druku: http://alistapart.com/articles/goingtoprint.
